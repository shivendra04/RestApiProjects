import requests,json
BASE_URL='http://127.0.0.1:8000/'
ENDPOINT='api/'
# def get_resource(id=None):
#     data={}
#     if id is not None:
#         data={
#         'id':id,
#         }
#     resp=requests.get(BASE_URL+ENDPOINT,data=json.dumps(data))
#     print(resp.status_code)
#     print(resp.json())
# get_resource(10)

# def get_all():
#     resp=requests.get(BASE_URL+ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())

#get_all()
import json
# def create_resource():
#     new_emp={
#     'name':'Dhoni',
#     'rollno':106,
#     'marks':32,
#     'gf':'Deepika',
#     'bf':'Yuvraj',
#     }
#     resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()

# def update_resource(id):
#     new_stu={
#     'id':id,
#     'marks':10,
#     'gf':'nothing',
#     }
#     resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_stu))
#     print(resp.status_code)
#     print(resp.json())
# update_resource(1)

def delete_resource(id):
    data={
    'id':id,
    }
    resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
delete_resource(7)
