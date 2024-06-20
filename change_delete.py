from read_write import read_data, write_data, print_data

def change_data():
    pass

def delete_data():
    data_list = []
    file = int(input("Enter number of file you want to work with: "))
        
    while file != 1 and file != 2:
        print ('Incorrect input')
        file = int(input('Enter number (1 or 2): '))

    if file == 1:
        data_list = read_data('data_first.csv', file)
    else:
        data_list = read_data('data_second.csv', file)

    del_index = print_data(data_list)
    
    answ = str(input (f"You want to delete record №{del_index}? (y/n): "))
    while answ!="y" and answ!="Y" and answ!="n" and answ!="N":
        print ('Incorrect input')
        answ = str(input ("Enter 'y'(yes) or 'n'(no): "))
    
    if answ == 'n' or answ == "N":
        print ("No changes were made")
        return

    del data_list[del_index-1]
    if file == 1:
        write_data('data_first.csv', data_list)
    else:
        write_data('data_second.csv', data_list)
    print (f"Record {del_index} was deleted")


delete_data()
