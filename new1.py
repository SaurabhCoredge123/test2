import requests
import xmltodict
import hashlib
import hmac
import base64
from datetime import datetime


access_key = '3P8O9R8K6F53XPXQ856N'
secret_key = 'zcNbACa9NfezqwINXhfZMXawmsqjQDLeEb8bgsxp'
endpoint_url = 'http://10.82.2.14:8080'

headers = {
    # 'Host': 'awsexamplebucket1234.us-west-1.s3.amazonaws.com',
    'Host': endpoint_url,
    'Date': datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT'),

}
def generate_signature(secret_key, string_to_sign):
    signature = hmac.new(secret_key.encode('utf-8'), string_to_sign.encode('utf-8'), hashlib.sha1)
    return base64.b64encode(signature.digest()).decode('utf-8')


def fetch_Bucket():
    try:
        http_verb= 'GET'
        content_md5 = ''
        content_type = ''
        date = headers['Date']
        canonicalized_amz_headers = ''
        canonicalized_resource = '/'
        string_to_signature = f'{http_verb}\n{content_md5}\n{content_type}\n{date}\n{canonicalized_amz_headers}{canonicalized_resource}'
        if not string_to_signature:
            return None  # Raise an exception
        #authorization header
        signature = generate_signature(secret_key, string_to_signature)  # Pass string_to_signature as an argument

        authorization_header = f'AWS {access_key}:{signature}'

        headers['Authorization'] = authorization_header
        if headers.is_valid():
            response = requests.get(endpoint_url, headers=headers)
            xml_response = response.text
            # Convert XML to JSON
            json_response = xmltodict.parse(xml_response)
            print(json_response)
            #print(response.content)
        else:
            return {"ERROR":"Authantication error"}

    except Exception as e:   #this belongs python exception
        return ({f"An error occurred": e})

result=fetch_Bucket()
print(result)

#create a bucket
def create_bucket(bucket_name):
    try:
        http_verb = 'PUT'
        content_md5 = ''
        content_type = ''
        date = headers['Date']
        canonicalized_amz_headers = ''
        canonicalized_resource = f'/{bucket_name}'
        string_to_signature = f'{http_verb}\n{content_md5}\n{content_type}\n{date}\n{canonicalized_amz_headers}{canonicalized_resource}'

        headers['Accept'] = 'application/json'
        #print(headers)

        signature = generate_signature(secret_key, string_to_signature)
        authorization_header = f'AWS {access_key}:{signature}'
        headers['Authorization'] = authorization_header
        if headers.is_valid():
            response = requests.put(endpoint_url + canonicalized_resource, headers=headers)
            if response.status_code == 200:
                print(f'Bucket {bucket_name} created successfully.')
            else:
                print(f'Failed to create bucket {bucket_name}. Error: {response.text}')
        else:
            return {"ERROR": "Authantication error"}

    except Exception as e:   #this belongs python exception
        return ({f"An error occurred": e})


bucket_name = 'my-test-buckect2323232'
result=create_bucket(bucket_name)
print(result)



#delete a bucket
def delete_bucket(bucket_name):
    try:
        http_verb = 'DELETE'
        content_md5 = ''
        content_type = ''
        date = headers['Date']
        canonicalized_amz_headers = ''
        canonicalized_resource = f'/{bucket_name}'
        string_to_signature = f'{http_verb}\n{content_md5}\n{content_type}\n{date}\n{canonicalized_amz_headers}{canonicalized_resource}'

        #Authorization header create
        signature = generate_signature(secret_key, string_to_signature)
        authorization_header = f'AWS {access_key}:{signature}'

        headers['Authorization'] = authorization_header

        if headers.is_valid():
            response = requests.delete(endpoint_url + canonicalized_resource, headers=headers)
            if response.status_code == 204:
                print(f'Bucket {bucket_name} deleted successfully.')
            else:
                print(f'Failed to delete bucket {bucket_name}. Error: {response.text}')
        else:
            return {"ERROR": "Authantication error"}

    except Exception as e:   #this belongs python exception
        return ({f"An error occurred": e})


# delete_bucket(bucket_name)
result=delete_bucket('my-test-buckect232')
print(result)















