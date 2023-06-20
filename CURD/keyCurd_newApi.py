import hashlib
import hmac
import base64
import logging

from flask import Flask,request
from flask_restful import Api, Resource
import requests
import xmltodict
from datetime import datetime
import json

app = Flask(__name__)
api = Api(app)

# access_key = '3P8O9R8K6F53XPXQ856N'
# secret_key = 'zcNbACa9NfezqwINXhfZMXawmsqjQDLeEb8bgsxp'
# endpoint_url = 'http://10.82.2.14:8080'


with open('config.json') as file:
    file_content = json.load(file)
access_key = file_content.get("access_key")
secret_key = file_content.get("secret_key")
endpoint_url = file_content.get("endpoint_url")



def generate_signature(secret_key, string_to_sign):
    signature = hmac.new(secret_key.encode('utf-8'), string_to_sign.encode('utf-8'), hashlib.sha1)
    return base64.b64encode(signature.digest()).decode('utf-8')

def make_api_request(http_verb, canonicalized_resource):
    try:
        headers = {
            'Host': endpoint_url,
            'Date': datetime.utcnow().strftime('%a, %d %b %Y  %H:%M:%S GMT'),
        }

        # content_md5 = ''
        # content_type = ''
        date = headers['Date']
        canonicalized_amz_headers = ''
        # string_to_signature = f'{http_verb}\n{content_md5}\n{content_type}\n{date}\n{canonicalized_amz_headers}{canonicalized_resource}'

        string_to_signature = f'{http_verb}\n\n\n{date}\n{canonicalized_amz_headers}{canonicalized_resource}'

        signature = generate_signature(secret_key, string_to_signature)
        authorization_header = f'AWS {access_key}:{signature}'
        headers['Authorization'] = authorization_header

        response = requests.request(http_verb, endpoint_url + canonicalized_resource, headers=headers)
        print(response)
        return response
    except Exception as e:
        logging.error(str(e))
        return {"error":"please provide a valid credential to generate a valid signature"}


class Buckets(Resource):
    #fetch_bucket
    def get(self):
        try:
            canonicalized_resource = '/'
            response = make_api_request('GET', canonicalized_resource)

            if response.status_code == 200:
                bucket_list=[]
                xml_response = response.text
                dict_response = xmltodict.parse(xml_response)
                list_of_buckets=dict_response.get('ListAllMyBucketsResult')
                for ele in list_of_buckets.get('Buckets').get('Bucket'):

                    #print(ele.get('Name'))
                    bucket_list.append(ele.get('Name'))

                return ({'buckets': bucket_list}, 200)
            else:
                return ({"message": f'Error: {response.status_code} - {response.reason}'}), response.status_code

        except Exception as e:   #this belongs python exception
            logging.error(f'an error occured: {str(e)}')
            return ({"An error occurred": "please try again with correct crendntial "})

    #create bucket
    def put(self):
        try:
            data = request.get_json()
            print(data)
            if not data or 'bucket_name' not in data:
                return {"Error":"Please give the bucket name, it's mandatory filed"}

            bucket = data.get("bucket_name")
            canonicalized_resource = f'/{bucket}'
            response = make_api_request('PUT', canonicalized_resource)
            if response.status_code == 200:
                return ({"message": f'Bucket {bucket} created successfully.'})
            else:
                return ({"message": f'Failed to create bucket {bucket}. Error: {response.text}'})

        except requests.exceptions.ConnectionError as e:  # this belongs request module
            logging.error(f'Connection error : {str(e)}')
            return ({"Connection Error": "Connection Error Occur "})
        except requests.exceptions.RequestException as e:
            logging.error(f'Request error : {str(e)}')
            return ({"Request Exception": "Request Error Occur"})
        except Exception as e:                 #this belongs python exception
            logging.error(f'python error : {str(e)}')
            return ({"An error occurred": "Python Error Occur"}),

# delete a bucket
class DeleteBucket(Resource):
        def delete(self,bucket_name):
            try:
                canonicalized_resource = f'/{bucket_name}'
                response = make_api_request('DELETE', canonicalized_resource)
                if response.status_code == 204:
                    return ({"message": f'Bucket {bucket_name} deleted successfully.'})
                else:
                    return ({"message": f'Failed to delete bucket {bucket_name}'}), response.status_code

            except requests.exceptions.ConnectionError as e:  # this belongs request module
                logging.error(f'connection Error: {e}')
                return ({"Connection Error": "this is conncetion error occur, please try again"})

            except requests.exceptions.RequestException as e:
                # return({"Request Exception": "e"})
                logging.error(f'Request Error: {e}')
                return ({"Request Exception":"Request Error Occur"})

            except Exception as e:  # this belongs python exception
                logging.error(f'python error : {str(e)}')
                return ({"An error occurred": "Python Error Occur"}),


# api.add_resource(Buckets, '/buckets')
# api.add_resource(DeleteBucket,'/delete_buckets/<string:bucket_name>')
# #app.run(debug=True,port=5002)


#to get bucket usage of bucket

class BucketsGet(Resource):
    def get(self,bucket_name):
        try:
            bucket_avilable_check=Buckets()
            check=bucket_avilable_check.get()

            print(check)

            if bucket_name in check[0].get('buckets'):

                canonicalized_resource = f'/{bucket_name}'
                response = make_api_request('GET', canonicalized_resource)

                print(response)
                if response.status_code == 200:
                    xml_response = response.text
                    print(xml_response, 'xml string')
                    response = xmltodict.parse(xml_response)
                    bucket_name = response.get('ListBucketResult').get('Name')

                    if response.get('ListBucketResult').get('Contents') is not None:
                        bucket_contents = response.get('ListBucketResult').get('Contents')

                        result = {
                            bucket_name: [
                                {
                                    'Key': item.get('Key'),
                                    'LastModified': item.get('LastModified'),
                                    'Size': item.get('Size'),
                                    'StorageClass': item.get('StorageClass'),
                                    'Type': item.get('Type')
                                }
                                for item in bucket_contents
                            ]
                        }

                        return (result)

                    else:
                        return ({"message": "this bucket is Empty"})
                else:
                    return ({"message": f'Error: {response.status_code} - {response.reason}'}), response.status_code
            else:
                return ({"message": "this bucket is not exist, please try again give valid name of bucket"})

        except Exception as e:  # this belongs python exception
            return ({"An error occurred": e})



#this url for get, put, delete bucket
api.add_resource(Buckets, '/buckets')
api.add_resource(DeleteBucket,'/delete_buckets/<string:bucket_name>')
app.run(debug=True,port=5002)




# this url for to see Uages of buckets
api.add_resource(BucketsGet,'/bucketget/<string:bucket_name>')
app.run(debug=True,port=5000)