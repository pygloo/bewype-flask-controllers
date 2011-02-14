# (C) Copyright 2010 Bewype <http://www.bewype.org>

# flask import
from flask import abort, url_for, redirect, session

# bewype import
from bewype.flask import app, render

# flask ext
from flaskext import themes


@app.route('/themes/')
def themes_list():
    _themes = themes.get_themes_list()
    return render('themes/list.html', themes=_themes)


@app.route('/themes/<identifier>')
def themes_save(identifier):
    if identifier not in app.theme_manager.themes:
        abort(404)
    session['theme'] = identifier
    return redirect(url_for('themes_list'))
