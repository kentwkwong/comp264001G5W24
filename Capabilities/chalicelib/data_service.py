import json
from datetime import datetime

def load_users():
    users = []
    with open('collection_users.json','r') as json_file:
        users = json.load(json_file)
    return users

def save_users(data):
    with open("collection_users.json", "w") as json_file:
        json.dump(data, json_file, indent=2)

def login(userid, password):
    data = load_users()
    for user in data:
        if user['userid'] == userid and user['password'] == password:
            return 1
    return 0

def upgrade_tier(userid):
    MAX_TIER = 3
    is_upgrade = False
    data = load_users()
    for user in data:
        if user['userid'] == userid:
            if user['tier'] < MAX_TIER:
                user['tier'] += 1
                is_upgrade = True
    if is_upgrade:
        save_users(data)
        return f'User: {userid} tier upgraded!'
    else:
        return f'Cannot upgrade user: {userid}'


def load_history():
    history = []
    with open('collection_history.json','r') as json_file:
        history = json.load(json_file)
    return history

def save_history(data):
    with open("collection_history.json", "w") as json_file:
        json.dump(data, json_file, indent=2)

def get_history(userid):
    data = load_history()
    filtered_data = [user for user in data if user['userid'] == userid]
    return filtered_data

# def check_url_search_existed(userid, url):
#     data = load_history()
#     for user in get_history(userid):
#         for detail in user['details']:
#             if detail['url'] == url:
#                 return True
#     return False


def save_sentiment(userid, stock, articles):
    data = []
    data = load_history()
    print(type(data))
    current = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    history = {
        'userid':userid, 
        'createtime':current,
        'stockcode':stock,
        'details':articles
    }
    data.append(history)
    save_history(data)
