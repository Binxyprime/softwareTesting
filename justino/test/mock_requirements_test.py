from source.main import Interface
from unittest import TestCase
from test.plugins.ReqTracer import requirements
from git_utils import *
from os import path
from storyFunctions import *

#0100 The system shall return 'Yes' or 'No' when asked 'Is the <file path> in the repo?'
#0101 The system shall return one of the following when asked 'What is the status of <file path>?'
#0102 The system shall return '<hash>, <date modified>, <author>' when asked 'What is the deal with <file path>?'
#0103 The system shall return the repo branch when asked 'What branch is <file path>?'
#0104 The system shall return the repo url when asked 'Where did <file path> come from?'


class TestGetMockRequirements(TestCase):

    #0100 The system shall return 'Yes' or 'No' when asked 'Is the <file path> in the repo?'
    @requirements(['#0100'])
    def test_path_in_repo(self):
        obj = Interface()
        # result = obj.ask('Is the <file path> in the repo?')
        result = is_file_in_repo(path.basename("requirements.txt"))
        print result
        self.assertEqual(result, datetime.now().strftime('%m: %d: %y: %H:%M:%S'))

    @requirements(['#0100'])
    def test_path_not_in_repo(self):
        obj = Interface()
        # result = obj.ask('Is the <file path> in the repo?')
        result = is_file_in_repo(path.basename("source"))
        print result
        self.assertEqual(result, datetime.now().strftime('%m: %d: %y: %H:%M:%S'))

    #0101 The system shall return one of the following when asked 'What is the status of <file path>?'
    # needs 4 tests, at least one for each return value
    @requirements(['#0101'])
    def test_path_status1(self):
        obj = Interface()
        result = obj.ask('What is the status of <file path>?')
        self.assertEqual(result, datetime.now().strftime('%m: %d: %y: %H:%M:%S'))

    @requirements(['#0101'])
    def test_path_status2(self):
        obj = Interface()
        result = obj.ask('What is the status of <file path>?')
        self.assertEqual(result, datetime.now().strftime('%m: %d: %y: %H:%M:%S'))

    @requirements(['#0101'])
    def test_path_status3(self):
        obj = Interface()
        result = obj.ask('What is the status of <file path>?')
        self.assertEqual(result, datetime.now().strftime('%m: %d: %y: %H:%M:%S'))

    @requirements(['#0101'])
    def test_path_status4(self):
        obj = Interface()
        result = obj.ask('What is the status of <file path>?')
        self.assertEqual(result, datetime.now().strftime('%m: %d: %y: %H:%M:%S'))

    #0102 The system shall return '<hash>, <date modified>, <author>' when asked 'What is the deal with <file path>?'
    # also need one for an invalid file probably
    def test_path_deal(self):
        obj = Interface()
        result = obj.ask('What is the deal with <file path>?')
        self.assertEqual(result, datetime.now().strftime('%m: %d: %y: %H:%M:%S'))

    #0104 The system shall return the repo url when asked 'Where did <file path> come from?'
    # also need one for an invalid file probably
    def test_path_deal(self):
        obj = Interface()
        result = obj.ask('Where did <file path> come from?')
        self.assertEqual(result, datetime.now().strftime('%m: %d: %y: %H:%M:%S'))

