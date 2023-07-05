from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, URLField
from wtforms.validators import Optional, Length, URL, DataRequired, Regexp


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            URL(require_tld=True, message=('Некорректный URL')),
            DataRequired(message='Укажите ссылку')
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16),
            Regexp(
                regex=r'^[A-Za-z0-9]{1,16}$',
                message='Недопустимое имя для короткой ссылки',
            ),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
