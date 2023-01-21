
phone_book = []
path = 'Tel.txt'

def readFile():
    result = []
    with open(path, 'r+', encoding='utf8') as data:
        for line in data:
            result.append(line.strip().split(','))
    return result

def add_new_contact(new_contact: list):
        data_to_save = ",".join(new_contact)+"\n"
        print(data_to_save)
        with open(path, 'a', encoding='utf8') as datafile:
            datafile.write(data_to_save)

def search_contact(find: str):
    result = []
    index = 0
    index_list = []
    phone_book = readFile()
    for contact in phone_book:
      for field in contact:
        if find in field:
          result.append(contact)
          index_list.append(index)
          break
      index += 1
    return result, index_list

def delete_contact(delete_contact: str):
    phone_book = readFile()
    if delete_contact == '':
        return
    else:
        phone_book.pop(int(delete_contact))
        with open(path, 'w', encoding='utf8') as data:
            data.write('')
        for i in phone_book:
            save_data_to_file(i)

def save_data_to_file(data_to_save):
    data_to_save = ",".join(data_to_save)+"\n"
    print(data_to_save)
    with open('Tel.txt', 'a', encoding='utf8') as datafile:
        datafile.write(data_to_save)


def change_contact(change_contact: str, choice: str):
    phone_book = readFile()
    if change_contact == '':
        return
    else:
        phone_book[int(change_contact)][int(choice)] = input('Введите: ')
        with open('Tel.txt', 'w', encoding='utf8') as data:
            data.write('')
        for i in phone_book:
            save_data_to_file(i)