
class CustomError(Exception):
    pass


def exception_test(x: int, y: int):
    try:
        if x + y <= 0:
            raise CustomError("The value is below 0")
        elif x + y == 0:
            raise CustomError("The value is 0")
        else:
            raise CustomError("The value is above 0")
    except CustomError:
        return CustomError

exception_test(2, 4)