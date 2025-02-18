def is_valid_url():
    """
    Checks if the user input is a valid URL.
    :return: True if the input is a valid URL, False otherwise
    """

    # Ask the user for input
    url = input("Enter a URL: ")

    # A valid URL should start with "http://" or "https://"
    if url.startswith("http://") or url.startswith("https://"):

        # Remove "http://" or "https://" to check the rest
        url = url.split("://")[1]

        # A valid domain should have at least one dot "."
        if "." in url:
            return True  # It's valid

    return False  # If any check fails, it's not a URL

print(is_valid_url())

