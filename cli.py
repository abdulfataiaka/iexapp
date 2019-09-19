import click
from config.db import DB
from flask.cli import with_appcontext

@click.command('db:setup')
@with_appcontext
def dbsetup():
    click.echo('[*] Setting up database and tables')
    DB.setup()
    click.echo('[*] Database setup complete')
