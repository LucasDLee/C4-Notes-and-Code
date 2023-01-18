# EA 2

def vowel_counter(my_statement):
    
    if type(my_statement) != type(""):
        return "Please input a string"
    
    vowels = 0
    my_statement = my_statement.lower()

    for x in my_statement:
        if (ord(x) == 97 # a
            or ord(x) == 101 # e
            or ord(x) == 105 # i
            or ord(x) == 111 # o
            or ord(x) == 117 # u
            or ord(x) == 121): # y
            vowels += 1
    return vowels

print(vowel_counter("among us"))
print(vowel_counter("City CENTRE commUnity Centre"))
print(vowel_counter(23423))
print(vowel_counter(True))
print(vowel_counter('a'))
print(vowel_counter('A'))
print(vowel_counter("bc"))