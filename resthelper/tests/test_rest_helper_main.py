import unittest

import docopt

from resthelper import rest_helper


class TestConsole(unittest.TestCase):
    def test_command_line_script_main(self):
        # call without the command line arguments that are specified with
        # docopt in main script should raise DocoptExit with help message
        self.assertRaises(docopt.DocoptExit, rest_helper.main)


if __name__ == '__main__':
    unittest.main()