from app import db
from data.post import Posts
from data.User import Users


class Post_Module:
    def __init__(self):
        self.Post_Module = Posts()
        self.User_Module = Users()

    def create_post(self, caption, user_id):
        user = Users.query.filter(Users.id == user_id).first()
        if user:
            new_post = Posts(
                from_user=user.id,
                caption=caption,
                name=user.name or user.username,
                comments =0
            )
            db.session.add(new_post)
            db.session.commit()
            text = "Post Created Successfully"
            return text
        else:
            text = "Please Post Valid User ID"
            return text

    def edit_post(self, post_id, caption):
        # No Security Handlers For Demo
        post = Posts.query.filter(Posts.post_id == post_id).first()
        if post:
            try:
                post.caption = caption
                db.session.commit()
                text = "successfully changed"
                return text
            except:
                db.session.rollback()

    def delete_post(self, post_id):
        # check_user = Users.query.get(user_id)
        # if user:
        #   check_password = self.check_password(encoded_password, hashed_password)
        #   if check_password is True:
        try:
            find_post = Posts.query.get(post_id)
            db.session.delete(find_post)
            db.session.commit()
            text = "Post Deleted!"
            return text
        except:
            db.session.rollback()
            text = "Wrong Post ID!"
            return text

    def get_all_posts(self):
        posts = []
        all_posts = Posts.query.all()
        posts_count = db.session.query(Posts).count()
        for i in all_posts:
            text = (f'''
            [{i.from_user}]-{i.name} in {i.post_id}:|| {i.caption}
            ''')
            posts.append(text)
        final_text = (f"[Posts = {posts_count}]" + "\n".join(posts))
        return final_text

    def get_all_posts_from_id(self, user_id):
        posts_from_id = []
        try:
            check_user = Users.query.get(user_id) # User is exist or no?
            check_posts = Posts.query.filter(Posts.from_user == user_id).all()
            if check_posts:
                for i in check_posts:
                    text = i.caption
                    posts_from_id.append(text)
                final_text = "".join(posts_from_id)
                return final_text
        except:
            text = "Wrong..."
            return text

    def likes_from_post(self):
        pass

    def comments_from_post(self):
        pass

    def like_a_post(self):
        pass

    def write_comment(self):
        pass

    def followers(self):
        pass

    def follow_user(self):
        pass
