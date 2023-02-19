from database.queris import (
    user_management,
    admin_management,
    message_management,
)


def check_user_information(first_name=None, last_name=None, username=None) -> dict:
    user_info = {
        'first_name': first_name,
        'last_name': last_name,
        'username': username,
    }
    
    if not first_name:
        user_info['first_name'] = "❌"
        
    if not last_name:
        user_info['last_name'] = "❌"
        
    if not username:
        user_info['username'] = "❌"
    
    return user_info

def user_block_status(chat_id, status):
    user_management.update_block(chat_id, bool(status))

def add_user(client, message):
    chat_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    
    if not user_management.select_user(chat_id):
        user_info = check_user_information(first_name, last_name, username)
        user_management.insert_user(chat_id, user_info['first_name'], user_info['last_name'], user_info['username'])
        return True

def update_user(client, message):
    chat_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username

    user = user_management.select_user(chat_id)
    if user:
        user_info = check_user_information(first_name, last_name, username)
        user_management.update_user(chat_id, user_info['first_name'], user_info['last_name'], user_info['username'])

def is_admin(chat_id, admin_list):
    if chat_id in admin_list:
        return True
    return False

def is_blocked(chat_id):
    user = user_management.select_user(chat_id)
    if user.is_blocked:
        return True
    return False