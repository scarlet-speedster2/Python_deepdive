import time


def time_ct(fn,*args,rep=5,**kwargs):

    start = time.perf_counter()
    for i in range(rep):

        fn(*args,**kwargs)

    end = time.perf_counter()

    return (end - start)/rep


def compute_power(n, *, start=1, end):

    result = [n**i for i in range(start,end)]
    return result
def compute_power2(n, *, start=1, end):

    result = (n**i for i in range(start,end))
    return list(result)


print(time_ct(compute_power,2,end = 5))
print(time_ct(compute_power2,2,end = 5))


