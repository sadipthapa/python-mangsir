pie=3.14
print(pie)
print(type(pie))
print(int(pie))
print(type(str(pie)))

string="12"
int(string)

#list to tuple
fruits=(
    'apple',
    'orange',
    'kivi',
    'banana',
    123,
    1.1
)
fruits=list(fruits)
fruits[0]="bsdjkbsdj"
print(tuple(fruits))
print(type(fruits))