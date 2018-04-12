import os
# python 2/3 support:
#   - configpaser will import backport on python 2
#   - will default to built-in version on python 3
import configparser
import re
import collections


def read_config(filename):
    """Reads a configfile"""
    # check if file exists
    if not os.path.isfile(filename):
        raise OSError("No such file '" + filename + "'")

    # ensure order of config.ini so use OrderedDict
    # important to use keys from URLs
    # sections directly without building keys
    config = configparser.ConfigParser(dict_type=collections.OrderedDict)
    config.read(filename)
    return config


def build_restful_url(base_url, username, url_restful_service):
    """Builds a restful service URL on the basis of atttributes"""
    # use regexp to support http and https
    # and to prepare for more complex ulrs
    pattern = re.compile(r"(?P<protocol>http[s]?://)(?P<hostname>.*)")
    match = pattern.match(base_url)
    protocol = match.group('protocol')
    hostname = match.group('hostname')

    # define basic strucutre of url and prepare substitution
    restful_url_template = (
        "%(protocol)s%(username)s@%(hostname)s%(url_restful_service)s")

    # attributes to be substituted
    attributes = {
        "protocol": protocol,
        "username": username,
        "hostname": hostname,
        "url_restful_service": url_restful_service
    }

    # substitute attributes of template
    restful_url = restful_url_template % attributes
    return restful_url