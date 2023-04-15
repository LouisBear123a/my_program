import argparse
import logging
from chatbot import Chatbot

if __name__ == '__main__':
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Web security chatbot')
    parser.add_argument('--debug', action='store_true', help='Enable debug logging')
    args = parser.parse_args()

    # Set up logging
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    # Create Chatbot instance
    chatbot = Chatbot()

    # Start chat loop
    print('Welcome to the web security chatbot.')
    while True:
        prompt = input('> ')
        response = chatbot.respond(prompt)
        if response is None:
            break
        print(response)
