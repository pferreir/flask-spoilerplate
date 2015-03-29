from flask import Blueprint, redirect, render_template, url_for
from sqlalchemy.orm.exc import NoResultFound

from geocashing.db import db
from geocashing.models.geocache import GeoCache
from geocashing.web.forms import CreateForm


bp_geocaches = _bp = Blueprint('geocaches', __name__, template_folder='templates')


@_bp.route('/geocache/<code>/')
def display(code):
    try:
        cache = GeoCache.find_one(code=code)
        return render_template('display.html', cache=cache)
    except NoResultFound:
        return "Cache not found", 404


@_bp.route('/geocache/create/', methods=("GET", "POST"))
def create():
    form = CreateForm()
    if form.validate_on_submit():
        cache = GeoCache(form.code.data, form.title.data, form.text.data)
        db.session.add(cache)
        db.session.commit()
        return redirect(url_for('.display', code=cache.code))
    else:
        return render_template('create.html', form=form)
