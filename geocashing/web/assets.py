import os
from webassets.loaders import YAMLLoader
from flask_assets import Environment


def init_assets(app):
    env = Environment(app)
    env.register(YAMLLoader(os.path.join(app.root_path, '..', 'bundles.yaml')).load_bundles())
    return env
