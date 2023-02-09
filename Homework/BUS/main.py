import os
import time
import function as fn

def cls():
    os.system('cls')
cls()    

def main_menu():
    cls()
    print('===================================\n'
          '|   Справочник автобусного парка  |\n'
          '===================================\n'
          '|           Главное меню          |\n'
          '===================================')
 
    menuitems = [("1", "- Показать все автобусы"),
                 ("2", "- Добавить новый автобус"),
                 ("3", "- Показать всех водителей"),
                 ("4", "- Добавить нового водителя"),
                 ("5", "- Показать все маршруты"),
                 ("6", "- Добавить новый маршрут"),
                 ("7", "- Детализация маршрута"),
                 ("8", "- Удаление данных"),
                 ("0", "- Выход")]
    
    for i in menuitems:
        print(i[0], i[1])


def bus_fleet_book():
    while True:
        main_menu()
      
        user_choice = input('Выберите необходимый пункт меню: ')


        if user_choice == '1':
            cls()
            print('==============================\n'
                  '|      Список автобусов      |\n'
                  '==============================')
            if os.path.exists('bus.txt'):
                print(fn.read_data_from_file('bus.txt'))
            else: 
                print('Список автобусов пуст. Добавьте хотя бы один автобус. Выход в главное меню через 3 секунды...')
                time.sleep(3)
            


        elif user_choice == '2':
            cls()
            print('==============================\n'
                  '| Добавление нового автобуса |\n'
                  '==============================')
            while True:
                fn.save_data_to_file('bus.txt', input('ID автобуса(в формате bus#): '), input('Госномер автобуса: '))
                choice = input('\nНажмите Enter чтобы добавить новый автобус\nВведите 0 для выхода\n')
                if choice == '0': 
                    bus_fleet_book()


        elif user_choice == '3':
            cls()
            print('==============================\n'
                  '|      Список водителей      |\n'
                  '==============================')
            if os.path.exists('driver.txt'):
                print(fn.read_data_from_file('driver.txt'))
            else: 
                print('Список водителей пуст. Добавьте хотя бы одного водителя. Выход в главное меню через 3 секунды...')
                time.sleep(3)


        elif user_choice == '4':
            cls()
            print('==============================\n'
                  '| Добавление нового водителя |\n'
                  '==============================')
            while True:
                fn.save_data_to_file('driver.txt', input('ID водителя(в формате driver#): '), input('Фамилия Имя Отчество (через пробел): '))
                choice = input('\nНажмите Enter чтобы добавить нового водителя\nВведите 0 для выхода\n')
                if choice == '0': 
                    bus_fleet_book()


        elif user_choice == '5':
            cls()
            print('==============================\n'
                  '|      Список маршрутов      |\n'
                  '==============================')
            if os.path.exists('route.txt'):
                print(fn.read_data_from_file('route.txt'))
            else: 
                print('Список маршрутов пуст. Добавьте хотя бы один маршрут. Выход в главное меню через 3 секунды...')
                time.sleep(3)

        elif user_choice == '6':
            cls()
            print('==============================\n'
                  '| Добавление нового маршрута |\n'
                  '==============================')
            while True:
                fn.save_data_to_file('route.txt', input('ID маршрута(в формате route#): '), input('Введите (через пробел) номер маршрута, ID автобуса, ID водителя: '))
                choice = input('\nНажмите Enter чтобы добавить новый маршрут\nВведите 0 для выхода\n')
                if choice == '0': 
                    bus_fleet_book()

        elif user_choice == '7':
            cls()
            print('==============================\n'
                  '|    Детализация маршрута    |\n'
                  '==============================')
            fn.detalisation('route.txt')


        elif user_choice == '8':
            cls()
            print('==============================\n'
                  '|       Удаление данных      |\n'
                  '==============================')
            delete_menuitems = [("1", "- Удалить информацию по автобусам"),
                                ("2", "- Удалить информацию по водителям"),
                                ("3", "- Удалить информацию по маршрутам"),
                                ("0", "- Выход")]

            for i in delete_menuitems:
                    print(i[0], i[1])

            choice = input('Выберете категорию, где необходимо удалить данные: ')

            if choice == '1':
                cls()
                fn.delete_data('bus.txt')

            if choice == '2':
                cls()
                fn.delete_data('driver.txt')

            if choice == '3':
                cls()
                fn.delete_data('route.txt')  

        if user_choice == '0': 
            print('Выход из программы. До свидания!')
            exit()  



bus_fleet_book()