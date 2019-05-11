class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        path_ops = new_path.split("/")
        current_dirs = self.current_path.split("/")
        for op in path_ops:
        	if op == "..":
        		current_dirs.pop()
        	else:
        		current_dirs.append(op)
        self.current_path = "/".join(current_dirs)

path = Path('/a/b/c/d')
path.cd('../x')
print(path.current_path)


def merge(*records):
    Patient = namedtuple('Patient', records[0]._fields + records[1]._fields)
    patient = Patient(*(records[0]+records[1]))
    return patient


    