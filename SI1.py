# неявные
a = 5 # int
b = 5.4 # float
c = "Five" # string
d = True
print(a, b ,c ,d)

# явные
a = int(5)
b = float(5.4)
c = str("Five")
d = bool(True)
print(a, b, c, d)
# range
for i in range(6, 15):
    i = i + 1
    print("Element:", i, "in range")
# pythonUsage
pythonUsage = '''Python is used for:
web development (server-side),
software development,
mathematics,
system scripting.'''
print(pythonUsage)
if 'server' and 'mathematics' in pythonUsage:
    print("Есть слово server и mathematics")
# eu am 5kg
a = 5
b = 2.5
c = 4
print("Eu am", a, "kg de miere si", b, "kilo de faina ca sa faca niste placinte \"Speciale\" in timp de", c, "ore")