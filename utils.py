import requests


def check_url(url):
    """
    Check if the provided URL is valid and returns the response code.

    Args:
        url (str): The URL to check.

    Returns:
        int: The response code for the URL.

    Raises:
        ValueError: If the URL is invalid or the request failed.
    """
    try:
        response = requests.head(url)
        return response.status_code
    except requests.exceptions.RequestException:
        raise ValueError('Invalid URL or request failed.')
        

def format_vulnerability(vulnerability):
    """
    Format a vulnerability dictionary into a string.

    Args:
        vulnerability (dict): The vulnerability to format.

    Returns:
        str: The formatted vulnerability string.
    """
    return f"{vulnerability['name']} ({vulnerability['severity']}): {vulnerability['description']}"


def format_exploit(exploit):
    """
    Format an exploit dictionary into a string.

    Args:
        exploit (dict): The exploit to format.

    Returns:
        str: The formatted exploit string.
    """
    return f"{exploit['name']} ({exploit['type']}): {exploit['description']}"
