menu = []
id = 1
def add_food(name,photo,price,quan,rate):
    global id
    dct={
        'id':id,
        'name':name,
        'photo':photo,
        'price':price,
        'quan':quan,
        'rate':rate
    }
    menu.append(dct)
    id+=1
    print()
    print('new food aded sucsessifly')
    print()
    dct = {}

def get_menu():
    for i in menu:
        print('-'*30)
        print(f"""
id        --> {i['id']}
name      --> {i['name']}
photo     --> {i['photo']}
price     --> {i['price']}
quantity  --> {i['quan']}
rate      --> {i['rate']}

total     --> {i['price']*i['quan']}
""")
        print('-'*30)

def get_by_id(id):
    b=True
    for i in menu:
        if i['id'] == id:
            b=False
            print('-'*30)
            print(f"""
id        --> {i['id']}
name      --> {i['name']}
photo     --> {i['photo']}
price     --> {i['price']}
quantity  --> {i['quan']}
rate      --> {i['rate']}

total     --> {i['price'] * i['quan']}

""")
            print('-'*30)
    if b:
        print(f"id {id} not found")


def delete(id):
    b=True
    for i in menu :
        if i['id'] == id:
            b=False
            s=input(f"are u sure delet food with id {id} y/n --> ")
            if s == 'y' or s == 'yes' or s == 'Y':
                menu.remove(i)
                print()
                print(f"food with id {id} deleted sucsessufliy")
                print()

    if b:
        print(f"id {id} not found ")

def update(id):
    b=True
    for i in menu:
        if i['id'] == id:
            b=False
            m=int(input("""
1   --> update only name
2   --> update only photo
3   --> update only price
4   --> update only quantity
5   --> update only rate
6   --> update all
7   --> main menu
    what do u want to update
"""))
            if m == 1:
                name=input('enter new name for thiis food --> ')
                i['name']=name
                print(f"name of food with id {id} changed sucsessufliy ")
                update(id)
            if m == 2:
                photo=input('enter new photo for thiis food --> ')
                i['photo']=photo
                print(f"photo of food with id {id} changed sucsessufliy ")
                update(id)
            if m == 3:
                price=int(input('enter new price for thiis food --> '))
                i['price']=price
                print(f"price of food with id {id} changed sucsessufliy ")
                update(id)
            if m == 4:
                quan=int(input('enter new quantity for thiis food --> '))
                i['quan']=quan
                print(f"quantity of food with id {id} changed sucsessufliy ")
                update(id)
            if m == 5:
                rate=int(input('enter new rate for thiis food --> '))
                i['rate']=rate
                print(f"rate of food with id {id} changed sucsessufliy ")
                update(id)
            if m == 6:
                name=int(input('enter new name for thiis food --> '))
                i['name']=name

                photo=input('enter new photo for thiis food --> ')
                i['photo']=photo

                price=int(input('enter new price for thiis food --> '))
                i['price']=price

                quan=int(input('enter new quantity for thiis food --> '))
                i['quan']=quan

                rate=int(input('enter new rate for thiis food --> '))
                i['rate']=rate

                print(f"food with id {id} changed sucsessifuly")
                update(id)
            if m == 7:
                return 0
    if b:
        print(f'id {id} not found ')

def max_price():
    mx = menu[0]
    for i in menu:
        if i['price'] > mx['price']:
            mx = i
    print()
    print('-'*30)
    print(f"""
          Max price food for menu

id        --> {mx['id']}
name      --> {mx['name']}
price     --> {mx['price']}
""")
    print('-'*30)

def min_price():
    mn = menu[0]
    for i in menu:
        if i['price'] < mn['price']:
            mn = i
    print()
    print('-'*30)
    print(f"""
          Min price food for menu

id        --> {mn['id']}
name      --> {mn['name']}
price     --> {mn['price']}
""")
    print('-'*30)


def max_quan():
    mx = menu[0]
    for i in menu:
        if i['quan'] > mx['quan']:
            mx = i
    print()
    print('-'*30)
    print(f"""
          Max quantity food for menu
          
id        --> {mx['id']}
name      --> {mx['name']}
quantity  --> {mx['quan']}
""")
    print('-'*30)

def min_quan():
    mn = menu[0]
    for i in menu:
        if i['quan'] < mn['quan']:
            mn = i
    print()
    print('-'*30)
    print(f"""
          Min quantity food for menu

id        --> {mn['id']}
name      --> {mn['name']}
quantity  --> {mn['quan']}
""")
    print('-'*30)

def max_tot():
    mx = menu[0]
    for i in menu:
        if i['price'] * i['quan'] > mx['price'] * mx['quan']:
            mx = i
    print()
    print('-'*30)
    print(f"""
          Max total food from menu

id        --> {mx['id']}
name      --> {mx['name']}
total     --> {mx['price'] * mx['quan']}
""")
    print('-'*30)

def min_tot():
    mn = menu[0]
    for i in menu:
        if i['price'] * i['quan'] > mn['price'] * mn['quan']:
            mn = i
    print()
    print('-'*30)
    print(f"""
          Min total food from menu

id        --> {mn['id']}
name      --> {mn['name']}
total     --> {mn['price'] * mn['quan']}
""")
    print('-'*30)




while True:
    n = int(input("""
1   --> add new food
2   --> get all menu
3   --> get by id
4   --> delete food by id
5   --> update food by id
6   --> max price
7   --> min price
8   --> max quantity
9  --> min quantity
10  --> max total
11  --> min total
12   --> exit
                  
choose your option  --> """))
    if n == 1:
        print()
        add_food(input('enter name of food --> '),
                 input('enter photo of food --> '),
                 int(input('enter price of food --> ')),
                 int(input('enter quantitiy of food --> ')),
                 int(input('enter rate of food --> ')),)
        print()
    if n == 2:
        get_menu()
    if n == 3:
        get_by_id(int(input('enter id  --> ')))
    if n == 4:
        delete(int(input('enter id for delete ')))
    if n == 5:
        update(int(input('enter id for apdate ')))
    if n == 6:
        max_price()
    if n == 7:
        min_price()
    if n == 8:
        max_quan()
    if n == 9:
        min_quan()
    if n == 10:
        max_tot()
    if n == 11:
        min_tot()
    if n == 12:
        s=input(f"are u sure delet food with id {id} y/n --> ")
        if s == 'y' or s == 'yes' or s == 'Y':
            break