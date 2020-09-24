from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

bp = Blueprint('api', __name__, template_folder='templates')


@bp.route('/', defaults={'page': 'index'})
@bp.route('/<page>')
def show(page):
    try:
        return render_template('pages/%s.html' % page)
    except TemplateNotFound:
        abort(404)
