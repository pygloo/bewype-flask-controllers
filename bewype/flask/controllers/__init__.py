# (C) Copyright 2010 Bewype <http://www.bewype.org>

__import__('pkg_resources').declare_namespace(__name__)

# python import
import os

# peak import
from peak.util.imports import importString

# bewype import
from bewype.config import _obj as c

# bewype-flask import
from bewype.flask import app


def _init_controllers():
    """Here we init all the controllers of the bewype namespace before running
    the app.
    """
    # simple shortcut
    _namespace = "bewype.flask.controllers"
    # controllers name space
    _controllers_package = importString(_namespace)
    # controllers all paths
    _controllers_paths = _controllers_package.__path__
    # ...
    for _p in _controllers_paths:
        for _f in os.listdir(_p):
            # simple check
            if '__init__.' in _f\
            or os.path.splitext(_f)[-1] != '.py':
                continue
            # do init
            else:
                _controller_name = os.path.splitext(_f)[0]
                _c = importString("%s.%s" % (_namespace, _controller_name))
                # prepare module name - custom bewype
                _m_name = 'module_%s' % _controller_name
                # module check
                if hasattr(_c, _m_name):
                    # get module
                    _m = getattr(_c, _m_name)
                    _controller_name
                    # get templates search path
                    _search_path = _m.jinja_loader.searchpath
                    # update jinja loader templates search path
                    app.jinja_loader.searchpath.extend(_search_path)


def run():
    """Starting the app.
    """
    # init all
    _init_controllers()
    # prepare run values
    _debug = c.app.debug.as_bool()
    # do run
    app.run(debug=_debug)
