# This function verify the variable and the result is true in case of an array. 
def IsItArray(a):
    return isinstance(a, list)

# This is the main function. The previous function was integrated. 
def array_diff(a, b):
    if IsItArray(a) and IsItArray(b):
        for x in b:
            i = 0
            while i < len(a):
                if a[i] == x:
                    a.pop(i)
                else:
                    i+=1
    else:
        a = []
    return a