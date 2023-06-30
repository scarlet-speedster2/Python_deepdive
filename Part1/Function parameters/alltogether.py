
def func(a,b,*c):
    print(a,b,c)


func(1,3,4,4,3,2)
#we cannot call the function this way
#func(a=1,b=3,2)
#keyword only arguments

def func(*,a,b):
    print(a,b)

func(a= 3,b= 5)

def func(a, b, *, c=5, d):
    print(a,b,c,d)

func(1, c = 7, d = 11, b= 1)