import pickle
import re
from pathlib import Path
new_clients_list = []
DATABASE_FILE = "database.pickle"


def init_database():
    global new_clients_list
    database_path = Path(DATABASE_FILE)
    if database_path.exists():
        f = open(DATABASE_FILE, "rb")
        new_clients_list = pickle.load(f)
        f.close()
    else:
        new_clients_list = []


def get_clients():
    return new_clients_list


def add_clients(*args):
    new_clients_list.append(args)
    with open(DATABASE_FILE, "wb") as f:
        pickle.dump(new_clients_list, f)


def update_clients():
    with open(DATABASE_FILE, "wb") as f:
        pickle.dump(new_clients_list, f)
