from sandman import app, db

app.config['SQLALCHEMY_DATABASE_URI'] = '<your DB's SQLAlchemy connection string>'

from sandman.model import register, Model

class Artist(Model):
    __tablename__ = 'Artist'

class Album(Model):
    __tablename__ = 'Album'

class Playlist(Model):
    __tablename__ = 'Playlist'

register((Artist, Album, Playlist))

app.run()
