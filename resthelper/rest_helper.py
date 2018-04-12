"""Rest Helper

Usage:
  rest_helper.py -n NUMBER -c FILE
  rest_helper.py -h | --help
  rest_helper.py --version

Options:
  -h --help           Show this help.
  --version           Show version.
  -n --num NUMBER     Number of urls.
  -c --config FILE    Filename of a config.ini file.

"""

from __future__ import print_function

import warnings
# ToDo: from future import print_fuction? up to which 2.x version?

from docopt import docopt

from resthelper.utils import read_config, build_restful_url


def main():
    """Builds restful service URLs on the basis of a configfile.

    Execution function for command line tool. Uses docopt to parse
    argmuents when used as command line tool. Reads a configfile to
    get propterties of a restful service url and prints it on the
    console.
    """
    arguments = docopt(__doc__, version='Rest Helper 0.1')

    # save command line arguments
    # ToDo: use schemas to parse type
    config_filename = arguments['--config']
    number_of_urls = int(arguments['--num'])

    config = read_config(config_filename)

    # read Urls and Data section from config file
    urls = config['Urls']
    username = config['Data'].get('username')
    url_restful_service = config['Data'].get('urlpath')

    # verify length of urls
    # if too many, raise warning and set to max length
    max_number_of_urls = len(urls.keys())
    if number_of_urls > max_number_of_urls:
        warnings.warn((
            "Too many urls requested ('" + str(number_of_urls) +
            "'). Set number to maximum available number ('" +
            str(max_number_of_urls) + "')."))
        number_of_urls = max_number_of_urls

    # loop over requested numbers of urls
    for num in range(1, number_of_urls + 1):
        # todo: for key,value in dict so that we dont need key build?
        key = 'url' + str(num)  # build url config key
        base_url = urls.get(key)  # read url from config

        # build restful url and print it
        restful_url = build_restful_url(
            base_url, username, url_restful_service)
        print(restful_url)