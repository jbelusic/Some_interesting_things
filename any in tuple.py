
def main():
    user_input = "MAX1236"
    commands = ("KOD",
                "HELP",
                "RESET",
                "TEST",
                "SVI",
                "TEMP",
                "DODATNI",
                "MAX",
                "MIN",
                "MASTER",
                "INFO")
    if any(user_input.startswith(s) for s in commands):
        print("yeeee")
    else:
        print("noooo")

if __name__ == '__main__':
    main()
