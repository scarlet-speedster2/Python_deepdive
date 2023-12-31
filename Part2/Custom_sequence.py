#Silly sequence
#Just for fun a custom silly sequence

class Silly:

    def __init__(self,n):

        self.n = n

    def __getitem__(self, item):

        if item < 0 or item > self.n:
            raise IndexError
        print("get item method is called")
        return "This is the silly item"

    def __len__(self):

        print('len method called')
        return self.n


s = Silly(10)

for item in s:
    print(item)

















