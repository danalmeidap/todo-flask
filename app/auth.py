import click
from app.database import mongo
from werkzeug.security import check_password_hash, generate_password_hash
from flask_simplelogin import SimpleLogin


def create_user(**data):
    """Creates user with encrypted password"""
    
    if "username" not in data or "password" not in data:
        raise ValueError("User name and password are required")
    
    data["password"] = generate_password_hash(
        data.pop("password"), method="pbkdf2:sha256"
    )
    
    mongo.db.users.insert_one(data)
    return data


def validate_login(data):
    if "username" not in data or "password" not in data:
        raise ValueError("User name and password are required")
    
    db_user = mongo.db.users.find_one({"username": data["username"]})

    return db_user and check_password_hash(db_user['password'], data['password'])


def configure(app):
    SimpleLogin(app, login_checker=validate_login)

    @app.cli.command()
    @click.argument("username")
    @click.password_option()
    def add_user(username, password):
        user = create_user(username= username, password= password)
        click.echo("User created")









        