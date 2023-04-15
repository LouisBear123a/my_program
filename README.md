# my_program
Ai vulnerability scanner and attacker. Yknow. As you do.

The program is a web security chatbot that allows users to run vulnerability scans and exploits on websites. The program is split into several modules, including chatbot.py, scanner.py, exploits.py, and utils.py, which handle different aspects of the program's functionality.

The chatbot module handles the main loop for the chatbot and sends user prompts to the OpenAI API to retrieve responses. If the user requests a scan or exploit, the chatbot module calls functions from the scanner and exploits modules to perform the requested action.

The scanner module includes sub-modules for crawling, nmap scanning, OpenVAS scanning, and ZAP scanning. These modules use various tools and APIs to scan websites for vulnerabilities and return reports on any findings.

The exploits module includes functions for running exploits on vulnerable websites. These functions use various exploit frameworks and payloads to gain access to vulnerable sites and allow the user to execute commands on the target machine.

The utils module includes various utility functions used throughout the program, such as functions for formatting and printing output and functions for interacting with the OpenAI API.

To run the program, you will need to install the required Python packages listed in the requirements.txt file. Once installed, you can run the program by executing the main.py file in the command line. The chatbot will prompt you for input and respond with relevant information based on your requests.
