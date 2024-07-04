
def employee():
    name = get_name()
    department = get_department()
    print(f"{name} from {department}")


def get_name():
    return input("Enter name: ")


def get_department():
    return input("Enter department: ")


if __name__ == "__main__":
    employee()

class Staff:
<<<<<<< HEAD
   ...
>>>>>>> c67e38c (introduction of a class)
=======
    def __init__(self, name, department):
        self.name = ""
        self.department = ""


>>>>>>> 468cbc5 (introduction of methods)
def main():
    staff = get_staff()
    print(f"{staff.name} from {staff.department}")


def get_staff():
    name = input("Enter name: ")
    department = input("Enter department: ")
    staff = Staff(name, department)
    return staff


if __name__ == "__main__":
    main()

