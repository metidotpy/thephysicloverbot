import pyromod
import asyncio
from pyrogram import Client, filters
from pyromod import listen
from pyrogram.types import *
from decouple import config
from threading import Thread
from database.queris import (
    user_management,
    admin_management,
    message_management,
    music_management,
    movie_management,
    book_management,
)
from keyboards import (
    MAIN_USER_KEYBOARD,
    MAIN_ADMIN_KEYBOARD,
)
from functions import (
    add_user,
    update_user,
    user_block_status,
    is_admin,
    is_blocked,
)
from messages import (
    message_admin_firstname,
    message_admin_fullname,
    message_with_firstname,
    message_with_fullname,
    send_post_to_admin,
)
from var import(
    BOT_TOKEN,
    API_ID,
    API_HASH,
    MUSIC_CHANNEL_ID,
    MOVIE_CHANNEL_ID,
    BOOK_CHANNEL_ID,
)
import random

LIST_OF_ADMINS = [admin.chat_id for admin in admin_management.select_admins()]

bot = Client(
    "stanleykubrickbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
cli = Client(
    'Stanley Kubrick',
    api_id=API_ID,
    api_hash=API_HASH
)

@cli.on_message(filters.channel)
async def send_message(client, message):
    chat_id = str(message.sender_chat.id)
    if chat_id == MUSIC_CHANNEL_ID:
        if message.audio:
            print(music_management.insert_music(message.id))
    elif chat_id == MOVIE_CHANNEL_ID:
        print(movie_management.insert_movie(message.id))
    elif chat_id == BOOK_CHANNEL_ID:
        print(book_management.insert_book(message.id))
@cli.on_deleted_messages(filters.channel)
async def deleted_messages(client, message):
    if type(message) == List:
        for m in message:
            chat_id = str(m.chat.id)
            if chat_id == MUSIC_CHANNEL_ID:
                music = music_management.select_music_message_id(m.id)
                print(music)
                if music:
                    print(music_management.delete_music(music.id))
            elif chat_id == MOVIE_CHANNEL_ID:
                movie = movie_management.select_movie_message_id(m.id)
                if movie:
                    print(movie_management.delete_movie(movie.id))
            elif chat_id == BOOK_CHANNEL_ID:
                book = book_management.select_book_message_id(m.id)
                if book:
                    print(book_management.delete_book(book.id))
    else:
        chat_id = str(message.chat.id)
        if chat_id == MUSIC_CHANNEL_ID:
            music = music_management.select_music_message_id(message.id)
            print(music)
            if music:
                print(music_management.delete_music(music.id))
        elif chat_id == MOVIE_CHANNEL_ID:
            movie = movie_management.select_movie_message_id(message.id)
            if movie:
                print(movie_management.delete_movie(movie.id))
        elif chat_id == BOOK_CHANNEL_ID:
                book = book_management.select_book_message_id(chat_id.id)
                if book:
                    print(book_management.delete_book(book.id))

@bot.on_message(filters.command(['start', ]))
async def start(client, message):
    chat_id = message.from_user.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    username = message.from_user.username
    admin_status = is_admin(str(chat_id), LIST_OF_ADMINS)
    
    user = user_management.select_user(chat_id)
    if not user:
        add_user(client, message)
    else:
        update_user(client, message)
    
    if last_name:
        if admin_status:
            text = message_admin_fullname(first_name, last_name)
            keyboard = MAIN_ADMIN_KEYBOARD
        else:
            text = message_with_fullname(first_name, last_name)
            keyboard = MAIN_USER_KEYBOARD
    else:
        if admin_status:
            text = message_admin_firstname(first_name)
            keyboard = MAIN_ADMIN_KEYBOARD
        else:
            text = message_with_firstname(first_name)
            keyboard = MAIN_USER_KEYBOARD
    
    await message.reply_text(text, reply_markup=keyboard)


@bot.on_message()
async def posts(client, message):
    try:
        chat_id = message.from_user.id
        first_name = message.from_user.first_name
        last_name = message.from_user.last_name
        username = message.from_user.username
        admin_status = is_admin(str(chat_id), LIST_OF_ADMINS)
        user = user_management.select_user(chat_id)
        if not user:
            add_user(client, message)
        else:
            update_user(client, message)
        
        user_blocked = is_blocked(chat_id)
        
        if user_blocked:
            await message.reply_text("شما توسط ادمین بلاک شدید.")
        else:
                print(message.text)
                if message.text == "معرفی موزیک 🎵":
                    musics = music_management.select_all_musics()
                    print(musics)
                    while True:
                        random_music = random.choice(musics)
                        try:
                            await bot.forward_messages(chat_id, MUSIC_CHANNEL_ID, random_music.message_id)
                            break
                        except Exception as e:
                            print(e)
                            continue
                    # try:
                    #     musics_id = [music.message_id for music in musics]
                    #     musics_channel = [music.id async for music in cli.get_chat_history(chat_id=MUSIC_CHANNEL_ID) if music.audio]
                    #     print(musics_channel)
                    #     for music in musics_channel:
                    #         if music not in musics_id:
                    #             print(music_management.insert_music(music))
                    # except:
                    #     pass
                    
                elif message.text == "معرفی فیلم 🎥":
                    movies = movie_management.select_all_movie()
                    while True:
                        random_movie = random.choice(movies)
                        try:
                            await bot.forward_messages(chat_id, MOVIE_CHANNEL_ID, random_movie.message_id)
                            break
                        except:
                            continue
                    # try:
                    #     movie_id = [movie.message_id for movie in movies]
                    #     movie_channel = [movie.id async for movie in cli.get_chat_history(chat_id=MOVIE_CHANNEL_ID)]
                    #     for movie in movie_channel:
                    #         if movie not in movie_id:
                    #             print(movie_management.insert_movie(movie))
                    # except:
                    #     pass

                
                elif message.text == 'معرفی کتاب 📕':
                    books = book_management.select_all_book()
                    while True:
                        random_book = random.choice(books)
                        try:
                            await bot.forward_messages(chat_id, BOOK_CHANNEL_ID, random_book.message_id)
                            break
                        except:
                            continue
                    # try:
                    #     book_id = [book.message_id for book in books]
                    #     book_channel = [book.id async for book in cli.get_chat_history(chat_id=BOOK_CHANNEL_ID)]
                    #     for book in book_channel:
                    #         if book not in book_id:
                    #             print(book_management.insert_book(book))
                    # except:
                    #     pass
                
                else:
                    message_obj = message_management.insert_message(user.id, chat_id, text=message.text)
                    text = send_post_to_admin(chat_id, message_obj[0].id)
                    await message.reply_text("پیام شما ارسال شد.", reply_markup=MAIN_USER_KEYBOARD)
                    for admin in LIST_OF_ADMINS:
                        await bot.send_message(admin, text[0], reply_markup=text[1])
                        await bot.forward_messages(admin, chat_id, message.id)
    except:
        pass



@bot.on_callback_query()
async def call_back(client, callback):
    data = callback.data
    chat_id = callback.from_user.id
    message_id = callback.message.id
    first_name = callback.from_user.first_name
    last_name = callback.from_user.last_name
    username = callback.from_user.username

    admin_status = is_admin(str(chat_id), LIST_OF_ADMINS)
    
    user = user_management.select_user(chat_id)
    if not user:
        add_user(client, callback)
    else:
        update_user(client, callback)
    
    user_blocked = is_blocked(chat_id)

    # BLOCK AND UNBLOCK SECTION -----------------------------------------------------------------
    if data.startswith("block_user_"):
        if admin_status:
            user_chat_id = data.split("_")[2]
            user_blocked = user_management.select_user(user_chat_id)
            user_block_status(user_blocked.chat_id, not user_blocked.is_blocked)
            if user_blocked.is_blocked:
                block = "blocked"
            else:
                block = "unblocked"
            await bot.send_message(chat_id, "You {} user with this chat id: {}".format(block, user_blocked.chat_id))
    # END OF BLOCK AND UNBLOCK SECTION -----------------------------------------------------------------

    # REPLY TO MESSAGE SECTION ----------------------------------------------------------------------------
    elif data.startswith("reply_message_"):
        if admin_status:
            reply_message_id = data.split("_")[2]
            message = message_management.select_message(reply_message_id)
            user_replied = user_management.select_user_id(message.user)
            answer = await bot.ask(chat_id, "**Send me your reply message: **")
            await bot.send_message(
                user_replied.chat_id,
"""
شما از ادمین یک پیام داریم:
{}
""".format(answer.text)
            )
            await answer.request.edit_text("*Your message send ✅.")
    # END OF REPLY TO MESSAGE SECTION ----------------------------------------------------------------------------


async def update_database():
    while True:
        try:
            #update musics database
            musics = music_management.select_all_musics()
            musics_id = [music.message_id for music in musics]
            musics_channel = [music.id async for music in cli.get_chat_history(chat_id=MUSIC_CHANNEL_ID) if music.audio]
            print(musics_channel)
            for music in musics_channel:
                if music not in musics_id:
                    print(music_management.insert_music(music))
            
            #update movies database
            movies = movie_management.select_all_movie()
            movie_id = [movie.message_id for movie in movies]
            movie_channel = [movie.id async for movie in cli.get_chat_history(chat_id=MOVIE_CHANNEL_ID)]
            for movie in movie_channel:
                if movie not in movie_id:
                    print(movie_management.insert_movie(movie))
            #update book database
            books = book_management.select_all_book()
            book_id = [book.message_id for book in books]
            book_channel = [book.id async for book in cli.get_chat_history(chat_id=BOOK_CHANNEL_ID)]
            for book in book_channel:
                if book not in book_id:
                    print(book_management.insert_book(book))
            
            print("I updated the database successfully and now let me rest for 30 min :)")
            await asyncio.sleep(1800)
        except Exception as e:
            print("update database: ", e)
            print("I sleep for 30 min with errors :(")
            await asyncio.sleep(1800)
            continue

if __name__ == "__main__":
    cli.start()
    bot.run()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(update_database())
    loop.close()
