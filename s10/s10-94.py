age = 9

try:

    if age < 10:
        raise Exception('You are underage...')

except Exception as exc:
    print(exc.args[0])