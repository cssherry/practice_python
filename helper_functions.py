"""A bunch of helper functions"""
def append_txt(filename):
    """To append .txt extension if it doesn't already exist"""
    if filename[-4:] != ".txt":
        filename += ".txt"
    return filename
