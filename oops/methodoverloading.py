#same function name different count of parameters

def add_nmbrs(n1,n2):
    return n1+n2
def add_nmbrs(n1,n2,n3):
    return(n1+n2+n3)

# print(add_nmbrs(100,400,100))
# print(add_nmbrs(800,988))             #method overloaded



def add_numbers(*args):
    print(sum(args))
add_numbers(10,20)
add_numbers(20,30,50)
add_numbers(39,38,49,98)