from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# ---------------- USER ----------------
class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)

    # Login
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

    # Perfil
    username = db.Column(db.String(120), unique=True, nullable=False)
    firstname = db.Column(db.String(120))
    lastname = db.Column(db.String(120))
    is_active = db.Column(db.Boolean(), default=True)

    # Relaciones
    posts = db.relationship("Post", backref="author", lazy=True)
    comments = db.relationship("Comment", backref="author", lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "username": self.username
        }


# ---------------- POST ----------------
class Post(db.Model):
    __tablename__ = "post"

    id = db.Column(db.Integer, primary_key=True)
    caption = db.Column(db.String(500))

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    media = db.relationship("Media", backref="post", lazy=True)
    comments = db.relationship("Comment", backref="post", lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "caption": self.caption,
            "user_id": self.user_id
        }


# ---------------- MEDIA ----------------
class Media(db.Model):
    __tablename__ = "media"

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))  # image, video, reel, etc
    url = db.Column(db.String(500))

    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))

    def serialize(self):
        return {
            "id": self.id,
            "type": self.type,
            "url": self.url,
            "post_id": self.post_id
        }


# ---------------- COMMENT ----------------
class Comment(db.Model):
    __tablename__ = "comment"

    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String(500))

    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))

    def serialize(self):
        return {
            "id": self.id,
            "comment_text": self.comment_text,
            "author_id": self.author_id,
            "post_id": self.post_id
        }


# ---------------- FOLLOWERS ----------------
class Follower(db.Model):
    __tablename__ = "follower"

    id = db.Column(db.Integer, primary_key=True)

    user_from_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user_to_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def serialize(self):
        return {
            "id": self.id,
            "user_from_id": self.user_from_id,
            "user_to_id": self.user_to_id
        }