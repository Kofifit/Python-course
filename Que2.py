def makeFibonacci(len_array):

    fib_seq = [0]*len_array
    for i in range(0,len_array) :
        if i==0 or i == 1:
            fib_seq[i] = 1
        else :
            fib_seq[i] = fib_seq[i-1] + fib_seq[i-2]
    return(fib_seq)

def ternarySearch(value, array):
    import math
    found = False
    index = 0
    max_ind = len(array)-1
    min_ind = 0
    while found != True:
        slice_1 = min_ind + math.ceil((max_ind-min_ind)/3)
        slice_2 = max_ind - math.ceil((max_ind-min_ind)/3)
        if slice_2 >= slice_1:         
            if array[slice_1] == value:
                index = slice_1
                found = True
            elif array[slice_2] == value:
                index = slice_2
                found = True
            elif array[slice_1] > value:
                max_ind = slice_1
            elif array[slice_1] < value and array[slice_2] > value:
                min_ind = slice_1
                max_ind = slice_2
            elif array[slice_2] < value:
                min_ind = slice_2
        else :
            index = []
            found = True
    return(index)


# main script

len_array = input(f'Please enter the length of Fibonacci: ')
value = input(f'Please enter the value you are looking for: ')
array = makeFibonacci(int(len_array))
index = ternarySearch(int(value), array)

if index == []:
    print(f'{value} wasn’t found in the requested Fibonacci sequence.')
else:
    print(f'The index of {value} in this Fibonacci sequence {index}')

