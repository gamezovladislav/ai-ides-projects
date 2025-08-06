from flask import Blueprint, jsonify

from models import User

user_bp = Blueprint('user', __name__)

@user_bp.route('/<int:user_id>')
def get_user(user_id):
    user = User.query.get(user_id)
    return jsonify(user.to_dict())
