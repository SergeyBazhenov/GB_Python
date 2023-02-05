# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной


import os
import time

def cls():
    os.system('cls')
cls()    


def rewrite_data(result, answer, line, contact_id, file_name):
    new_data = input("Введите новое значение: ")
    result[answer - 1] = new_data
    result[len(result) - 1] += '\n'
    line[contact_id - 1] = ' '.join(result)
    with open (file_name, 'w', encoding = 'utf-8') as data:
        for i in line:
            data.write(i)

fileName = 'Phonebook.txt'

def writeFile (file_name):
    cls()
    print('==============================\n'
          '| Добавление нового контакта |\n'
          '==============================')
    while True:
        with open (file_name, 'a', encoding = 'utf-8') as data:
            last_name = input('Фамилия: ')
            first_name = input('Имя: ')
            patronymic = input('Отчество: ')
            phone_number = input('Номер телефона: ')
            data.writelines(f'{last_name} {first_name} {patronymic} {phone_number}\n')
            choice = input('\nНажмите Enter чтобы добавить новый контакт\nВведите 0 для выхода\n')
            if choice == '0': 
                return 
        
def readFile (file_name):
    cls()
    print('==============================\n'
          '|      Список контактов      |\n'
          '==============================')
    while True:
        with open(file_name, 'r', encoding = 'utf-8') as data:
            line = data.readlines()
            
        for i in line:
            i = line.index(i)
            print(f'{i+1}. {line[i].strip()}')
        choice = input('\nНажмите 0 для выхода\n')
        if choice == '0': 
            return
    
def findContactByKeyWord (file_name):
    cls()
    print('==============================\n'
          '|       Поиск контакта       |\n'
          '==============================')
    while True:
        key_word = input('Введите ФИО или номер телефона для поиска: ').casefold()
        
        with open(file_name, 'r', encoding = 'utf-8') as data:
            count = 0
            for line in data:
                if key_word in line.casefold(): 
                    print(line)
                    count += 1
            if count == 0: print('Контакт не найден.')
            else: print(f'Найдено контактов: {count}')    
        choice = input('\nНажмите Enter для продолжения или 0 для выхода\n')
        if choice == '0': 
            return
        

def DeleteContact(file_name):
    cls()
    print('==============================\n'
          '|      Удаление контакта     |\n'
          '==============================')             
    while True:
        with open(file_name, 'r', encoding = 'utf-8') as data:
            line = data.readlines()
        
        for i in line:
            i = line.index(i)
            print(f'{i+1}. {line[i].strip()}')
        
        deleted_str = int(input('Введите порядковый номер контакта, который хотите удалить: '))
        del line[deleted_str - 1]
        
        with open (file_name, 'w', encoding = 'utf-8') as data:
            for i in line:
                data.write(i)
        choice = input('\nНажмите Enter, чтобы продолжить удаление контактов\nВведите 0 для выхода\n')
        if choice == '0': 
            return   
        
def ReplaceData(file_name):
    cls()
    print('==============================\n'
          '|      Изменение данных      |\n'
          '==============================')             
    while True:
        with open(file_name, 'r', encoding = 'utf-8') as data:
            line = data.readlines()
            
        for i in line:
            i = line.index(i)
            print(f'{i+1}. {line[i].strip()}')

        contact_id = int(input('Введите порядковый номер контакта: '))
        result = line[contact_id - 1].split()

        answer = int(input('Какие данные хотите изменить?\n'
                        '1 - Фамиля\n'
                        '2 - Имя\n'
                        '3 - Отчество\n'
                        '4 - Номер телефона\n'
                        '0 - для выхода\n'))
        
        
        if (answer == 1) or (answer == 2) or (answer == 3) or (answer == 4):
            rewrite_data(result, answer, line, contact_id, fileName)
                    
        choice = input('\nНажмите Enter, чтобы продолжить изменение контактов\nВведите 0 для выхода\n')
        if choice == '0': 
            return


def main_menu():
    cls()
    print('===================================\n'
          '|      Телефонный справочник      |\n'
          '===================================\n'
          '|           Главное меню          |\n'
          '===================================')
 
    print('1 - Показать все записи\n'
          '2 - Найти запись по ФИО или номеру телефона\n'
          '3 - Добавить новый контакт\n'
          '4 - Удалить контакт\n'
          '5 - Изменить данные контакта\n'
          '0 - Выход')

def Phonebook():
    while True:
        main_menu()
        user_choice = int(input('Выберете необходимый пункт меню: '))
                
        if user_choice == 1:
            if os.path.exists(fileName):
            #Показать все записи
                readFile(fileName)
            else: 
                print('Контакты отсутствуют. Создайте хотя бы один контакт. Выход в главное меню через 3 секунды...')
                time.sleep(3)  
    
               
            

        if user_choice == 2: 
            #Найти запись по фио или номеру
            findContactByKeyWord(fileName)
                

        if user_choice == 3: 
            #Добавить новый контакт
            writeFile(fileName)
            

        if user_choice == 4: 
            #Удалить контакт
            DeleteContact(fileName)
               

        if user_choice == 5: 
            #Изменить данные у контакта
            ReplaceData(fileName)
            

        if user_choice == 0: 
            print('Выход из программы. До свидания!')
            break    


Phonebook() 