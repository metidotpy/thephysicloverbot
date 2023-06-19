from pyrogram import Client
from database.queris import music_management, movie_management, book_management
from var import(
    BOT_TOKEN,
    API_ID,
    API_HASH,
    MUSIC_CHANNEL_ID,
    MOVIE_CHANNEL_ID,
    BOOK_CHANNEL_ID,
)
import asyncio

cli = Client(
    "Stanley Kubrick",
    api_id=API_ID,
    api_hash=API_HASH
)

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
    loop = asyncio.get_event_loop()
    loop.run_until_complete(update_database())
    loop.close()