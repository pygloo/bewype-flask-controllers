# (C) Copyright 2010 Bewype <http://www.bewype.org>

# flask import
from flask import Flask, session

# flask themes
from flaskext.themes import setup_themes, render_theme_template

# bewype import
from bewype.config import _obj as c


def render(template, **context):
    """Theme renderer shortcut.
    """
    _theme = session.get('theme', 'default')
    return render_theme_template(_theme, template, **context)


# The app
app = None


def __init():
    """Dummy unique init method.
    """
    # get secret key.
    _secret_key = c.app.secret_key if hasattr(c, 'app') is True else None
    # get identifier
    _identifier = c.app.identifier if hasattr(c, 'app') is True else None
    # ...
    global app
    if app is None\
    and _secret_key is not None\
    and _identifier is not None:
        # get/set app
        app = Flask(__name__)
        app.secret_key = _secret_key
        # set themes path - currently hard coded for `easy to use` reason
        app.config['THEME_PATHS'] = ['themes']
        # init themes
        setup_themes(app, app_identifier=_identifier)


# do init
__init()
