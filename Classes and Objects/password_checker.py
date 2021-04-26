

class InvalidPasswordError(Exception):
    pass


class ShortPasswordError(InvalidPasswordError):
    pass


class NoNumbersInPasswordError(InvalidPasswordError):
    pass


class NoSpecialInPassowordError(InvalidPasswordError):
    pass


def check_password(password):
    if len(password) < 8:
        raise ShortPasswordError(password)
    for n in "0123456789":
        if n in password:
            break

    else:
        raise NoNumbersInPasswordError(password)
    for s in "?!.":
        if s in password:
            break

    else:
        raise NoSpecialInPassowordError(password)
