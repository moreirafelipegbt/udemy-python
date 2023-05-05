def show_name(**params):
    print(params['address'])
    print(params['lname'])
    print(params['age'])
    print(params['gender'])

show_name(fname="Felipe", lname="Moreira", age=32, gender='male', address="8th street")