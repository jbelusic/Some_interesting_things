def test_sum():
    assert sum([1, 2, 3, 4]) == 6, "Should be 6"
    assert sum([1, 2, 3, 5]) == 6, "Never get this"

if __name__ == "__main__":
    try:
        test_sum()
    except AssertionError:
        print("Error")
    test_sum()
    print("Everything passed")


import sys
print(sys.platform)
print(1)
assert('linux' in sys.platform), "This run on linux"
print(2)
