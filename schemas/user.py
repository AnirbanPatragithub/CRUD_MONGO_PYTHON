
def userEntity(item) -> dict:
    print(item)
    return {
        'id':str(item['_id']),
        'email':item['email'],
        'location':item['location'],
        'clock_in':item.get('clock_in','NA')
        }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

def itemEntity(item) -> dict:
    # print(item)
    return {
        'id':str(item['_id']),
        'name':str(item['name']),
        'email':item['email'],
        'item_name':item['item_name'],
        'quantity':item.get('quantity','NA'),
        'expiry_date':item.get('expiry_date','NA'),
        'insert_date' : item.get('insert_date','NA')
        }

def itemsEntity(entity) -> list:
    return [itemEntity(item) for item in entity]