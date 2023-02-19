from database.queris import (
    user_management,
)
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

def message_with_firstname(first_name):
    return """
سلام {} عزیز به ربات من خوش آمدید
شما الان میتوانید هرچیزی که دلت میخواد به مهدی بگی و این پیام به صورت ناشناس میمونه.

در ضمن یسری قابلیت های دیگه هم داریم که میتونی ازش استفاده کنی :)
""".format(first_name)

def message_with_fullname(first_name, last_name):
    return """
سلام {} {} عزیز به ربات من خوش آمدید
شما الان میتوانید هرچیزی که دلت میخواد به مهدی بگی و این پیام به صورت ناشناس میمونه.

در ضمن یسری قابلیت های دیگه هم داریم که میتونی ازش استفاده کنی :)
""".format(first_name, last_name)

def message_admin_firstname(first_name):
    return """
سلام {} عزیز به ربات من خوش آمدید
شما الان میتوانید هرچیزی که دلت میخواد به مهدی بگی و این پیام به صورت ناشناس میمونه.

در ضمن یسری قابلیت های دیگه هم داریم که میتونی ازش استفاده کنی :)


شما ادمین هستید.
""".format(first_name)

def message_admin_fullname(first_name, last_name):
    return """
سلام {} {} عزیز به ربات من خوش آمدید
شما الان میتوانید هرچیزی که دلت میخواد به مهدی بگی و این پیام به صورت ناشناس میمونه.

در ضمن یسری قابلیت های دیگه هم داریم که میتونی ازش استفاده کنی :)

شما ادمین هستید.
""".format(first_name, last_name)

def send_post_to_admin(chat_id, message_id):
    user = user_management.select_user(chat_id)
    block_and_reply_keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Block 🚫", callback_data="block_user_{}".format(chat_id)),
            InlineKeyboardButton("Reply 🔅", callback_data="reply_message_{}".format(message_id))
        ]
    
    ])
    return """
👇👇 Hello admin you got a message 👇👇
User chat ID => {}
User first name => {}
User last name => {}
User username => {}

Have fun <3
""".format(
    user.chat_id,
    user.first_name,
    user.last_name,
    user.username
), block_and_reply_keyboard
