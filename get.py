
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
   ...
>>>>>>> c67e38c (introduction of a class)
def main():
    staff = get_staff()
    print(f"{staff.name} from {staff.department}")


def get_staff():
    staff = Staff()
    staff.name = input("Enter name: ")
    staff.department = input("Enter department: ")
    return staff


if __name__ == "__main__":
    main()

