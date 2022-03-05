class CustomException(Exception):
    """Invalid sign string provided"""


if __name__ == '__main__':
    print(type(CustomException()))