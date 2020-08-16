import string

result = string.punctuation

def reverse_string(str_2):
    new_str = str_2.split(' ')
    final_str = []
    punc = []
    for i,word in enumerate(new_str[::-1]):
        index = len(new_str)-i-1


        # print(word[-1])
        if word[-1]  in result:
            final_str.append(word[:-1])
            punc.append((index,word[-1]))
            print(index, word)
            # new_str[-i][-1] = word[-1]
        else: final_str.append(word)
    for val in punc:
        final_str.insert(val[0]+1,val[1])
        ''.join(final_str)
    return ' '.join(final_str)

final_str = reverse_string('hello, my name is bob! and?')
print(final_str)
