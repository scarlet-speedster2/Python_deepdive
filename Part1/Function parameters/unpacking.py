l = [1,2,3,4]
print(l[0])
print(l[1:])

a, *b = l
print(a,b)
a, *b = 1, 3, 5, "hello"
print(a,b)
s = "python"

a, b, *c, d = s
print(a,b,c,d)
l1 = [1,2,3]
l2 = [4,5,6]
print([*l1,*l2])
print((*l1,*l2))
s = "abc"
print([*l1,*s])

#it can be used to concatinate two sets cause + wont work with the sets

s1 = {1,2,3}
s2 = {4,5,6}

print({*s1,*s2})

#dict
d1 = {'key1':1,'key2':2}
d2 = {'key2':3,'key4':4}
print([*d1,*d2])

#to make a dictionary with **argument
#it will override the latated key in case of the repetations

d3 = {**d1,**d2}
print(d3)

l =  [1,2,3,'python']

a,*c,(e,f,*g)  = l
print(a,c,e,f,g)

#equivalent slicing

a,c,e,f,g = l[0],l[1:-1],l[-1][0],l[-1][1],l[-1][2:]
print(a,c,e,f,g)

