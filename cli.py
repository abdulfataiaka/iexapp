import click
from config.db import db
from flask.cli import with_appcontext
from app.seeders.stocks_seeder import StocksSeeder

@click.command('db:setup')
@click.option('--seed', default=False, is_flag=True)
@with_appcontext
def dbsetup(seed):
    click.echo('[*] Creating database and tables')
    db.drop_all()
    db.create_all()

    if seed:
        click.echo('[*] Seeding default database records')
        StocksSeeder.run()

    click.echo('[*] Database setup complete')
