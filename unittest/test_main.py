"""
test_main.py (client)
"""
from argparse import ArgumentParser
from unittest import TestCase
from unittest.mock import patch
from signal_interpreter_client.src_client.main import init_app, main


class MainTestClient(TestCase):
    """
    MainTestClient
    """

    def setup_parser(self):
        """
        setup_parser
        """
        self.parser = ArgumentParser()
        self.parser.add_argument('--signal')

    def test_main_argument_parser(self):
        """
        test_main_argument_parser
        """
        self.setup_parser()

        parsed_short = self.parser.parse_args(['--signal', '11'])

        self.assertEqual(parsed_short.signal, '11')

    @staticmethod
    @patch('sys.argv', ['test_main',
                        '--signal',
                        '27'])
    def test_main():
        """
        test_main --> check if message post is called at least once
        """
        pstr = 'signal_interpreter_client.src_client.main.message_post'
        with patch(pstr) as mock_run:
            main()
            mock_run.assert_called_once()

    @staticmethod
    @patch('signal_interpreter_client.src_client.main.__name__',
            '__main__')
    @patch('sys.argv', ['test_main', '--signal', '11'])
    def test_init():
        """
        test_init
        """
        with patch('signal_interpreter_client.src_client.main.main') as mock_main:
            init_app()
            mock_main.assert_called_once()