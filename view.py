import os

from sys import platform

commands = ['Показать все контакты',
            'Добавление контакта',
            'Поиск контакта',
            'Удаление контакта',
            'Изменение контакта',
            'Выход',]

def clear_screen():
    #очистка экрана (кроссплатформенная)
    if platform == "linux" or platform == "linux2" or platform == "darwin":
        os.system("clear")  # для Linux & MacOS
    else:
        os.system("cls")    # для Windows

def main_menu():
    print('Главное меню')
    for i, item in enumerate(commands, 1):
        print(f'\t{i} {item}')
    choice = input('Выберите пункт меню: ')
    return choice

def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print('Телефонная книга пустая')
    else:
        print(f'\t№. {"Имя":30} {"Телефон":15} {"Комментарий":15}')
        for i, contact in enumerate(phone_list, 1):
                print(f'\t{i}. {contact[0]:30} {contact[1]:15} {contact[2]:20}')
        
def exit_in_menu():
    input(f'Enter выход в меню>: ')

def create_new_contact():
    print('Новый контакт')
    name = input('Введите имя и фамилию: ')
    phone =input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

def find_contact():
    find = input('Введите искомый элемент: ')
    return find


def del_contact():
    search = input(f'Поиск контакта который хотите удалить>: ')
    return search

def change_contacts():
    search = input(f'Поиск контакта который хотите поменять>: ')
    return search

def show_contacts_index(phone_list: list, index_list: list):
    if len(phone_list) < 1:
        print('Телефонная книга пустая')
    else:
        print(f'\t№. {"Имя":30} {"Телефон":15} {"Комментарий":15} {"Индекс":1}')
        for i, contact in enumerate(phone_list, 1):
                print(f'\t{i}. {contact[0]:30} {contact[1]:15} {contact[2]:20} {index_list[i-1]:1}')

def index_view():
    index = input(f'Введите индекс контакта: ')
    return index
def choice_change():
    choice = input(f'Что хотите поменять (0) Имя, (1) Номер телефона, (2) комментарий введите цифру\n>:')
    return choice