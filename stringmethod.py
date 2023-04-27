##isdigit()

a="12345"
print(a.isdigit())

##strip()

a="    thunder soft   "
z=a.strip(" ")
y=(a.strip())
print(y)
print(z)

##lower
c="THUNDERSOFT HYDERBAD"
print(c.lower())

##UPPER()

c="thundersoft hyderbad"
print(c.upper())


##startswith()

txt = "Hello, welcome to my world."

x = txt.startswith("wel", 7, 20)

print(x)

txt1="thunder,soft is mobile company"

x=txt1.startswith("so",9,29)

##endswith()

txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)


x = txt.endswith("my world1.")

print(x)

##replace()

t = "I like bananas"

x = t.replace("bananas", "apples")
y=x.replace("apple","pineapple")

print(x)
print(y)