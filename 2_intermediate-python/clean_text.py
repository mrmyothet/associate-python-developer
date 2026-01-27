product = "Wireless Mouse"


# Define clean_text function
def clean_text(text, lower=True):
    """
    Clean text by swapping spaces to underscores and converting to lowercase.

    Args:
        text (str): A string to be cleaned.
        lower (bool): Whether to convert the text to lowercase.

    Returns:
        text (str): Cleaned string.
    """
    clean_text = text.replace(" ", "_")
    if lower == False:
        return clean_text
    else:
        # Apply lowercase transformation
        return clean_text.lower()


# Test with default behavior
print(clean_text(product))
