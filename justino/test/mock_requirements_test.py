from source.main import Interface
from unittest import TestCase
from plugins.ReqTracer import requirements
from source.git_utils import *
from os import path
from mock import patch, Mock


class TestMockRequirements(TestCase):
    # mock file in repo
    @patch('subprocess.Popen')
    @requirements(['#0100', '#0050', '#0051', '#0052'])
    def test_file_in_repo(self, mock_subproc_popen):
        obj = Interface()
        process_mock = Mock()
        attrs = {'communicate.return_value': ('', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = obj.ask('Is the <nose2.cfg> in the repo?')
        self.assertEqual(result, 'Yes')

    @patch('subprocess.Popen')
    @requirements(['#0100', '#0050', '#0051', '#0052'])
    def test_file_not_in_repo(self, mock_subproc_popen):
        obj = Interface()
        process_mock = Mock()
        attrs = {'communicate.return_value': ('test.txt', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = obj.ask('Is the <test.txt> in the repo?')
        self.assertEqual(result, 'No')

    # mock file status
    @patch('source.git_utils.get_diff_files')
    @requirements(['#0101', '#0050', '#0051', '#0052'])
    def test_file_modified(self, mock_subproc_diff_files):
        obj = Interface()
        mock_subproc_diff_files.return_value = os.path.abspath('requirements.txt')
        result = obj.ask('What is the status of <requirements.txt>?')
        self.assertEqual(result, 'requirements.txt has been modified locally')

    @patch('source.git_utils.get_diff_files')
    @patch('source.git_utils.get_untracked_files')
    @requirements(['#0101', '#0050', '#0051', '#0052'])
    def test_file_untracked(self, mock_untracked, mock_diff):
        obj = Interface()
        mock_diff.return_value = []
        mock_untracked.return_value = os.path.abspath('requirements.txt')
        result = obj.ask('What is the status of <requirements.txt>?')
        self.assertEqual(result, 'requirements.txt has not been checked in')

    @patch('source.git_utils.get_diff_files')
    @patch('source.git_utils.get_untracked_files')
    @patch('source.git_utils.is_repo_dirty')
    @requirements(['#0101', '#0050', '#0051', '#0052'])
    def test_file_dirty(self, mock_dirty, mock_untracked, mock_diff):
        obj = Interface()
        mock_diff.return_value = []
        mock_dirty = True
        mock_untracked.return_value = []
        result = obj.ask('What is the status of <requirements.txt>?')
        self.assertEqual(result, 'requirements.txt is a dirty repo')

    @patch('subprocess.Popen')
    @requirements(['#0102', '#0050', '#0051', '#0052'])
    def test_file_info(self, mock_subproc_popen):
        obj = Interface()
        process_mock = Mock()
        attrs = {'communicate.return_value': ('__file__', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = obj.ask('What is the deal with <{}>?'.format(__file__))
        self.assertEqual(result, '__file__')

    # mock repo branch
    @patch('subprocess.Popen')
    @requirements(['#0103', '#0050', '#0051', '#0052'])
    def test_repo_branch(self, mock_subproc_popen):
        obj = Interface()
        process_mock = Mock()
        attrs = {'communicate.return_value': ('__file__', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = obj.ask('What branch is <{}>?'.format(__file__))
        self.assertEqual(result, '__file__')

    # mock repo url
    @patch('subprocess.Popen')
    @requirements(['#0104', '#0050', '#0051', '#0052'])
    def test_repo_url(self, mock_subproc_popen):
        obj = Interface()
        process_mock = Mock()
        attrs = {'communicate.return_value': ('__file__', '')}
        process_mock.configure_mock(**attrs)
        mock_subproc_popen.return_value = process_mock
        result = obj.ask('Where did <{}> come from?'.format(__file__))
        self.assertEqual(result, '__file__')

    # Coverage functions
    @requirements(['#0101'])
    def test_path_checker(self):
        self.assertRaisesRegexp(Exception, 'Path blah does not exist cannot get git file', get_git_file_info, 'blah')

    @requirements(['#0101'])
    def test_is_file_in_repo_cov(self):
        self.assertRaisesRegexp(Exception, '%s changed or is untracked in repo %s', is_file_in_repo, 'requirements.txt')



