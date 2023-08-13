memo = '''hi
my name is
choigukhee'''

print(memo)

a= "hi"
print(a*2)

b = "hello"
c = " world"
print(b+c)

print("="*50)
print("hi")
print("="*50)

life = "hi, my life is very good"
print(len(life))
print(life[0])
print(life[5])
print(life[0:6])
print(life[12:])
print(life[:])

content = "20010331Rainy"
year = content[0:4]
month = content[4:6]
date = content[6:8]
weather = content[8:]
print(year + " " +  month + " " + date + " " + weather)

name = "gukhee"
newName = name[0:2] + "p" + name[3:]
name = newName
print(name)

print("I eat %d apples" %3)

print("I eat %s." %"apples")

print("I ate %d apples. so I was sick for %s days" %(10,"three")) 

print("that is %d%%" %98)

print("%10s hi" %"oh")
print("%-10s hi" %"oh")

print("I eat {0} apples" .format(3))
print("I eat {0} {1}" .format(3, "apples"))
print ("I eat {num} {thing}" .format(num = 3, thing = "apples"))

print(f'{"hi":=^10}')
print(f'{"python":!^12}')

f="hobby"
print(f.count('b'))
print(len(f))
print(f.find('b'))
print(f.find("i"))
print(f.upper())
print(f.lower())
print(f.replace("h", "r"))
