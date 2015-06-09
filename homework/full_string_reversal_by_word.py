def string_reversal_by_word(s):
    return ' '.join(s.split()[::-1])

s1 = 'I love milk'
print(string_reversal_by_word(s1))