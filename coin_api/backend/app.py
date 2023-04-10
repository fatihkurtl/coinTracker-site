from flask import Flask, jsonify, request, current_app, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Users, FavoriteList, Comments, Admin, Post, Contact, Base, engine
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import jwt
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'images'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png', 'gif'}


def allowed_file(filename):
    """Yalnızca izin verilen dosya uzantılarına sahip dosyaların yüklenmesini sağlar"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


engine = create_engine('mysql://root:2410@localhost/coinTracker')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

@app.route('/register', methods = ['POST'])
def register():
    data = request.get_json()
    
    if session.query(Users).filter((Users.email == data['email']) | (Users.userName == data['userName'])).first():
        return jsonify({'msg': 'This email or username is already registered.'}), 203
    
    if data['email'] == 'kurtf061@gmail.com':
        hashed_password = generate_password_hash(data['password'], method='sha256')
        add_admin = Admin(username = data['userName'], password = hashed_password)
        session.add(add_admin)
        session.commit()
        return jsonify({'msg': 'Registration Successful', 'admin': True}), 201
    
    hashed_password = generate_password_hash(data['password'], method='sha256')
    new_user = Users(fullName = data['fullName'], email = data['email'], userName = data['userName'], password = hashed_password)
    session.add(new_user)
    session.commit()
    return jsonify({'msg': 'Registration Successful', 'info': True}), 201

@app.route('/login', methods = ['POST'])
def login():
    data = request.get_json()
    user = session.query(Users).filter(Users.email == data['email']).first()
    
    if user and check_password_hash(user.password, data['password']):
        token = jwt.encode({"some": "payload"}, "secret", algorithm="HS256")
        if data['email'] == 'kurtf061@gmail.com':
            return jsonify({'info': True, 'msg': 'Login successful', 'token': token, 'admin': True}), 202
        return jsonify({'info': True, 'msg': 'Login successful', 'token': token}), 202
    
    if not user:
        return jsonify({'msg': 'User not found', 'info': False}), 204
    
    return jsonify({'msg': 'Your password is wrong'}), 203

# only admin share post
@app.route('/share_post/<admin>', methods = ['POST'])
def savePost(admin):
    print(admin)
    file = request.files['file']
    title = request.form.get('title')
    content = request.form.get('content')
    print(title, content)
    print(file, 'file burada')
    if file and allowed_file(file.filename):
        if admin:
            # Dosya adını güvenli hale getirir ve dosyayı kaydeder
            filename = secure_filename(file.filename)
        
            # Dizini oluştur veya varsa geç
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        
            # Dosyayı kaydet
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
            new_post = Post(title = title, content = content, image = filename)
            session.add(new_post)
            session.commit()
            
            return jsonify({'message': 'File successfully uploaded', 'info': True}), 201
    return jsonify({'msg': 'Unauthorized'}), 401

@app.route('/get_post/<admin>', methods = ['GET', 'POST'])
def getPost(admin):
    if request.method == 'GET':
        posts = session.query(Post).all()
        post_list = []
        for post in posts:
            post_data = {
                'id': post.id,
                'title': post.title,
                'content': post.content,
                'image': 'http://localhost:3000/images/' + post.image,
                'created_at': post.created_at
            }
            post_list.append(post_data)
        return jsonify({'posts': post_list})
    return jsonify({'msg': 'Method not allowed.'}), 405

@app.route('/delete_post/<id>', methods = ['POST', 'DELETE'])
def deletePost(id):
    if id:
        post = session.query(Post).filter(Post.id == id).first()
        if post:
            session.delete(post)
            session.commit()
            return jsonify({'msg': 'Post deleted successfully.'}), 201
        return jsonify({'msg': 'Post not found.'}), 204
    return jsonify({'msg': 'Unauthorized'}), 401

@app.route('/images/<path:path>') # images klasörünün altındaki dosyaları statik olarak sunar  
def send_js(path):
    return send_from_directory('images', path)

@app.route('/post_detail/<id>', methods = ['GET'])
def get_post(id):
    post = session.query(Post).filter(Post.id == id).first()
    if post:
        post_data = {
            'id': post.id,
            'title': post.title,
            'content': post.content,
            'image': 'http://localhost:3000/images/' + post.image,
            'created_at': post.created_at
        }
        return jsonify({'post': post_data})
    return jsonify({'msg': 'Post not found.'}), 204

   
@app.route('/get_comments/<id>', methods = ['GET', 'POST'])
def getPostComment(id):
    comments = session.query(Comments).filter(Comments.post_id == id).all()
    comment_list = []
    for comment in comments:
        comment_data = {
            'id': comment.id,
            'content': comment.content,
            'user_id': comment.user_id,
            'post_id': comment.post_id,
            'created_at': comment.created_at,
        }
        user = session.query(Users).filter(Users.id == comment_data['user_id']).all()
        print(user, 'user burada')
        for i in user:
            user_data = {
                'id': i.id,
                'userName': i.userName,
                'email': i.email,
            }
            comment_data['user'] = user_data
        comment_list.append(comment_data)
    return jsonify({'comments': comment_list})


@app.route('/save_comment/<id>/<user>', methods = ['POST'])
def saveComment(id, user):
    print(user, 'user burada save comment')
    print(id, 'id burada save comment')
    data = request.get_json()
    print(data, 'request burada save comment')
    user = session.query(Users).filter(Users.email == user).first()
    if user:
        add_comment = Comments(content=data['comment'], user_id=user.id, post_id=id)
        session.add(add_comment)
        session.commit()
        return jsonify({'msg': 'Comment saved successfully.'}), 201
    else:
        return jsonify({'msg': 'User not found.'}), 404
    
@app.route('/delete_comment/<id>', methods = ['POST', 'DELETE'])
def deleteComment(id):
    comment = session.query(Comments).filter(Comments.id == id).first()
    if comment:
        session.delete(comment)
        session.commit()
        return jsonify({'msg': 'Comment deleted successfully.'}), 201
    return jsonify({'msg': 'Comment not found.'}), 204    


@app.route('/contact', methods = ['POST'])
def contact():
    data = request.get_json()
    if data['user']:
        user = session.query(Users).filter(Users.email == data['user']).first()
        add_member_contact = Contact(fullName=data['name'], email=data['email'], phone=data['phone'], message=data['message'], user_id=user.id)
        session.add(add_member_contact)
        session.commit()
        return jsonify({'msg': 'Message sent successfully.'}), 201
        
    add_contact = Contact(fullName=data['name'], email=data['email'], phone=data['phone'], message=data['message'])
    session.add(add_contact)
    session.commit()
    return jsonify({'msg': 'Message sent successfully.'}), 201

@app.route('/forgot_password', methods = ['POST'])
def forgotPassword():
    data = request.get_json()
    user = session.query(Users).filter(Users.email == data['email']).first()
    if user:
        hashed_password = generate_password_hash(data['password'], method='sha256')
        session.query(Users).filter(Users.email == data['email']).update({Users.password: hashed_password})
        session.commit()
        return jsonify({'msg': 'Email sent successfully.'}), 201
    return jsonify({'msg': 'User not found.'}), 404

@app.route('/get_users/<admin>', methods = ['GET', 'POST'])
def getUsers(admin):
    users = session.query(Users).all()
    user_list = []
    if admin:
        for user in users:
            user_data = {
                'id': user.id,
                'fullName': user.fullName,
                'userName': user.userName,
                'email': user.email,
                # 'password': user.password,
                'registerTime': user.registerTime,
            }
            user_list.append(user_data)
        return jsonify({'users': user_list}), 201
    return jsonify({'msg': 'Admin not found.'}), 404

@app.route('/delete_user/<id>', methods = ['POST', 'DELETE'])
def deleteUser(id):
    user = session.query(Users).filter(Users.id == id).first()
    if user:
        session.delete(user)
        session.commit()
        return jsonify({'msg': 'User deleted successfully.'}), 201
    return jsonify({'msg': 'User not found.'}), 204

if __name__  == '__main__':
    app.run(debug=True, port=3000)
