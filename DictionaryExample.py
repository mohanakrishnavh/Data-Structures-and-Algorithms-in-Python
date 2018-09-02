# Example of dictionary
class DictClass:
    def __init__(self):
        self.data = 0


obj = DictClass()

d = dict()
d['object'] = obj
d[1] = True
d['1'] = False

print(d['object'].data)
print(d)
