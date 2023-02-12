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

# EA 3

class University:
    def __init__(self, sn, c, u, s, o):
        self.school_name = sn
        self.chancellor = c
        self.num_of_undergraduates = u
        self.num_of_staff = s
        self.is_open = o
    
    def __str__(self):
        statement = "%s is run by %s with %d undergraduates and %d staff" % (self.school_name, self.chancellor, self.num_of_undergraduates, self.num_of_staff)
        return statement

    def calculate_gpa(self, grades, credits):
        gpa = 0
        total_credits = 0
        grade_scale = {
            'A+': 4.33,
            'A': 4,
            'A-': 3.67,
            'B+': 3.33,
            'B': 3,
            'B-': 2.67,
            'C+': 2.33,
            'C': 2,
            'C-': 1.67,
            'D': 1,
            'F': 0
        }
        i = 0
        for x in grades:
            gpa += grade_scale[x]*credits[i]
            total_credits += credits[i]
            i += 1

        gpa /= total_credits
        return gpa

u1 = University("SFU", "Tamara Vrooman", 25690, 1095, True)
u2 = University("UBC", "Steven Point", 53872, 6296, True)
gr1 = ['A', 'B', 'A+', 'C']
cr1 = [3, 3, 3, 4]
gr2 = ['F', 'A-', 'A+', 'B+']
cr2 = [2, 3, 3, 3]
print(u1) # SFU is run by Tamara Vrooman with 25690 undergraduates and 1095 staff
print(u2) # UBC is run by Steven Point with 53872 undergraduates and 6296 staff
print(u1.calculate_gpa(gr1, cr1)) # 3.23
print(u2.calculate_gpa(gr2, cr2)) # 3.09000...
