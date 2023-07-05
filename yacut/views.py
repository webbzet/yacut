import string
import random
from flask import render_template, redirect, flash, url_for

from yacut import db, app
from yacut.models import URLMap
from yacut.forms import URLMapForm
from yacut.utils import get_short_id


def get_short_id():
    short = ''.join(random.choices(string.ascii_lowercase, k=6))
    if URLMap.query.filter_by(short=short).first():
        get_short_id()
    return short


@app.route('/<string:short>', methods=['GET'])
def short_link_redirect(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLMapForm()
    if form.validate_on_submit():
        short = form.custom_id.data
        if not short:
            short = get_short_id()
        if URLMap.query.filter_by(short=short).first():
            flash(f'Имя {short} уже занято!', 'dublikat')
            return render_template('yacut.html', form=form)
        db.session.add(URLMap(original=form.original_link.data, short=short))
        db.session.commit()
        flash(
            url_for('short_link_redirect', short=short, _external=True), 'link'
        )
    return render_template('yacut.html', form=form)
