def banner(text, char='=', length=80):
    """
    Create a simple banner surrounding :param text

    EXAMPLE:
        banner('Some Header', '=') returns
        =============[ Some Header ]=============

    :param text: The text to surround
    :param char: The character to surround :param text with
    :param length: The total length of the line
    :returns: String representation of the banner
    """
    text = '[ {text} ]'.format(text=text)
    banner = '\n{text:{char}^{length}}'.format(text=text, char=char, length=length)
    return banner