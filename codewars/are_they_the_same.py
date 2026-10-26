# https://www.codewars.com/kata/550498447451fbbd7600041c/train/python

def comp(array1, array2):
    if not array1:
        return array1 == array2
    for n1 in array1:
        sq = n1*n1
        for j in range(len(array2)):
            if array2[j] == sq:
                array2.pop(j)
                break
        else:
            return False
    return array2 == []
