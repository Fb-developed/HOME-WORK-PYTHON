all_list = []
id = 1
while True:
    n = int(input("""
            chose your option -->

            1  --> Add a new task
            2  --> View all task
            3  --> update task info
            4  --> delete task info
            5  --> exit
                                
                    """))
    if n == 1:
        dict1 = {}
        task = input("Enter task name --> ")
        time = input('enter task time --> ')
        user = input('enter task user --> ')
        during = input('enter task during --> ')
        dict1 = {
            'id':id,
            'task':task,
            'time':time,
            'user':user,
            'during':during
        }
        id+=1
        all_list.append(dict1)
        print('-'*20)
        print('new task added successfully ')
    if n == 2:
        for i in all_list:
            print(f"""
id      --> {i['id']}
task    --> {i['task']}
time    --> {i['time']}
user    --> {i['user']}
during  --> {i['during']}
""")


    if n == 3:
        b=True
        id=int(input('enter id of task for update --> '))
        for i in all_list:
            if i['id'] == id:
                b=False
                ntask = input('enter new task for task --> ')
                ntime = input('enter new time for task --> ')
                nuser = input('enter new user for task --> ')
                nduring = input('enter new during for task --> ')
                i['task'] = ntask
                i['time'] = ntime
                i['user'] = nuser
                i['during'] = nduring
                print()
                print(f"task with id {id} updated successfully")
        if b:
            print( 'id ', id, 'not found ')

    if n == 4:
        b=True
        id = int(input('enter id of task for delete --> '))
        for i in all_list:
            if i['id'] == id:
                b=False
                all_list.remove(i)
                print()
                print(f"task with id {id} deleted successfully")
        if b:
            print('id ', id, 'not found')
    if n == 5:
        l=input('are you sure you want to exit? y/n ')
        if l == 'y' or l == 'Y' or l == 'yes' or l == 'YES':
            print('thank you for using this program')
            break
        else:
            continue