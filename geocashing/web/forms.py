import re

from flask import render_template, Markup
from flask_wtf import Form

from wtforms import StringField
from wtforms.validators import DataRequired, Regexp, Length
from wtforms.widgets import TextInput, TextArea


GEOCACHE_CODE_RE = re.compile(r'GC\w{1,7}')


class UITextWidget(object):
    base_widget = TextInput

    def __call__(self, field, **kwargs):
        return Markup(render_template('widgets/ui-field.html', field=field, kwargs=kwargs, input=self.base_widget()))


class UITextAreaWidget(UITextWidget):
    base_widget = TextArea


class UIStringField(StringField):
    widget = UITextWidget()


class CreateForm(Form):
    code = UIStringField('Code', description="The Geocache code, <em>GCxxx</em>",
                         validators=[DataRequired(), Regexp(GEOCACHE_CODE_RE)])
    title = UIStringField('Title', validators=[DataRequired(), Length(min=5)])
    text = UIStringField('Description', validators=[DataRequired(), Length(min=10)], widget=UITextAreaWidget())
