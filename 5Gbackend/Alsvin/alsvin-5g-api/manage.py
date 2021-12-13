import click
from flask.cli import with_appcontext


@click.command("init")
@with_appcontext
def init():
    """Create a new admin user"""
    from alsvin-5g-api.extensions import db
    from alsvin-5g-api.models import User

    click.echo("create user")
    user = User(username="admin", email="vlad.duda@outlook.com", password="admin", active=True)
    db.session.add(user)
    db.session.commit()
    click.echo("created user admin")
