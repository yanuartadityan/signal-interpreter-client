from server_communication_handler import message_post
from argparse import ArgumentParser


if __name__ == '__main__':
    arg = ArgumentParser()
    arg.add_argument('--signal', required=True, help="String input for the POST payload", default=None)
    parsed_args = arg.parse_args()

    message = {
        "signal": parsed_args.signal
    }

    message_post("http://127.0.0.1:5000", message)

