import random
import sys
#import emoji


def showMatrix():
    return f'{matrix[0]},{matrix[1]},{matrix[2]} \n{matrix[3]},{matrix[4]},{matrix[5]} \n{matrix[6]},{matrix[7]},{matrix[8]}'
    

def checkWin():
    if matrix[0] == matrix[1] == matrix[2]:
        return(f'Победили {matrix[0]}')
        
    elif matrix[3] == matrix[4] == matrix[5]:
        return(f'Победили {matrix[3]}')
        
    elif matrix[6] == matrix[7] == matrix[8]:
        return(f'Победили {matrix[6]}')
        
    elif matrix[0] == matrix[3] == matrix[6]:
        return(f'Победили {matrix[0]}')
        
    elif matrix[1] == matrix[4] == matrix[7]:
        return(f'Победили {matrix[1]}')
        
    elif matrix[2] == matrix[5] == matrix[8]:
        return(f'Победили {matrix[2]}')
       
    elif matrix[0] == matrix[4] == matrix[8]:
        return(f'Победили {matrix[0]}')
        
    elif matrix[2] == matrix[4] == matrix[6]:
        return(f'Победили {matrix[2]}')
        
    else: return "Ваш ход"

matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]



def player(text):
    print(showMatrix())
    #while True:
    #try:
    number = int(text)
    if (matrix[number-1] != 'X') and (matrix[number-1] != 'O'):
        matrix[number-1] = 'X'
        return checkWin()
           
    else:
        return "Неверный ввод. Ячейка занята"
            
    # except:
    #     print("Неверный ввод")
        

def comp(matrix):
    for i in range(0,len(matrix)):
        if (matrix[i] != 'X') and matrix[i] != 'O':
            matrix[i] = 'O'
            return ()

# def start_game(text):

#     player(text)
#     showMatrix()
#     if checkWin() != "Ваш ход":
#         sys.exit()
#     #comp(matrix)
#     showMatrix()
#     if checkWin() != "Ваш ход":
#         sys.exit()