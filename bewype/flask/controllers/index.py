# (C) Copyright 2010 Bewype <http://www.bewype.org>

# bewype import
from bewype.flask import app, render

@app.route('/')
def index():
    return render('index.html', greetings='Welcome!')
