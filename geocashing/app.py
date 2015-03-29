import os

from flask import Flask

from geocashing.db import db
from geocashing.web.assets import init_assets
from geocashing.web.blueprints.geocaches import bp_geocaches
from geocashing.web.blueprints.site import bp_site


NAV_ITEMS = ({'id': 'home',
              'title': 'Home',
              'url': 'site.home'},
             {'id': 'create',
              'title': 'Create',
              'url': 'geocaches.create'},
             {'id': 'contact',
              'title': 'Contact',
              'url': 'site.home'})


def make_app():
    app = Flask(__name__, template_folder='web/templates')
    app.config.from_pyfile(os.environ.get('GEOCASHING_CONFIG', 'app.conf'))

    app.register_blueprint(bp_geocaches)
    app.register_blueprint(bp_site)

    app.jinja_env.globals.update(
        nav_items=NAV_ITEMS
    )

    init_assets(app)
    db.init_app(app)

    return app

app = make_app()
