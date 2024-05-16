from app.views import update_user_pro,delete_user_pro


def menu():
    print('Add User    => 1')
    print('Update User => 2')
    print('Delete User => 3')
    print('Read User   => 4')
    print('Quit        => q')
    return input('?:')


def run():
    while True:
        choice = menu()
        if choice == '1':
            pass
            # user_create_pro(user:User)
        elif choice == '2':
            update_user_pro()

        elif choice == '3':
            delete_user_pro()
        elif choice == 'q':
            break


if __name__ == '__main__':
    run()