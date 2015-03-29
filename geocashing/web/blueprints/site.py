from flask import Blueprint, redirect, url_for


bp_site = _bp = Blueprint('site', __name__)


@_bp.route('/')
def home():
    return redirect(url_for('geocaches.create'))
