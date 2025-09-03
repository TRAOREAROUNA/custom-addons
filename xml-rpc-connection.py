import xmlrpc.client

url = 'http://localhost:8069'
username ='admin'
password ='odoo'
db = 'ero'

common =xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')

user_uid = common.authenticate(db, username,password,{})
'xmlrpc/2/object' 'execute_kw'
'db,uid,password,model_name,methode_name,[],{}'

models=xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# search function
property_ids=models.execute_kw(db,user_uid,password,'estate.property','search',[[]],{'offset': 5,'limit':1})
print("search function ==> ", property_ids)

# search count
count_property_ids=models.execute_kw(db,user_uid,password,'estate.property','search_count',[[]])
print("count function ==> ", count_property_ids)


# read function
read_property_ids=models.execute_kw(db,user_uid,password,'estate.property','read',[property_ids],{'fields': ['name']})
print("read function ==> ", read_property_ids)


# search and read function
search_read_property_ids=models.execute_kw(db,user_uid,password,'estate.property','search_read',[[]],{'fields': ['name']})
print("search_read function ==> ", search_read_property_ids)

# # create function
# create_property_id=models.execute_kw(db,user_uid,password,'estate.property','create',[{'name': 'property from RPC','sales_id': 2}])
# print("create property ==> ", create_property_id)

# write function
# write_property_id=models.execute_kw(db,user_uid,password,'estate.property','write',[[11],{'name': 'property from RPC updated'}])
# read_name_get=models.execute_kw(db,user_uid,password,'estate.property','name_get',[[11]])
# print("update property ==> ", read_name_get)

# # unlink function
# unlink_property_id=models.execute_kw(db,user_uid,password,'estate.property','unlink',[[11]])
# print("unlink property ==> ", unlink_property_id)