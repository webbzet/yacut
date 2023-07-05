from re import match
from http import HTTPStatus
from flask import request, jsonify
import validators

from yacut import db, app
from yacut.utils import get_short_id
from yacut.error_handlers import InvalidAPI
from yacut.models import URLMap


@app.route('/api/id/', methods=['POST'])
def add_urlmap():
    """Создание короткой ссылки"""
    data = request.get_json()
    if not data:
        raise InvalidAPI('Отсутствует тело запроса', HTTPStatus.BAD_REQUEST)
    if 'url' not in data:
        raise InvalidAPI(
            '"url" является обязательным полем!', HTTPStatus.BAD_REQUEST
        )
    if 'custom_id' not in data or not data['custom_id']:
        data['custom_id'] = get_short_id()
    if not validators.url(data['url']):
        raise InvalidAPI('Некорректный URL', HTTPStatus.BAD_REQUEST)
    if not match(r'^[A-Za-z0-9]{1,16}$', data['custom_id']):
        raise InvalidAPI(
            'Указано недопустимое имя для короткой ссылки', HTTPStatus.BAD_REQUEST
        )
    if URLMap.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPI(
            f'Имя "{data["custom_id"]}" уже занято.', HTTPStatus.BAD_REQUEST
        )
    urlmap = URLMap()
    urlmap.from_dict(data)
    db.session.add(urlmap)
    db.session.commit()
    return jsonify(urlmap.to_dict()), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/',)
def get_url(short_id):
    """Получение оригинальной ссылки"""
    if not short_id:
        raise InvalidAPI('Поле "short_id" является обязательным')
    new_url = URLMap.query.filter_by(short=short_id).first()
    if not new_url:
        raise InvalidAPI('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': new_url.original}), HTTPStatus.OK
