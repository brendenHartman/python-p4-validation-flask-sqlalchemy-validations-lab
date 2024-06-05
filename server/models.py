from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators 
    @validates('name')
    def name_val(self,key,name):
        existing_name = Author.query.filter_by(name=name).first()
        if existing_name:
            raise ValueError('Author name must be unique')
        if name == '':
            raise ValueError('Author must have name')
        return name
    
    @validates('phone_number')
    def phone_number_val(self,key,phone_number):
        if len(phone_number) != 10:
            raise ValueError('Phone number must be 10 in length')
        if not phone_number.isdigit():
            raise ValueError('')
        return phone_number

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Add validators  
    @validates('content')
    def content_val(self,key,content):
        if len(content) < 250:
            raise ValueError('')
        return content
    @validates('summary')
    def summary_val(self,key,summary):
        if len(summary) > 250:
            raise ValueError('')
        return summary
    @validates('category')
    def category_val(self,key,category):
        if category != 'Non-Fiction' and category != 'Fiction':
            raise ValueError('')
        return category
    @validates('title')
    def title_val(self,key,title):
        if "Won't Believe" not in title and "Secret" not in title and "Top" not in title and "Guess" not in title:
            raise ValueError('')
        return title
    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
