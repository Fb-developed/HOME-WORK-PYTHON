from colorama import Fore, Style, init
init(autoreset=True)

def add(n):
    with open('text.txt','a') as file:
        file.write(n+'\n')






def get():
    with open('text.txt','r+') as file:
        print(Fore.CYAN +file.read())






def update(n,new):
    with open('text.txt','r') as file:
       t =  file.readlines()
       for i in range(len(t)):
            if i == n-1:
                t[i] =new+'\n'
    with open('text.txt','w') as file:
        file.writelines(t)






def delete(n):
    with open('text.txt','r') as file:
       t =  file.readlines()
       for i in range(len(t)):
            if i == n-1:
                t[i]= '\n'
    with open('text.txt','w') as file:
        file.writelines(t)







while True:
    print('''
                        1 add string
                        2 get file
                        3 update sting
                        4 delete string  
                        5 exit       
    ''')
    try:
        f = int(input('Choce your option (1-5) '))
    except ValueError:
                print('Eror input!')
                continue
    if f == 1:
        try:
            add(input('enter string for add to file '))
            print('-'*30)
            print(Fore.GREEN + 'aded string sucsessufily')
            print('-'*30)
        except ValueError:
                print('Eror input!')
    if f == 2:
        get()
    if f == 3:
        try:   
            n = int(input('enter line for update '))
            new = input('enter new string ')     
            update(n,new)
            print('-'*30)
            print(Fore.GREEN + f'update line {n} sucsessufily ')
            print('-'*30)
        except ValueError:
                print('Eror input!')
    if f == 4:
        try:
            n = int(input('enter line for deleted '))
            delete(n)
            print('-'*30)
            print(Fore.GREEN + f'deleted line {n} sucsessufily')
            print('-'*30)
        except ValueError:
                print('Eror input!')
    if f == 5:
        print('confirm for exit yes/no')
        t = input('enter yes or no ')
        if t == 'yes':
            break
        else:
            continue
