def comp(array1, array2):
    if array2==None or array1==None:
        return False
    if  array2==[] and array1==[]:
        return True
    for i in range(len(array1)):
        if array1[i] < 0:
            array1[i] *= -1
    for i in array2:
        if i**(0.5) not in array1:
            return False
        else:
            array1.remove(i**(0.5))
    return True

