##create  csv file / any file  and upload it in s3
#read the s3 bucket and read the csv files/ any file
#donwload the csv files


from hashlib import new
from turtle import pd

import boto
import boto.s3.connection
from boto import s3
from boto.s3 import bucket

access_key = 'YIKGZV07KGU6SWLBAVRI'
secret_key = 'dbvyNyJYpQP7hpyw5dYhxv6MWnzkwul9SWRJwAnw'

conn = boto.connect_s3(
        aws_access_key_id = access_key ,
        aws_secret_access_key = secret_key,
        host = '10.82.2.14',
        port= 8080,
        is_secure=False,               # uncomment if you are not using ssl
        calling_format = boto.s3.connection.OrdinaryCallingFormat(),
        )

#creating bucket
list =  ["jay.bucket","my-world-bucket101"]

# for ele in list:
#         bucket = conn.create_bucket(ele)
#         print(bucket, type(bucket))
#         print(bucket.name, type(bucket.name))
# print("created")



#print out bucket name
for bucket in conn.get_all_buckets():
        print(bucket.name)
print("mani")



#Deleting bucket
#single bucket delete

# bucket = conn.get_bucket("my-new-bucket")
# conn.delete_bucket(bucket)
# print("delete bucket")


# #@@@@@@# multipal bucket delete

# list =  ["chandu.bucket","my-new-bucket99"]
# for ele in list:
#         bucket = conn.get_bucket(ele)
#         conn.delete_bucket(bucket)
# print("all_clear")



#creating Object inside bucket and object is txt.file h

# bucket_obj = conn.get_bucket("my-new-bucket99")

# key = bucket_obj.new_key('hello.txt')
# key.set_contents_from_string('Hello world!! how are MR. ashok')
#
# key = bucket_obj.new_key('ram.txt')
# key.set_contents_from_string('Hello World!!, today task ios completed now whats new task ')




##########################


# def create_obje():
#         bucket_name = "my-new-bucket99"
#         bucket_obj = conn.get_bucket("my-new-bucket99")
#
#         key = bucket_obj.new_key('mani.txt')
#         key.set_contents_from_string('Hello World!!, completed task ')
# create_obje()




#$$$$$$$$$$$=====>>> create a object inside bucket and here object isa image

# bucket_obj = conn.get_bucket("jay.bucket")

# key = bucket_obj.new_key('img1.avif')
# key.set_contents_from_filename('/Users/coredge/Downloads/img1.avif')
#
#######################################
# folder
# parth = /Users/coredge/Desktop/demo/bucket_s3

# bucket_obj = conn.get_bucket("jay.bucket")
#
# key = bucket_obj.new_key('img5.avif')
# key.set_contents_from_filename('/Users/coredge/Desktop/demo/bucket_s3/img5.avif')

######################################################


# from desktop = parth == /Users/coredge/Desktop/
# bucket_obj = conn.get_bucket("jay.bucket")
#
# key = bucket_obj.new_key('img6.avif')
# key.set_contents_from_filename('/Users/coredge/Desktop/img6.avif')


# create a object inside bucket and here object isa image

# def upload():
#         bucket_obj = conn.get_bucket("jay.bucket")
#         key = bucket_obj.new_key('img4.avif')
#         key.set_contents_from_filename('/Users/coredge/Desktop/demo/bucket_s3/img4.avif')
#
# upload()

###################################

#fetch from the bucket

#listing a bucket conetent
# bucket_obj = conn.get_bucket("my-new-bucket99")
# for bucket in bucket_obj.list():
#         print("{name}".format(
#                 name = bucket.name,
#                 # created = bucket.creation_date,
#         ))


#method 2
# bucket = conn.get_bucket("jay.bucket")
# for key in bucket.list():
#         print("{name}\t{size}\t{modified}".format(
#                 name = key.name,
#                 size = key.size,
#                 modified = key.last_modified,
#         ))

#######################################
#fetch by function

# def fetch():
#         bucket = conn.get_bucket("jay.bucket")
#         for key in bucket.list():
#                 print("{name}\t{size}\t{modified}".format(
#                         name=key.name,
#                         size=key.size,
#                         modified=key.last_modified,
#                 ))
# fetch()

# for i in range(10):
#         fetch()

#####################################################



#to get and generate link to access the objects

#when publicly  allowed

# bucket_obj = conn.get_bucket("jay.bucket")
# key_obj=bucket_obj.get_key("img4.avif")
#
# key_obj.set_canned_acl("public-read")
# url = key_obj.generate_url(expires_in=0,query_auth=False)
# print(url)



#private
# def make_private():
#         bucket_obj = conn.get_bucket("jay.bucket")
#         key_obj=bucket_obj.get_key("img6.avif")
#
#         key_obj.set_canned_acl("private")
#         url = key_obj.generate_url(expires_in=0,query_auth=False)
#         print(url)
# make_private()


# def make_public():
#         bucket_obj = conn.get_bucket("jay.bucket")
#         key_obj=bucket_obj.get_key("img5.avif")
#
#         key_obj.set_canned_acl("public-read")
#
#         url = key_obj.generate_url(expires_in=0,query_auth=True)
        # #if user is authorize but can't see image but if we give time limit than he can see so that it's behave like here private.
        # print(url)

        #url = key_obj.generate_url(expires_in=5,query_auth=False)
        #if user is not authorize, it's public image so everyone access so not working expires_in.
        #expires_in = 0 means infinity time

