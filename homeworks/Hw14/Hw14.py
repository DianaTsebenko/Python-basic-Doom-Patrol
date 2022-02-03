import argparse
import json


def new_file():
    file = open("user_info.json", 'w')
    file.write(json.dumps([]))
    file.close()
    return open("user_info.json", 'r')


def user_add(users):
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--username", help="person_username")
    parser.add_argument("-e", "--email", help="person_email")
    parser.add_argument("-s", "--status", help="person_status")
    args = parser.parse_args()

    try:
        users['username'] = args.username
        users['email'] = args.email
        users['status'] = args.status
    except IndexError:
        raise Exception('U wrote wrong person info')


def check_user_exists(user_info, user):
    for users in user_info:
        if user['username'] == users['username'] or \
                user['email'] == users['email']:
            return True

    return False


def add_user(user):
    try:
        read_file = open('user_info.json', 'r')
    except FileNotFoundError:
        read_file = new_file()

    try:
        user_info = json.loads(read_file.read())
    except ValueError:
        with open('user_info.json', "w") as write_file:
            write_file.write(json.dumps([]))
        user_info = []
    read_file.close()

    if not check_user_exists(user_info, user):
        user_info.append(user)
        with open('user_info.json', 'w') as write_file:
            write_file.write(json.dumps(user_info, indent=4, sort_keys=True))
    else:
        raise "User with username or email already exist"


if __name__ == "__main__":
    new_user = {}
    user_add(new_user)
    add_user(new_user)
