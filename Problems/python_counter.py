count = 0 
def make_counter():
    # count = 0 
    def counter1():
        # nonlocal count
        count += 1
        return count 
    def counter2():
        # nonlocal count
        count += 1 
        return count 
    return counter1, counter2

c1, c2 = make_counter()
print(c1())
print(c2()) 