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


def tree_to_dir_structure(grandparent, parent_name, profile="basic"):
    # create parent
    parent = Directory(grandparent, parent_name)

    # get tree data
    with open(f"../profiles/{profile}/tree.txt", "r") as tree_data:
        tree_list = tree_data.read().split("\n")

    # initialize variables
    dir_objects = {'parent': parent}

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
                if current_parent == "parent" and is_dir(child):
                    new_dir = Directory(parent, child_name)
                    dir_objects[child_name] = new_dir
                elif current_parent == "parent" and not is_dir(child):
                    File(parent, child_name, file_extension(child))
                # if is_dir(child):
                #     new_dir = Directory(dir_objects[current_parent], child_name)
                #     dir_objects[child_name] = new_dir
                # elif not is_dir(child):
                #     File(dir_objects[current_parent], child_name, file_extension(child))
                break
            j -= 1
    return parent


# tree_to_dir_structure("E:/NIVZER/Projects/web_init", "parent")
print(tree_to_dir_structure("E:/NIVZER/Projects/web_init", "parent").child_dirs)


"""

TREE                INDEX    DIR LEVEL    PARENT DIR
parent/               0         0         N/A
|--js/                1         1         parent
|----packages/        2         2         js
|------node/          3         3         packages
|----script.js        4         2         js
|--css/               5         1         parent
|----style.css        6         2         css
|--img/               7         1         parent
|--index.html         8         1         parent

 # To find parent get dir level (n) of current dir or file and then find the last dir with level n-1.
"""