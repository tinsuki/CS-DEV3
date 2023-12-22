from memory_profiler import profile

@profile
def example():
    a = [1] * (2 ** 20)
    b = [2] * (2 * 10 ** 7)
    #del b # try to comment this line...
    return a

example()