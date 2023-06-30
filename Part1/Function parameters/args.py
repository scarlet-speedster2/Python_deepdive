
def fucn(a,b,*args):
    print(a,b,args)


fucn(1,2,3,5,5,"hello")

#keyword only argument

def fucn(a,b,*args,d):
    print(a,b,args,d)

fucn(1,35,2,3,3,d=2)

def avg(*args):

    count = len(args)

    return count and sum(args)/count

print(avg(1,3,5,3))

def func(a,b,c):
    print(a,b,c)

l = [1,2,3]

func(*l)
# * can be used to unpack the list to parameters
def func(a,b,c,*d):
    print(a,b,c,d)

func(1,b=2,c=5)

# we can use * to get all the keyword only arguments after this *

def func(*,a,b):
    print(a,b)

func(a=3,b=5)

