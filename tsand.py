from sandman import app, db
from sandman.model import activate
app.config['SQLALCHEMY_DATABASE_URI'] = 'monreal.sqlite'

from sandman.model import register, Model

#class Artist(Model):
#    __tablename__ = 'Artist'

#class Album(Model):
#    __tablename__ = 'Album'

#class Playlist(Model):
#    __tablename__ = 'Playlist'

#register((Artist, Album, Playlist))


class monrent(Model):
     __tablename__ = 'monrent'

class plinks(Model):
     __tablename__= 'plinks'
register((monrent,plinks))
sandman.model.activate_admin_classes
app.run()
