# app.py
from flask import Flask
from models.user import db
from routes.user_routes import user_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)

with app.app_context():
    db.create_all()

app.register_blueprint(user_bp, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
