import os


class Directory:
    def __init__(self, parent, name, direct="y"):
        self.name = name
        self.direct = direct
        self.child_dirs = {}
        self.files = {}
        if type(parent) == Directory and self.direct == "y":
            self.parent = parent
            self.parent.add_dir(self.name)
            self.parent = parent.path
        else:
            self.parent = parent
        self.path = f"{self.parent}/{self.name}"

    def add_dir(self, dir_name):
        self.child_dirs[dir_name] = Directory(self, dir_name, "n")

    def add_dirs(self, dir_list):
        for directory in dir_list:
            self.child_dirs[directory] = Directory(self, directory)

    def add_file(self, f_name, f_extension):
        self.files[f_name] = File(self, f_name, f_extension, "n")

    def add_files(self, file_dict):
        for file in file_dict:
            self.files[file[0]] = File(self, file[0], file[1])

    def make_files(self):
        for file in self.files.values():
            file.make_file()

    def create_all(self):
        os.mkdir(self.path)
        self.make_files()
        for directory in self.child_dirs.values():
            directory.create_all()


class File:
    def __init__(self, file_parent, file_name, file_extension, direct="y"):
        self.file_parent = file_parent
        self.file_name = file_name
        self.file_extension = file_extension
        self.direct = direct
        if self.direct == "y":
            self.file_parent.add_file(self.file_name, self.file_extension)
        self.file_parent = file_parent.path
        self.path = f"{self.file_parent}/{self.file_name}.{self.file_extension}"

    def make_file(self):
        open(self.path, 'w').close()
