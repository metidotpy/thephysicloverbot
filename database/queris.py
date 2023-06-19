from .tables import engine, Session, Base, AdminList, User, Message, Music, Movie, Book
# Admin Session and Management
class AdminManagement():
    def select_admins(self):
        return Session.query(AdminList).all()
    
    def select_admin(self, chat_id):
        return Session.query(AdminList).filter_by(chat_id=chat_id).first()
    
    def insert_admin(self, chat_id):
        try:
            admin = AdminList(chat_id=chat_id)
            Session.add(admin)
            Session.commit()
            return admin, bool(admin)
        except:
            return False
    
    def delete_admin(self, chat_id):
        try:
            Session.query(AdminList).filter_by(chat_id=chat_id).delete()
            Session.commit()
            return True
        except:
            return False

# User Session and Management
class UserManagement():
    def select_users(self):
        return Session.query(User).all()
    
    def select_user(self, chat_id):
        return Session.query(User).filter_by(chat_id=chat_id).first()
    
    def select_user_id(self, id):
        return Session.query(User).filter_by(id=id).first()
    
    def insert_user(self, chat_id, first_name=None, last_name=None, username=None):
        try:
            user = User(chat_id=chat_id, first_name=first_name, last_name=last_name, username=username)
            Session.add(user)
            Session.commit()
            return user, bool(user)
        except:
            return False
    
    def update_user(self, chat_id, first_name=None, last_name=None, username=None):
        try:
            user = Session.query(User)\
                .filter_by(chat_id=chat_id)\
                .update({
                "first_name": first_name,
                "last_name": last_name,
                "username": username
            })
            Session.commit()
            return True
        except:
            return False
    
    def update_block(self, chat_id, block_status):
        try:
            Session.query(User)\
                .filter_by(chat_id=chat_id)\
                .update({
                    'is_blocked': block_status,
                })
            Session.commit()
            return True
        except:
            return False

# Message Session and Management
class MessageManagement():
    def select_messages(self):
        return Session.query(Message).all()
    
    def select_user_messages(self, chat_id):
        user = Session.query(User).filter_by(chat_id=chat_id).first()
        return user.messages
    
    def select_message(self, id):
        return Session.query(Message).filter_by(id=id).first()
    
    def insert_message(self, user_id, user_chat_id, text):
        try:
            message = Message(user=user_id, user_chat_id=user_chat_id, text=text)
            Session.add(message)
            Session.commit()
            return message, True
        except:
            return False

    def delete(self, id):
            try:
                Session.query(Message).filter_by(id=id).delete()
                Session.commit()
                return True
            except:
                return False

class MusicManagement():
    def select_all_musics(self):
        return Session.query(Music).all()
    
    def select_music_message_id(self, message_id):
        return Session.query(Music).filter_by(message_id=message_id).first()
    
    def select_music(self, id):
        return Session.query(Music).filter_by(id=id).first()
    
    def insert_music(self, message_id):
        try:
            music = Music(message_id=message_id)
            Session.add(music)
            Session.commit()
            return music, True
        
        except:
            return False
    def delete_music(self, id):
        try:
            Session.query(Music).filter_by(id=id).delete()
            Session.commit()
            return True
        except:
            return False

class MovieManagement():
    def select_all_movie(self):
        return Session.query(Movie).all()
    
    def select_movie_message_id(self, message_id):
        return Session.query(Movie).filter_by(message_id=message_id).first()
    
    def select_movie(self, message_id):
        return Session.query(Movie).filter_by(message_id=message_id).first()
    
    def insert_movie(self, message_id):
        try:
            movie = Movie(message_id=message_id)
            Session.add(movie)
            Session.commit()
            return movie, True
        
        except:
            return False
    def delete_movie(self, id):
        try:
            Session.query(Movie).filter_by(id=id).delete()
            Session.commit()
            return True
        except:
            return False


class BookManagement():
    def select_all_book(self):
        return Session.query(Book).all()
    
    def select_book_message_id(self, message_id):
        return Session.query(Book).filter_by(message_id=message_id).first()
    
    def select_book(self, message_id):
        return Session.query(Book).filter_by(message_id=message_id).first()
    
    def insert_book(self, message_id):
        try:
            book = Book(message_id=message_id)
            Session.add(book)
            Session.commit()
            return book, True
        
        except:
            return False
    def delete_book(self, id):
        try:
            Session.query(Book).filter_by(id=id).delete()
            Session.commit()
            return True
        except:
            return False

admin_management = AdminManagement()
user_management = UserManagement()
message_management = MessageManagement()
music_management = MusicManagement()
movie_management = MovieManagement()
book_management = BookManagement()