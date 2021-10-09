
def main():

    x = 999
    _locals = locals()

    s = 'for i in range(5):\n print("i = ", i)\n'
    exec(s)

    print("-------------------")
    print(_locals)

    print("-------------------")

    exec("x = x + 1", _locals)

    print("x = x + 1 ->", _locals.get("x"))

if __name__ == '__main__':
    main()
