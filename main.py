def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except (ValueError, IndexError, KeyError) as e:
            print(f"Error: {e}")
            return None
    return wrapper


@input_error
def handle_add_command(users, entering):
    _, key, value = entering.split(maxsplit=2)
    users[key] = value
    return 'Saved'


@input_error
def handle_change_command(users, entering):
    _, key, value = entering.split(maxsplit=2)
    if key in users:
        users[key] = value
        return 'Saved'
    else:
        return f'User {key} not found'


@input_error
def handle_phone_command(users, entering):
    _, key = entering.split(maxsplit=1)
    if key in users:
        return users[key]
    else:
        return f'Phone number for {key} not found'


@input_error
def handle_show_all_command(users):
    if users:
        return "\n".join([f'{key}: {value}' for key, value in users.items()])
    else:
        return 'No users found'


def main():
    users = {}
    commands = {
        "add": handle_add_command,
        "change": handle_change_command,
        "phone": handle_phone_command,
        "show all": handle_show_all_command,
    }
    
    bye_list = ["good bye", "close", "exit", "."]
    
    while True:
        inputting = input('> ')
        entering = inputting.lower()
        
        if entering == 'hello':
            print('How can I help you?')
        elif entering.startswith("add"):
            print(commands["add"](users, entering))
        elif entering.startswith("change"):
            print(commands["change"](users, entering))
        elif entering.startswith("phone"):
            print(commands["phone"](users, entering))
        elif entering == "show all":
            print(commands["show all"](users))
        elif entering in bye_list:
            print("Good bye!")
            break
        else:
            print("Command not recognized.")


if __name__ == '__main__':
    main()
