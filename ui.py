from logger import input_data, print_data

def interface():
    print("Phonebook \n1 - write data \n2 - read data")
    command = int(input('Enter number: '))

    while command != 1 and command != 2:
        print ('Incorrect input')
        command = int(input('Enter number: '))

    if command == 1:
        input_data()
    elif command == 2:
        print_data()

