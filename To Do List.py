tasks = []

def save_tasks():
    with open('tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def load_tasks():
    try:
        with open('tasks.txt', 'r' ) as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

load_tasks()
while True:
    print('--- To-Do List ---')
    print('1. Add')
    print('2. View')
    print('3. Mark Done')
    print('4. Delete')
    print('5. Quit')
    choice = input('Select an action: ')
    if choice == '5':
        print('Goodbye')
        break
    elif choice == '1':
        task = input('Enter a task: ')
        tasks.append(task)
        save_tasks()
    elif choice == '2':
        if not tasks:
            print('No tasks yet')
        else:
            for number, task in enumerate(tasks, 1):
                print(f'{number}. {task}')
    elif choice == '3':
        if not tasks:
            print('No tasks yet')
        else:
            for number, task in enumerate(tasks, 1):
                print(f'{number}. {task}')
            done = int(input('Which task number is done? '))
            tasks[done - 1] = '✓ ' + tasks[done-1]
            save_tasks()
    elif choice == '4':
        if not tasks:
            print('No tasks yet')
        else:
            for number, task in enumerate(tasks, 1):
                print(f'{number}. {task}')
            delete = int(input('Which task number should be deleted? '))
            removed = tasks.pop(delete-1)
            print(f'Deleted: {removed}')
            save_tasks()

            

    else:
        print('Invalid input. Please enter 1-5')
