import  model
import  view
import time


def start():
    while (True):
        view.clear_screen()
        choice = view.main_menu()
        match choice:
            case "1":
                # вывод данных
                view.show_contacts(model.readFile())
                view.exit_in_menu()
            case "2":
                # добавление данных
                new_contact = list(view.create_new_contact())
                model.add_new_contact(new_contact)
                view.exit_in_menu()
            case "3":
                # поиск
                find = view.find_contact()
                result, n = model.search_contact(find)
                view.show_contacts(result)
                view.exit_in_menu()
            case "4":
                # удаление данных
                contact = view.del_contact()
                result, index = model.search_contact(contact)
                view.show_contacts_index(result, index)
                index = view.index_view()
                model.delete_contact(index)
                view.exit_in_menu()
            case "5":
                # Замена номера
                change = view.change_contacts()
                result, index = model.search_contact(change)
                view.show_contacts_index(result, index)
                index = view.index_view()
                choice = view.choice_change()
                model.change_contact(index, choice,)
                view.exit_in_menu()
            case "6":
                # выход
                exit(0)
            case _:
                print("неверный ввод")
                time.sleep(3)