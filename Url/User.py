import json

from flask import request

from app import app
from Module.User_Module import User_Module
from Module.Post_Module import Post_Module
from Module.Comment_Module import Comment_Module

user_module = User_Module()
post_module = Post_Module()
comment_module = Comment_Module()


@app.route('/login', methods=['GET'])
def login_get():
    text = "Enter Your Username And Password..."
    return json.dumps(text)


@app.route('/login', methods=['POST'])
def login_post():
    data = json.loads(request.data)
    password = data.get("password")
    username = data.get('username')
    res = user_module.login(password=password, username=username)
    res_dict = {
        "status": res
    }
    return json.dumps(res_dict)


@app.route('/users', methods=['GET'])
def get_users():
    users = user_module.get_all_users()
    userlist = []
    for user in users:
        userlist.append(
            {
                "name": user.name,
                "username": user.username,
                "id": user.id,
                "email": user.email
            }
        )
    return json.dumps(userlist)


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = user_module.get_user_by_id(user_id)
    if user is not None:
        userlist = []
        userlist.append(
            {
                "name": user.name,
                "username": user.username,
                "id": user.id,
                "email": user.email
            }
        )
        return json.dumps(userlist)
    else:
        return json.dumps("User Not Exist")


@app.route('/users', methods=['POST'])
def post_users():
    data = json.loads(request.data)
    name = data.get('name')
    password = data.get("password")
    username = data.get('username')
    email = data.get('email')
    user_module.create_user(name=name, password=password, username=username, email=email)
    return 'i'


@app.route('/users/<user_id>', methods=['PUT'])
def put_users(user_id):
    data = json.loads(request.data)
    username = data.get('username')
    password = data.get('password')
    name = data.get('name')
    email = data.get('email')
    res = user_module.update_user(username=username, password=password, name=name, email=email, user_id=user_id)
    return json.dumps(res)


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_users(user_id):
    data = json.loads(request.data)
    username = data.get('username')
    password = data.get('password')
    res = user_module.delete_user(username=username, password=password, user_id=user_id)
    return json.dumps(res)


@app.route('/posts', methods=['GET'])
def get_posts():
    return 'k'


@app.route('/posts', methods=['POST'])
def post_posts():  # create post
    data = json.loads(request.data)
    user_id = data.get('user_id')
    caption = data.get('caption')
    res = post_module.create_post(user_id=user_id, caption=caption)
    return res


@app.route('/posts/<post_id>', methods=['PUT'])
def put_posts(post_id):
    data = json.loads(request.data)
    caption = data.get('caption')
    result = post_module.edit_post(post_id=post_id, caption=caption)
    return json.dumps(result)


@app.route('/posts/<post_id>', methods=['DELETE'])
def delete_posts(post_id):
    result = post_module.delete_post(post_id=post_id)
    return json.dumps(result)


@app.route('/posts/explore', methods=['GET'])
def all_posts():
    res = post_module.get_all_posts()
    return json.dumps(res)


@app.route('/users/<user_id>/posts', methods=['GET'])
def user_posts(user_id):
    result = post_module.get_all_posts_from_id(user_id)
    return json.dumps(result)


@app.route('/posts/<post_id>/c', methods=['GET'])
def post_comments(post_id):
    res = comment_module.comments_from_post(post_id)
    return json.dumps(res)


@app.route('/posts/<post_id>/c', methods=['POST'])
def create_comment(post_id):
    data = json.loads(request.data)
    comment = data.get('comment')
    username = data.get('username')
    password = data.get('password')
    result = comment_module.write_comment(comment, username, password, post_id)
    return json.dumps(result)

@app.route('/posts/<post_id>/c', methods=['DELETE'])
def delete_comment(post_id):
    pass


@app.route('/posts/<post_id>/c', methods=['PUT'])
def edit_comment(post_id):
    pass
