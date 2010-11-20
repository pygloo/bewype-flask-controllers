#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python import
import os
from ConfigParser import SafeConfigParser

class Config(object):
    """Simple config singleton for a bewype application. Offers shortcut methods
    to obtain config values directly.
    """

    class __Singleton:
        """Our singleton object.
        """

        def __init__(self):
            """Create the new singleton with the application config.

            :param config: SafeConfigParser object for all the application
            :see: `ConfigParser.SafeConfigParser`
            """
            # get config dir
            _config_dir = os.path.abspath(os.path.dirname(__file__))
            # read config
            self.config = SafeConfigParser()
            self.config.read(os.path.join(_config_dir, 'config.ini'))

        def get_bool(self, path):
            """Call common get_value function with bool type parameter.
            """
            return self.get(path, type_=bool)

        def get_int(self, path):
            """Call common get_value function with int type parameter.
            """
            return self.get(path, type_=int)

        def get_str(self, path):
            """Call common get_value function with str type parameter.
            """
            return self.get(path, type_=str)

        def get(self, path, type_=str):
            """A little jQuery like shortcut for the `get_value` method.

            :param path: something like "section>option"
            :param type_: type of the expected value. Default: str
            :return: expected value in the expected type or None
            :rtype: `object`
            """
            # get value
            _value = self.get_value(*path.split(">"), type_=type_)
            # check and return
            return None if _value is None or _value == "" else _value

        def get_value(self, section, option, type_=str):
            """Simple config value getter to avoid exception risk when getting
            a config value. If the section and option exist, returns the
            corresponding value, None otherwise.

            The `type_` parameter specify the expected option type and
            return.

            :param section: section name of the expected value
            :param option: option name name of the expected value
            :param type_: type of the expected value. Default: str
            :return: expected value in the expected type or None
            :rtype: `object`
            """
            # check has config
            if self.config is None:
                return None
            # check value exist
            elif self.config.has_section(section) \
            and self.config.has_option(section, option):
                # check expected value type
                if type_ is int:
                    return self.config.getint(section, option)
                elif type_ is bool:
                    return self.config.getboolean(section, option)
                elif type_ is str:
                    return self.config.get(section, option)
                # unexpected type ??
                else:
                    return None
            # value does not exist                
            else:
                # do nothing
                return None

        def get_section(self, section):
            """Returns a dict object with the content of the section passed as
            parameter. None if the section does not exist.

            :param section: section name of the expected value
            """
            # check has config
            if self.config is None:
                return None
            # check section exist
            elif self.config.has_section(section):
                # build and return dict with the given section
                return dict(self.config.items(section))
            # not found
            else:
                # do nothing
                return None

    # singleton instance
    instance = None

    def __new__(c, force=False):
        """Singleton new init.
        """
        # if doesn't already initialized
        if not Config.instance \
        or force is True:
            # create a new instance
            Config.instance = Config.__Singleton()
        # return the manager object
        return Config.instance

