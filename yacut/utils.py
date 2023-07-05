import random
import string

from yacut.models import URLMap


def get_short_id():
    short = ''.join(random.choices(string.ascii_lowercase, k=6))
    if URLMap.query.filter_by(short=short).first():
        get_short_id()
    return short
