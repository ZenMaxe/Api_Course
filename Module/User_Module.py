import bcrypt
import json

from sqlalchemy import exc  # or from sqlalchemy.exc import IntegrityError

from app import db
from data.User import Users


class User_Module:
    def __init__(self):
        self.User_Module = Users()

    def login(self, username, password):
        user = Users.query.filter(Users.username == username).first()
        if user:
            encoded_password = password.encode('utf-8')
            hashed_password = user.password
            res = self.check_password(encoded_password, hashed_password)
            return res

        return False

    def create_user(self, name, username, password, email):
        hashed_password = self.get_hashed_password(password.encode("utf8"))
        new_user = Users(
            name=name,
            username=username,
            password=hashed_password,
            email=email,
            comments=0
        )
        db.session.add(new_user)
        db.session.commit()
        pass

    def get_all_users(self):
        all_users = Users.query.all()
        return all_users

    def get_user_by_id(self, user_id):
        user = Users.query.get(user_id)
        return user

    def update_user(self, username, password, name, email, user_id):
        user = Users.query.filter(Users.id == user_id).first()
        if user:
            try:
                encoded_password = password.encode('utf-8')
                user.password = self.get_hashed_password(encoded_password)
                user.name = name
                user.username = username
                user.email = email
                db.session.commit()

                text = "Information Updated!"
                return text
            except exc.IntegrityError:
                db.session.rollback()  # rollback data if changed
                text = "Please Send All Data , You Need Send "
                return text
        else:
            text = "User Not Found"
            return text

    def delete_user(self, username, password, user_id):
        check_id = Users.query.filter(Users.id == user_id).first()
        if check_id:
            user = Users.query.filter(check_id.username == username).first()
            if user:
                try:
                    hashed_password = user.password
                    encoded_password = password.encode('utf-8')
                    res = self.check_password(encoded_password, hashed_password)
                    if res is True:
                        data = Users.query.filter(user.username == username).delete()
                        db.session.commit()
                        text = "User Deleted"
                        return text
                    else:
                        text = "Wrong Password"
                        return text
                except:
                    db.session.rollback()

    def get_hashed_password(self, plain_text_password):
        # Hash a password for the first time
        #   (Using bcrypt, the salt is saved into the hash itself)
        return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

    def check_password(self, plain_text_password, hashed_password):
        # Check hashed password. Using bcrypt, the salt is saved into the hash itself
        return bcrypt.checkpw(plain_text_password, hashed_password)
