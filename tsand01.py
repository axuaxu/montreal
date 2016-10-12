from sandman import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///montreal.sqlite'

from sandman.model import activate

activate(browser=True)

app.run()

