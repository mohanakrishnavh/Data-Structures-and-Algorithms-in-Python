# Representing a tree as list of lists
def binary_tree(r):
    return [r, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, value):
    root[0] = value


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


'''
r = binary_tree(10)
print(r)
insert_left(r, 4)
print(r)
insert_right(r, 5)
insert_left(r, 3)
print(r)
insert_right(r, 7)
print(r)

l = get_left_child(r)
print(l)
r = get_right_child(r)
print(r)
'''
