import sys
import datetime

from users_data import USERS
from database import add_clients, init_database, get_clients, update_clients

init_database()
new_users = {'name': '', 'PIN': 0, 'Balance': 0, 'Status': '', 'Block_time': ''}
user_name_input = input('Enter your username: ')


def withdraw():
    global balance
    get_clients()
    client_check_name = [user for user in USERS if user['name'] == user_name_input]
    new_client_check_name = [new_user for new_user in get_clients() if new_user[0]['name'] == user_name_input]
    for balance in client_check_name:
        client_balance = balance['Balance']
    for new_balance in new_client_check_name:
        new_client_balance = new_balance[0]['Balance']
    if client_check_name:
        print(f'Balance: {client_balance} BGN')
    else:
        print(f'Balance: {new_client_balance} BGN')
    print('How much do you wish to withdraw?')
    withdraw_input = int(input())
    if client_check_name:
        client_new_balance = client_balance - withdraw_input
        if client_new_balance < 0:
            print('You do not have enough money in your account.')
        else:
            print(f'Your new balance is: {client_new_balance} BGN')
    elif new_client_check_name:
        new_client_new_balance = new_client_balance - withdraw_input
        if new_client_new_balance < 0:
            print('You do not have enough money in your account.')
        else:
            print(f'Your new balance is: {new_client_new_balance} BGN')
            new_client_check_name[0][0]['Balance'] -= withdraw_input
            update_clients()
    u_actions = int(input('Determine your action (1/2/3):\n1. Withdraw (1)\n2. Deposit (2)\n3. \
Balance (3)\n4. Exit (4)\n'))
    if u_actions == 1:
        withdraw()
    elif u_actions == 2:
        deposit()
    elif u_actions == 3:
        balance()
    else:
        sys.exit()


def deposit():
    global balance
    get_clients()
    client_check_name = [user for user in USERS if user['name'] == user_name_input]
    new_client_check_name = [new_user for new_user in get_clients() if new_user[0]['name'] == user_name_input]
    for balance in client_check_name:
        client_balance = balance['Balance']
    for new_balance in new_client_check_name:
        new_client_balance = new_balance[0]['Balance']
    if client_check_name:
        print(f'Balance: {client_balance} BGN')
    else:
        print(f'Balance: {new_client_balance} BGN')
    print('How much do you wish to deposit?')
    deposit_input = int(input())
    if client_check_name:
        client_new_balance = client_balance + deposit_input
        print(f'Your new balance is: {client_new_balance} BGN')
    elif new_client_check_name:
        new_client_new_balance = new_client_balance + deposit_input
        print(f'Your new balance is: {new_client_new_balance} BGN')
        new_client_check_name[0][0]['Balance'] += deposit_input
        update_clients()
    u_actions = int(input('Determine your action (1/2/3):\n1. Withdraw (1)\n2. Deposit (2)\n3. \
Balance (3)\n4. Exit (4)\n'))
    if u_actions == 1:
        withdraw()
    elif u_actions == 2:
        deposit()
    elif u_actions == 3:
        balance()
    else:
        sys.exit()


def balance():
    global balance
    get_clients()
    client_check_name = [user for user in USERS if user['name'] == user_name_input]
    new_client_check_name = [new_user for new_user in get_clients() if new_user[0]['name'] == user_name_input]
    for balance in client_check_name:
        client_balance = balance['Balance']
    for new_balance in new_client_check_name:
        new_client_balance = new_balance[0]['Balance']
    if client_check_name:
        print(f'Your current balance is: {client_balance} BGN')
    elif new_client_check_name:
        print(f'Your current balance is: {new_client_balance} BGN')
    u_actions = int(input('Determine your action (1/2/3):\n1. Withdraw (1)\n2. Deposit (2)\n3. \
Balance (3)\n4. Exit (4)\n'))
    if u_actions == 1:
        withdraw()
    elif u_actions == 2:
        deposit()
    elif u_actions == 3:
        balance()
    else:
        print('You have logged out.')
        sys.exit()


