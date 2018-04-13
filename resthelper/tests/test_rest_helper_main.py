import unittest

import docopt

from resthelper import rest_helper


class TestConsole(unittest.TestCase):
    def test_command_line_script_main(self):
        # call without the right command line arguments that are used by
        # docopt should raise DocoptExit with help message
        self.assertRaises(docopt.DocoptExit, rest_helper.main)


if __name__ == '__main__':
    unittest.main()