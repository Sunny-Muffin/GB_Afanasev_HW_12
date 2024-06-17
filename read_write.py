def read_data(file_path, file_num):
    if file_num == 1:
        with open(file_path, 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            data_first_list = []
            j = 0
            for i in range(len(data_first)):
                if data_first[i] == '\n' or i == len(data_first) - 1:
                    data_first_list.append(''.join(data_first[j:i+1])) # запись [j:i+1] - срез
                    j = i
            return data_first_list
    elif file_num == 2:
        with open(file_path, 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            data_second_list = []
            for i in range(len(data_second)):
                if data_second[i] != '\n':
                    data_second_list.append(data_second[i])
            return data_second_list


def write_data(file_path, file_num):
    if file_num == 1:
        pass
    elif file_num == 2:
        pass


print(read_data('data_first.csv', 1))
print(read_data('data_second.csv', 2))