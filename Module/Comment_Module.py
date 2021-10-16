from app import db
from data.User import Users
from data.post import Posts
from data.comment import Comments
from Module.Post_Module import Post_Module
from Module.User_Module import User_Module

user_module = User_Module()
post_module = Post_Module()


# texts


class Comment_Module:
    def __init__(self):
        self.User_Module = Users()
        self.Post_Module = Posts()

    def comments_from_post(self, post_id):
        if post_id:
            try:
                comments = Comments.query.filter(Comments.comment_for_post == post_id).all()
                comment_list = []
                for i in comments:
                    comment = i.comment
                    user = Users.query.filter(Users.id == i.comment_from_user).first()
                    user_id = user.id
                    username = user.username or user.name
                    text = f"""
                    [{user_id}] {username} / {comment}
                    """
                    comment_list.append(text)
                final_text = "\n".join(comment_list)
                return final_text
            except:
                db.session.rollback()
                return False

    def write_comment(self, comment, username, password, post_id):
        user = Users.query.filter(Users.username == username).first()
        post = Posts.query.filter(Posts.post_id == post_id).first()
        if user and post:
            encoded_password = password.encode('utf-8')
            hashed_password = user.password
            res = user_module.check_password(plain_text_password=encoded_password, hashed_password=hashed_password)
            if res is True:
                try:
                    check_post = Posts.query.filter(Posts.post_id == post_id)
                    new_comment = Comments(
                        comment=comment,
                        comment_for_post=post_id,
                        comment_from_user=user.id
                    )
                    db.session.add(new_comment)
                    db.session.commit()
                    setattr(user, "comments", +1)  # add comment to user
                    db.session.commit()
                    setattr(post, "comments", +1)  # add comment to post
                    db.session.commit()
                    return res
                except:
                    db.session.rollback()

    # we can use flask-login for save data and remember user
    def edit_comment(self):
        pass

    def all_comment_from_user(self):
        pass

    def delete_comment(self):
        pass
