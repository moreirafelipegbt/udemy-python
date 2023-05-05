value = -10


class SmallValueException(BaseException):

    def __init__(self, msg):
        self.msg = msg

    def message(self):
        return self.msg


class LargeValueException(BaseException):

    def __init__(self, msg):
        self.msg = msg

    def message(self):
        return self.msg
try:
    if value < 0:
        raise SmallValueException('The value is too small...')
    elif value > 100:
        raise LargeValueException('The value is too large...')

except SmallValueException as small:
    print(small.message())
except LargeValueException as large:
    print(large.message())

print('The app finishes the execution')