s1 = 'Я люблю тебя'
s2 = "I love you"
s3 = """
На дворе трава
На траве ???
"""

#print (s3)
#who = input ("Что было на траве?")
#print ("На траве были", who)

a = input("Enter a:")
print(type(a))
a = int(a)
print(type(a))
pi = 3.1415926

print (f'a={a}, pi={pi}, a*pi={a*pi}')

b = a/2
bb = a//2
bbb = a ** 3
print(f'{b=}, {bb=}, {bbb=}')

c1 = bbb == 8
c2 = bbb == 16
print(f'{c1=}, {c2=}')
