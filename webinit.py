import argparse
import tree_reader as tree


def let_there_be_light(path: str, name: str, profile="basic"):
    universe = tree.make_tree(path, name, profile)
    universe.create_all()
    tree.enforce_template(universe)
    tree.enforce_variables(universe)


parser = argparse.ArgumentParser(description="Make a project directory.")
parser.add_argument('path', type=str, help='Specify path for project directory')
parser.add_argument('name', type=str, help='Specify name for project directory')
parser.add_argument('profile', type=str, help='Specify name for project directory')
args = parser.parse_args()

let_there_be_light(args.path, args.name, args.profile)