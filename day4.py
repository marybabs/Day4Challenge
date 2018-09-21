def sum_list(L):
    total = 0 
    for i in L:
        if isinstance(i, list):  # checks if `i` is a list
            total += sum_list(i)
        else:
            total += i
    return total
print(sum_list([1,2,3,[1,2,3]]))



def power(x,y):
    if(y==1):
        return(x)
    if(y!=1):
        return(x*power(x,y-1))
x=int(input("Enter base: "))
y=int(input("Enter exponential value: "))
print("Result:",power(x,y))