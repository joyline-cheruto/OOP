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
