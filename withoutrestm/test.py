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
# get_resource()

# def get_all():
#     resp=requests.get(BASE_URL+ENDPOINT)
#     print(resp.status_code)
#     print(resp.json())

#get_all()
# import json
# def create_resource():
#     new_emp={
#     'eno':500,
#     'ename':'Shyam',
#     'esal':8000,
#     'eaddr':'Delhi',
#     }
#     resp=requests.post(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# create_resource()

# def update_resource(id):
#     new_emp={
#     'id':id,
#     'esal':99999,
#     'eaddr':'Hilauli',
#     }
#     resp=requests.put(BASE_URL+ENDPOINT,data=json.dumps(new_emp))
#     print(resp.status_code)
#     print(resp.json())
# update_resource(5)

def delete_resource(id):
    data={
    'id':id,
    }
    resp=requests.delete(BASE_URL+ENDPOINT,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())
delete_resource(5)
