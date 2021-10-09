#Python List Append vs Extend

#append: Appends object at the end.

x = [1, 2, 3]
x.append([4, 5])
print (x)
#gives you: [1, 2, 3, [4, 5]]

#extend: Extends list by appending elements from the iterable.

x = [1, 2, 3]
x.extend([4, 5])
print (x)
#gives you: [1, 2, 3, 4, 5]

################################

li = ['a', 'b', 'mpilgrim', 'z', 'example']
li.append("new")
#['a', 'b', 'mpilgrim', 'z', 'example', 'new']

li.append(["new", 2])
#['a', 'b', 'mpilgrim', 'z', 'example', 'new', ['new', 2]]

li.insert(2, "new")
#['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', ['new', 2]]

li.extend(["two", "elements"])
#['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', ['new', 2], 'two', 'elements']