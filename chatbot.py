import openai
from scanner import Scanner

# Set up OpenAI API key
openai.api_key = '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'

# Set up scanner
scanner = Scanner()

def chat(prompt):
    # Send prompt to OpenAI API and retrieve response
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0
    )
    response_text = response.choices[0].text.strip()

    # Check if user wants to exit
    if 'exit' in response_text.lower():
        return None

    # Check if user wants to run a scan
    if 'scan' in response_text.lower():
        # Parse URL and run vulnerability scan
        url = input('Enter URL to scan: ')
        scanner.scan(url)
        return 'Scan complete. Use `show report` to see the results.'

    # If OpenAI API doesn't provide any relevant responses, return default message
    return "I'm sorry, I don't understand. Please try again or type `exit` to end the session."
