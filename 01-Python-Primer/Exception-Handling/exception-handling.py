age = -1

while age <= 0:
    try:
        age = int(input('Enter your age in years :'))
        if age <= 0:
            print('You age must be positive')

    except ValueError:
        print('invalid age specification')
    except EOFError:
        print('unexpected error')
        raise