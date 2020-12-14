from dir_data_structure import Directory, File


def is_dir(directory):
    return True if directory[-1] == "/" else False


def level(item):
    item_level = item[1:].count("--")
    return item_level


def file_extension(item):
    file_ext = item[1:].replace("--"*level(item), '')
    file_ext = file_ext.split(".")[-1]
    return file_ext


def item_name(item, full_name="n"):
    if item[0] == "|" and is_dir(item):
        return item[:-1].replace(f"|{'--'*level(item)}", '')
    elif item[0] == "|" and not is_dir(item):
        if "." in item and full_name == "n":
            file_name = item[1:].replace("--"*level(item), '')
            file_name = '.'.join(file_name.split(".")[:-1])
            return file_name
        elif "." in item and full_name == "y":
            return item[1:].replace("--"*level(item), '')
        else:
            return item[1:].replace("--"*level(item), '')
    else:
        return item[:-1]


def tree_structure(grandparent, parent_name, profile="basic"):
    # initialize parent
    parent = Directory(grandparent, parent_name)
    directories = {'parent': parent}

    # get tree data
    with open(f"../profiles/{profile}/tree.txt", "r") as tree_data:
        tree_list = tree_data.read().split("\n")

    # read loop
    for i in range(len(tree_list)):
        if i == 0:
            continue
        current_level = level(tree_list[i])
        j = i
        while j >= 0:
            if level(tree_list[j])+1 == current_level:
                current_parent = item_name(tree_list[j])
                child = tree_list[i]
                child_name = item_name(child)
                if is_dir(child):
                    new_dir = Directory(directories[current_parent], child_name)
                    directories[child_name] = new_dir
                elif not is_dir(child):
                    File(directories[current_parent], child_name, file_extension(child))
                break
            j -= 1
    return parent


tree_structure("E:/NIVZER/Projects/", "parent").create_all()