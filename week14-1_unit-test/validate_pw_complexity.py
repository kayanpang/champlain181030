import re

def validate_pw_complexity(password: str):

    if not re.match("^.{8,}", password):
        # 8 characters or more
        complex_enough = False

    # if not re.match("[a-z]", password):
    #     complex_enough = False
    #     # lower case
    #
    # if not re.match("[A-Z]", password):
    #     complex_enough = False
    #     # upper case
    #
    # if not re.match("[\d]", password):
    #     complex_enough = False
    #     # number
    #
    # if not re.match("[^0-9A-Za-z\s]", password):
    #     complex_enough = False
    #     # special character
    #
    # if not re.match("\s", password):
    #     complex_enough = False
    #     # no whitespace

    return complex_enough

def validate_password_length(password: str):

# pattern take 1 ("(?=.*\d)(?=.*\[a-z])(?=.*[A-Z]).(^.{8,}")
# better write separately as rules might change later