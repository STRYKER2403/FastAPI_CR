def add(firstName : str | list[int,int,str], lastName : str = None):
    firstName.capitalize()
    # for item in firstName:
    #     item.
    return firstName + " " + lastName


fname = "swapnil"
lname = "Srivastava"

name = add(fname, lname)
print(name)