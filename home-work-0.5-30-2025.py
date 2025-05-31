from datetime import datetime
import random
from colorama import init, Fore

init(autoreset=True)

def registration(name, surname, age, creat_date, last_update, username, password):
    pass1 = input(Fore.YELLOW + 'enter your password again --> ')
    if pass1 != password:
        print(Fore.RED + 'wrong password')
        return 0
    with open('file.txt', 'a') as file:
        file.write(f'{name}/{surname}/{age}/{creat_date}/{last_update}/{username}/{password}/\n')
        print(Fore.GREEN + '='*50)
        print(Fore.GREEN + 'you registered successfully! Now you can log in!')
        print(Fore.GREEN + '='*50)

def login(username, password):
    with open('file.txt', 'r') as file:
        lines = file.readlines()
    for ents in lines:
        lst1 = ents.split('/')
        if lst1[5] == username and lst1[6] == password:
            print(Fore.GREEN + '='*50)
            print(Fore.GREEN + 'You logged in successfully')
            print(Fore.GREEN + '='*50)
            while True:
                print(Fore.CYAN + f'''
             Hello {lst1[5]}
Your name         -->  {lst1[0]}
Your surname      -->  {lst1[1]}
Your age          -->  {lst1[2]}
Your reg. date    -->  {lst1[3]}
Last updated      -->  {lst1[4]}
''')
                x = int(input(Fore.YELLOW + '''
What do you want to do?
1 --> update
2 --> logout
3 --> delete account
'''))
                if x == 1:
                    name = input('enter new name --> ')
                    surname = input('enter new surname --> ')
                    age = input('enter new age --> ')
                    last = datetime.now()
                    lst1[0] = name
                    lst1[1] = surname
                    lst1[2] = age
                    lst1[4] = str(last)
                    lines.remove(ents)
                    ents = '/'.join(lst1)
                    lines.append(ents)
                    with open('file.txt', 'w') as file:
                        file.writelines(lines)
                    print(Fore.GREEN + '='*50)
                    print(Fore.GREEN + 'your account updated successfully')
                    print(Fore.GREEN + '='*50)
                if x == 2:
                    print(Fore.BLUE + '='*30)
                    print(Fore.BLUE + 'you logged out')
                    print(Fore.BLUE + '='*30)
                    return 0
                if x == 3:
                    passw = input('enter your password --> ')
                    if passw == password:
                        lines.remove(ents)
                        with open('file.txt', 'w') as file:
                            file.writelines(lines)
                        print(Fore.RED + '='*30)
                        print(Fore.RED + 'your account was deleted forever')
                        print(Fore.RED + '='*30)
                        return 1
                    else:
                        print(Fore.RED + 'wrong password')
        else:
            print(Fore.RED + 'wrong username or password')

def forgot_password(username):
    n = str(random.randint(1000, 9999))
    with open('password.txt', 'w+') as file:
        file.write(n)
    ps = input(Fore.YELLOW + 'enter 4-digit password from password.txt  --> ')
    if n == ps:
        with open('file.txt', 'r') as file:
            lines = file.readlines()
        for ents in lines:
            lst1 = ents.split('/')
            if lst1[5] == username:
                new_pass = input('enter new password --> ')
                new_pass2 = input('enter new password again --> ')
                if new_pass == new_pass2:
                    lst1[6] = new_pass
                    lines.remove(ents)
                    ents = '/'.join(lst1)
                    lines.append(ents)
                    with open('file.txt', 'w') as file:
                        file.writelines(lines)
                    print(Fore.GREEN + 'your password was changed successfully')
                    return 'salom'
                print(Fore.RED + 'passwords are not equal')
            print(Fore.RED + 'user not found')
            return "salom"

while True:
    try:
        n = int(input(Fore.MAGENTA + """
choose your option  
1 --> registration
2 --> login 
3 --> forgot password
-------->   """))
        if n == 1:
            registration(
                input('enter your name     --> '),
                input('enter your surname  --> '),
                input('enter your age      --> '),
                datetime.now(),
                datetime.now(),
                input('enter your username --> '),
                input('enter your password --> ')
            )
        if n == 2:
            login(
                input('enter your username --> '),
                input('enter your password --> ')
            )
        if n == 3:
            forgot_password(input('enter your username --> '))
    except Exception as ex:
        print(ex)
