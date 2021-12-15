def getTwoAnswers():
    ans_1 = input(f'Please enter the first answer below: ')
    ans_2 = input(f'Please enter the second answer below: ')
    ans_1 = ans_1.lower()
    ans_2 = ans_2.lower()
    ans_1 = ans_1.replace(".","") # remove dots
    ans_2 = ans_2.replace(".","")
    ans_1 = ans_1.replace(",","") # remove commas
    ans_2 = ans_2.replace(",","")
    return(ans_1, ans_2)

def makeNgram(string,N):
    seq_Ngram = []
    dictionary = {}
    words = string.split(" ")
    for word in words:
        for g in range(len(word)-1):
            gram = ''
            for i in range(N):
                if i + g < len(word):
                  gram += word[g+i]
            seq_Ngram.append(gram)
    for seq_1 in seq_Ngram:
        dictionary[seq_1] = 0
        for seq_2 in seq_Ngram:
            if seq_1 == seq_2:
                dictionary[seq_1] += 1
    return dictionary

def dictComparison(dict_1,dict_2, n):
    counter = 0
    for k,v in dict_1.items():
        if k in dict_2.keys():
            if v == dict_2[k]:
                counter += 1
    if counter == len(dict_1):
        print(f'{n}Gram: Plagiarism detected!')
    else:
        print(f'{n}Gram: No Plagiarism detected')


# main scirpt

answers = getTwoAnswers()
diction1_2gram = makeNgram(answers[0], 2)
diction1_3gram = makeNgram(answers[0], 3)
diction2_2gram = makeNgram(answers[1], 2)
diction2_3gram = makeNgram(answers[1], 3)

dictComparison(diction1_2gram, diction2_2gram, 2)
dictComparison(diction1_3gram, diction2_3gram, 3)
