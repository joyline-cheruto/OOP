
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
=======
def main():
    name, department = staff()
    print(f"{name} from {department}")


def staff():
    name = input("Enter name: ")
    department = input("Enter department: ")
    return name, department


if __name__ == "__main__":
    main()

