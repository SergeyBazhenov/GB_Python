import os

def read_data_from_file(file_name):
    while True:
        with open(file_name, 'r', encoding = 'utf-8') as data:
            line = data.readlines()
            
        for i in line:
            i = line.index(i)
            print(f'{i+1}. {line[i].strip()}')
        choice = input('\nНажмите 0 для выхода\n')
        if choice == '0': 
            return


def save_data_to_file(file_name, id, add_info):
    
        with open (file_name, 'a+', encoding = 'utf-8') as data:
            data.writelines(f'{id} {add_info}\n')
             

def detalisation(file_name):
    while True:
        with open(file_name, 'r', encoding = 'utf-8') as data:
            line = data.readlines()
                
            for i in line:
                i = line.index(i)
                print(f'{i+1}. {line[i].strip()}')

        route_id = int(input('Введите ID маршрута: '))
        os.system('cls')
        
        print(f'Выбран маршрут: {line[route_id - 1]}')

        print(f'Номер маршрута: {line[route_id - 1].split()[1]}\n')

        bus_id = line[route_id - 1].split()[2]
        driver_id = line[route_id - 1].split()[3] 

        with open('bus.txt', 'r', encoding = 'utf-8') as data:
            count = 0
            for line in data:
                if bus_id == line.split()[0]: 
                    print(f'ID автобуса: {line.split()[0]}\nГосномер автобуса: {line.split()[1]}\n')
                    count += 1
            if count == 0: print(f'Автобус {bus_id} ещё не добавлен в справочник. Создайте новую запись.')

        
        with open('driver.txt', 'r', encoding = 'utf-8') as data:
            count = 0
            for line in data:
                if driver_id == line.split()[0]: 
                    print(f'ID водителя: {line.split()[0]}\nФИО водителя: {line.split()[1]} {line.split()[2]} {line.split()[3]}')
                    count += 1
            if count == 0: print(f'Водитель {driver_id} ещё не добавлен в справочник. Создайте новую запись.')
        choice = input('\nНажмите 0 для выхода\n')
        if choice == '0': 
            return


def delete_data(file_name):
    while True:
        with open(file_name, 'r', encoding = 'utf-8') as data:
            line = data.readlines()
        
        for i in line:
            i = line.index(i)
            print(f'{i+1}. {line[i].strip()}')
        
        deleted_str = int(input('Введите порядковый номер строки, которую хотите удалить: '))
        del line[deleted_str - 1]
        
        with open (file_name, 'w', encoding = 'utf-8') as data:
            for i in line:
                data.write(i)
        choice = input('\nНажмите Enter, чтобы продолжить удаление\nВведите 0 для выхода\n')
        if choice == '0': 
            return 