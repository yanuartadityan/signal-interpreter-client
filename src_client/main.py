"""
main.py
"""
from argparse import ArgumentParser
from signal_interpreter_client.src_client.server_communication_handler import message_post


def main():
    """
    main.py
    """
    arg = ArgumentParser()
    arg.add_argument('--signal', required=True, help="String input for the POST payload", default=None)
    parsed_args = arg.parse_args()

    message = {
        "signal": parsed_args.signal
    }

    return_value = message_post("http://127.0.0.1:5000", message)
    print(return_value)


def init_app():
    """
    init_app
    """
    if __name__ == '__main__':
        main()

# run app
init_app()
