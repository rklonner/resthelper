"""Rest Helper

Usage:
  rest_helper.py -n NUMBER -c FILE
  rest_helper.py -h | --help
  rest_helper.py --version

Options:
  -h --help           Show this help.
  --version           Show version.
  -n --num NUMBER     Number of URLs (Integer: NUMBER > 0).
  -c --config FILE    Filename of a config.ini file.

"""

from __future__ import print_function
import warnings

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

    # save and validate command line arguments
    config_filename = arguments['--config']
    try:
        number_of_urls = int(arguments['--num'])
        if number_of_urls < 1:
            raise Exception((
                "An integer greater than zero is required "
                "for the argument '-n | --num'."))
    except ValueError:
        raise Exception((
            "An integer is required for the argument '-n | --num'."))

    config = read_config(config_filename)

    # read Urls and Data section from config file
    urls = config['Urls']
    username = config['Data'].get('username')
    url_restful_service = config['Data'].get('urlpath')

    # verify length of urls
    # if too many, raise warning and set to max length
    url_keys = config.options('Urls')
    max_number_of_urls = len(url_keys)
    if number_of_urls > max_number_of_urls:
        warnings.warn((
            "Too many urls requested ('" + str(number_of_urls) +
            "'). Set number to maximum available number ('" +
            str(max_number_of_urls) + "')."))
        number_of_urls = max_number_of_urls

    # loop over requested number of urls
    for url_key in url_keys[0:number_of_urls]:
        base_url = urls.get(url_key)  # read url from config

        # build restful url and print it
        restful_url = build_restful_url(
            base_url, username, url_restful_service)
        print(restful_url)


# if called directly, execute main function
if __name__ == '__main__':
    main()