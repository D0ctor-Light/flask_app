from flask.cli import FlaskGroup
from timeweb.web import app, db, Data


cli = FlaskGroup(app)


@cli.command('create_db')
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


if __name__ == "__main__":
    cli()
