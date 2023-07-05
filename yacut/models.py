from datetime import datetime
from flask import url_for
from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(
            url=self.original,
            short_link=url_for('short_link_redirect', short=self.short, _external=True)
        )

    def from_dict(self, data):
        self.original = data['url']
        self.short = data['custom_id']
