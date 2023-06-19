from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup
)

MAIN_USER_KEYBOARD = ReplyKeyboardMarkup(
    keyboard= [
        [
            'معرفی موزیک 🎵',
            'معرفی فیلم 🎥',
            'معرفی کتاب 📕'
        ],
    ],
    resize_keyboard=True
)

MAIN_ADMIN_KEYBOARD = ReplyKeyboardMarkup(
    keyboard= [
        ['معرفی موزیک 🎵','معرفی فیلم 🎥','معرفی کتاب 📕'],
        ['لیست کاربر ها 👤', "لیست ادمین ها 👤", "لیست پیام ها 💬"],
    ],
    resize_keyboard=True
)