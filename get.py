def main():
    name, department = staff()
    print(f"{name} from {department}")


def staff():
    name = input("Enter name: ")
    department = input("Enter department: ")
    return name, department


if __name__ == "__main__":
    main()
