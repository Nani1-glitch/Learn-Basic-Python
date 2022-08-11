from os import listdir
from os.path import isfile , join
files_list = [f for f in listdir("/users") if isfile(join("/users", f))]
