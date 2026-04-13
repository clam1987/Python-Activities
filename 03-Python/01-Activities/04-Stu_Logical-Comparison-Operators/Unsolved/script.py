a = "50"
b = 50
c = 100
d = c % b
e = c / 2

expression1 = (b == e);
expression2 = (e < d);

# Use comparison operators so all expressions below log to the console as true
print(a == b);
print(b != e);
print(c < b);
print(d > 0);

# Use logical operators so all expressions below log to the console as true
print(expression1 and expression2);
print( not expression1 or expression2);
  