def block_card():
    get_clients()
    new_client_check_name = [new_user for new_user in get_clients() if new_user[0]['name'] == user_name_input]
    if new_client_check_name:
        new_client_check_name[0][0]['Status'] = 'Blocked'
        time = datetime.datetime.now()
        blocked_time = time.strftime('%m/%d/%Y, %H:%M:%S')
        new_client_check_name[0][0]['Block_time'] = blocked_time
        update_clients()


def unblock_card():
    get_clients()
    new_client_check_name = [new_user for new_user in get_clients() if new_user[0]['name'] == user_name_input]
    if new_client_check_name:
        if new_client_check_name[0][0]['Status'] == 'Blocked':
            time = datetime.datetime.now()
            unblocked_time = time.strftime('%m/%d/%Y, %H:%M:%S')
            blocked_time = new_client_check_name[0][0]['Block_time']
            unblocked_time_int = datetime.datetime.strptime(unblocked_time, '%m/%d/%Y, %H:%M:%S')
            blocked_time_int = datetime.datetime.strptime(blocked_time, '%m/%d/%Y, %H:%M:%S')
            difference = (unblocked_time_int - blocked_time_int).total_seconds() / 60.0
            if difference >= 5.0:
                new_client_check_name[0][0]['Status'] = 'Active'
            update_clients()


def client_entry():
    get_clients()
    client_check_name = [user for user in USERS if user['name'] == user_name_input]
    new_client_check_name = [new_user for new_user in get_clients() if new_user[0]['name'] == user_name_input]
    unblock_card()
    if not client_check_name and not new_client_check_name:
        print('No such username.\nDo you want to create a new profile?')
        new_profile = input('(Y/N)')
        if new_profile.upper() == "Y":
            new_profile_username = input('Username:')
            try:
                new_profile_pin = int(input('PIN: '))
                new_profile_pin_2 = int(input('Confirm your PIN code: '))
                if new_profile_pin_2 != new_profile_pin:
                    print('Your PIN codes do not match.')
                    new_profile_pin_3 = int(input('Please try again:'))
                    if new_profile_pin_3 != new_profile_pin:
                        print('Your PIN codes do not match. System has restarted.')
                        sys.exit()
            except ValueError:
                print("Invalid PIN. Must use only digits. Session ended.")
                sys.exit()
            else:
                try:
                    new_profile_balance = int(input('Starting balance: '))
                except ValueError:
                    print('Invalid entry. Must use only digits. Session ended.')
                    sys.exit()
            new_users['name'] += new_profile_username
            new_users['PIN'] += new_profile_pin
            new_users['Balance'] += new_profile_balance
            new_users['Status'] = 'Active'
            add_clients(new_users)
            print(new_users)
            print('User created.')
            sys.exit()

        else:
            print("Your session has expired.")
            sys.exit()
    if new_client_check_name[0][0]['Status'] == 'Blocked':
        print('Your account is temporary blocked. Try again later.')
        sys.exit()
    cc = 1
    while True:
        try:
            user_pin_input = int(input('Enter your PIN: '))
            client_check_pin = [pin for pin in USERS if pin['PIN'] == user_pin_input]
            new_client_check_pin = [new_pin for new_pin in get_clients() if new_pin[0]['PIN'] == user_pin_input]
            if not client_check_pin and not new_client_check_pin:
                print("Your PIN is incorrect.")
                cc += 1
            if cc == 4:
                print("Your card has been temporary blocked.")
                block_card()
                sys.exit()
            elif client_check_pin or new_client_check_pin:
                break
        except ValueError:
            print("Your PIN code must contain only digits. Session ended.")
            sys.exit()
    u_actions = int(input('Determine your action (1/2/3):\n1. Withdraw (1)\n2. Deposit (2)\n3. \
Balance (3)\n4. Exit (4)\n'))
    if u_actions == 1:
        withdraw()
    elif u_actions == 2:
        deposit()
    elif u_actions == 3:
        balance()
    else:
        print('You have logged out.')
        sys.exit()


client_entry()

