#####   CREATE A NEW BUCKET ######
import boto3
import logging
import json
import chalicelib.cloud_util as util

# define credentials
history = 'collection_history.json'
users = 'collection_users.json'

region = "us-east-1"
bucket = "contentcen301242732.aws.ai"




# Configure logging
logging.basicConfig(level=logging.ERROR)
def read_users():
    try:
        
        client = boto3.client('s3', region_name=region)
        # Read the file content from S3
        obj = client.get_object(Bucket=bucket, Key=users)
        jstr = obj['Body'].read().decode('utf-8')
        data = json.loads(jstr)
        return data
    except Exception as e:
        print(f'error: {str(e)}')
        return []

def write_users(data):
    client = boto3.client('s3', region_name=region)
    print(f'write_users :> {data}')
    jstr = json.dumps(data)
    try:
        client.put_object(
            Body=jstr.encode('utf-8'),
            Bucket=bucket,
            Key=users
        )
        print(f'CP := write_users')
    except Exception as e:
        print(f'error: {str(e)}')

# if email not exists, save it and return the user profile, otherwise return user profile
def register_user(email):
    is_exist = False
    user_dict = read_users()
    print(f'regiser_user :> {user_dict}')
    # check email exists, return user profile
    for usr in user_dict:
        if usr['userid'] == email:
            return usr

    # if email not exists, save to s3 and return the user profile
    usr = {'userid':email, 'tier':1}
    user_dict.append(usr)
    write_users(user_dict)
    return usr

def upgrade_tier(email):
    is_upgrade = False
    show_tier = 0
    data = read_users()
    for user in data:
        if user['userid'] == email:
            if user['tier'] < util.MAX_TIER:
                user['tier'] += 1
                show_tier = user['tier']
                is_upgrade = True
    if is_upgrade:
        write_users(data)
        return {'message':f'User: {email} tier upgraded to {show_tier}!','tier':show_tier}
    else:
        return {'message':f'User: {email} tier reaches MAX and cannot upgrade!'}

def reset_tier(email):
    data = read_users()
    show_tier = 1
    for user in data:
        if user['userid'] == email:
            user['tier'] = show_tier
    write_users(data)
    return {'message':f'User: {email} tier reset to {show_tier}!','tier':show_tier}