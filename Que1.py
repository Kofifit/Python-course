def guessNumberBasic(min_lim = 1,max_lim = 100):

    int(min_lim)
    int(max_lim)
    counter = 0
    list_int = list(range(min_lim,max_lim+1))
    print(f"Please think of a number between {min_lim} and {max_lim}, but don't tell me what it is!")
    solution = False

    while solution != True:

        int_num = list_int[((len(list_int))//2)]
        resp = f'Is it greater, equal to or less than {int_num}? Answer with G/E/L: '
        ans = input(resp)
        sliceindex = list_int.index(int_num)

        if ans != 'E':
            if ans == 'G':
                counter+=1
                list_int = list_int[(sliceindex + 1):]
            elif ans == 'L':
                counter+=1
                list_int = list_int[:sliceindex]
        else :
            print("I knew I'd get it")
            solution = True

        if len(list_int) == 1:
            print(f'I know your number! It is {list_int[0]}')
            solution = True

    return(counter)


def guessNumberPro():
    import math
    min_lim = int(input(f'What is the lower boundary of the number? '))
    max_lim = int(input(f'What is the upper boundary of the number? '))
    interval = max_lim-min_lim
    guess_num = math.floor(math.log2(interval))
    print(f"I am positive I will guess your number in {guess_num} steps or less")

    counter = guessNumberBasic(min_lim,max_lim)
    if counter == guess_num :
        print(f"I knew I'd guess you number in {guess_num} steps!")
    elif counter < guess_num :
        print(f"Ha! It took less than {guess_num} steps to guess your number!")
    else :
        print(f"Oh well, it took more steps to guess your number.. Maybe next time")


#Choose between Two functions
I = True

while I:
    choice = input(f'Would you like to play with Basic or Pro version? B/P (B-basic,P-pro) : ')
    if choice == 'B' :
        guessNumberBasic()
        I = False
    elif choice == 'P' :
        guessNumberPro()
        I = False
    else :
        print('You have entered the wrong input, try again')

