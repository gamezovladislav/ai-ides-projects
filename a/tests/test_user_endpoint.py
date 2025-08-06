import pytest

from app import app
from models.user import db, User


@pytest.fixture
def client(tmp_path, monkeypatch):
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{tmp_path / 'test.db'}"
    with app.app_context():
        db.create_all()
        db.session.add(User(id=1, name="Alice"))
        db.session.commit()
    return app.test_client()

def test_get_user(client):
    resp = client.get('/users/1')
    assert resp.status_code == 200
    assert resp.json == {"id":1, "name":"Alice"}
