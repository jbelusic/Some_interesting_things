
def a1():
    return "This returns A"
    
def b1():
    return "This returns B"
    
def main():
    a = a1()
    b = b1()

    print("Start")

    d = {"A":a, "B":b}

    x = "A"
    print(d[x])

if __name__ == '__main__':
    main()
