from unittest import TestCase

import docopt

from resthelper.rest_helper import main

class TestConsole(TestCase):
    def test_command_line_script_main(self):
        # call without the right command line arguments that are used by
        # docopt should raise DocoptExit with help message
        self.assertRaises(docopt.DocoptExit, main)

if __name__ == '__main__':
    unittest.main()