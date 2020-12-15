import tree_reader as tree


def let_there_be_light(path: str, name: str):
    universe = tree.make_tree(path, name)
    universe.create_all()
    tree.enforce_template(universe)
    tree.enforce_variables(universe)