#         print(url)
# make_public()

#######################################
#download object from the bucket

# bucket_obj = conn.get_bucket("jay.bucket")
# key = bucket_obj.get_key('img1.avif')
# key.get_contents_to_filename('/Users/coredge/Desktop/demo/Download/img1.avif')
#

# def download():
#         bucket_obj = conn.get_bucket("jay.bucket")
#         key = bucket_obj.get_key('img1.avif')
#         key.get_contents_to_filename('/Users/coredge/Desktop/demo/Download/img1.avif')
#
#
# download()


#over write upon image
# def download():
#         bucket_obj = conn.get_bucket("jay.bucket")
#         key = bucket_obj.get_key('img5.avif')
#         key.get_contents_to_filename('/Users/coredge/Desktop/demo/Download/img4.avif')
#
#         key_obj = bucket_obj.get_key("img4.avif")
#         url = key_obj.generate_url(expires_in=0, query_auth=False)
#         print(url)
#         print('downloaded successfully')
#
#
# download()

#not ---> overwrite is overcome by keyn name reverse or visevrsa



# def download():
#         bucket_name= 'jay.bucket'
#         key_name = 'img5.avif'
#         path = '/Users/coredge/Desktop/demo/Download/img5.avif'
#         bucket_obj = conn.get_bucket(bucket_name)
#         key = bucket.get_key(key_name)
#         key.get_contents_to_filename(path)
#         print('downloaded successfully')
# download()

#####################################
# delete object

# from flask import Flask, render_template
# import boto3
#
# app = Flask(__name__)
# @app.route('/')

#def get_list_bucket():
        # bucket = conn.get_bucket('jay.bucket')
        # for key in bucket.list():
        #         print(key.name)
        # print('fetched successfully')



        # s3 = boto3.client('s3')
        # response = s3.list_objects(Bucket='jay.bucket')
        # keys = [obj['Key'] for obj in response['Contents']]
        # return render_template('/Users/coredge/Desktop/demo/test.html', keys=keys)

        #return jsonify({'keys': keys})



#get_list_bucket()


# def list_image_on_url():
#     bucket = conn.get_bucket('chandu.bucket')
#     bucket.set_acl('public-read')
#
#
#     url = bucket.generate_url(expires_in=3600)  # Generate URL with 1-hour expiration
#     print(url)
#
# list_image_on_url()










#def get_list_bucket():
#     s3 = boto3.resource('s3')
#     bucket = s3.Bucket('jay.bucket')
#     keys = [obj.key for obj in bucket.objects.all()]
#
#     html = "<h1>S3 Bucket List</h1>"
#     html += "<ul>"
#     for key in keys:
#         html += f"<li>{key}</li>"
#     html += "</ul>"
#
#     return html
#
# if __name__ == '__main__':
#     get_list_bucket()




















#deleting an object
# def delete_obj():
#         bucket_obj = conn.get_bucket('jay.bucket')
#         bucket.delete_key('hello.txt')
#         print('deleted successfully')
# delete_obj()
# get_list_bucket()


#GENERATE OBJECT DOWNLOAD URLS (SIGNED AND UNSIGNED)

# def download_link_link():
#         bucket_obj = conn.get_bucket("jay.bucket")
#         key_obj = bucket_obj.get_key("img5.avif")
#         url = key_obj.generate_url(expires_in=0,query_auth= False, force_http = True,
#                  expires_in_absolute = 10)
#         print(url)
#
# download()








#print out bucket name
# for bucket in conn.get_all_buckets():
#         print(bucket.name)
# print("mani")






















# import os
# os.environ["CEPH_DEFAULT_REGION"] = "NONE"
# os.environ["CEPH_ACCESS_KEY_ID"] = "QI9ZHB30QVP4SMHB4UCH"
# os.environ["CEPH_SECRET_ACCESS_KEY"] = "h3jTc5rb67bZ1RnxIlDCqOhtB4iV6YcsOfwQgyXH"

#def fun(self):
# s3 = boto3.resource_(
#     # user_name = "ashok$ashok-test",
#     service_name ="s3",
#
#     host = "10.82.2.14:8080",
#     aws_access_key_id = "QI9ZHB30QVP4SMHB4UCH",
#     aws_secret_access_key="h3jTc5rb67bZ1RnxIlDCqOhtB4iV6YcsOfwQgyXH",
#
# )

# #print out bucket name
# for bucket in s3.buckets.all():
#     print(bucket.name)

# fun()

#upload file to s3 bucket
# s3.Bucket("test").upload_file(Filename="img1.avif", key="img1.avif")
# s3.Bucket("test").upload_file(Filename="img6.avif", key="img6.avif")
#
# for obj in s3.Bucket("test").objects.all():
#     print(obj)


#load csv file directly into python
# obj = s3.Bucket("test").Object("img1.avif").get()
# chandu = pd.read_csv(obj["Body"], index_col=0)
# type(chandu)


# obj = s3.Bucket("test").Object("img6.avif").get()
# chandu2 = pd.read_csv(obj["Body"], index_col=0)
# # type(chandu)
# chandu2.head()



#download file and read from dics
# s3.Bucket("test").download_file(key="img1.avif",Filename="img1.avif")
# pd.read_csv('img1.avif', index_col=0)


