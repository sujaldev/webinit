from dir_data_structure import Directory, File
import os


# keep track of current directory context
# keep track of directory level

def dir_level(dir_command):
    level = dir_command[1:].count("--")
    return level


def is_dir(directory):
    if directory[-1] == "/":
        return True
    else:
        return False


def dir_name(directory):
    directory[1:-1].replace("--"*dir_level(directory), '')


def read_tree(g_parent_path, name, profile):
    parent = Directory(g_parent_path, name)
    current_dir = parent.path
    with open(f"../profiles/{profile}/tree.txt", "r") as tree_data:
        tree = tree_data.read().split("\n")
    for entry in tree:
        current_level = dir_level(entry)
        if is_dir(entry):
            parent.add_dir(dir_name(entry))
