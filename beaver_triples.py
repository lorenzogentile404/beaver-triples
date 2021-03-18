import random

# F_p with p = 5
p = 5

# P1 has input x, P2 has input y and we want to compute z = (x*y) % p
x = 2
print("x = " + str(x))

y = 2
print("y = " + str(y))

# Generate Beaver's triple
a = random.randint(0, p-1)

b = random.randint(0, p-1)

c = a*b % p

print("a,b,c = " + str(a) + "," + str(b) + "," + str(c))

# Secret share Beaver's triple
def secret_share(s):
    s1 = random.randint(0, p-1)
    s2 = (s - s1) % p
    # print(str(s) + " = (" + str(s1) + " + " + str(s2) + ") % " + str(p))
    return s1,s2

# a1,b1,c1 go to P1 and a2,b2,c2 go to P2
a1,a2 = secret_share(a)
b1,b2 = secret_share(b)
c1,c2 = secret_share(c)

print("\nShares of the Beaver's triple sent to P1 by the dealer")
print("a1,b1,c1 = " + str(a1) + "," + str(b1) + "," + str(c1))

print("\nShares of the Beaver's triple sent to P2 by the dealer")
print("a2,b2,c2 = " + str(a2) + "," + str(b2) + "," + str(c2))

print("\nComputation:\n")

print("P1 computes shares of x, x1 and x2 and sends x2 to P2")
x1,x2 = secret_share(x)

print("x1,x2 = " + str(x1) + "," + str(x2))

print("\nP2 computes shares of y, y1 and y2 and sends y1 to P1")
y1,y2= secret_share(y)

print("y1,y2 = " + str(y1) + "," + str(y2))

print("\nP1 computes e1 and d1 and sends them to P2")
e1 = (a1 + x1) % p
d1 = (b1 + y1) % p

print("e1,d1 = " + str(e1) + "," + str(d1))

print("\nP2 computes e2 and d2 and sends them to P1")
e2 = (a2 + x2) % p
d2 = (b2 + y2) % p

print("e2,d2 = " + str(e2) + "," + str(d2))

print("\nBoth P1 and P2 reconstruct e and d, indeed e = (e1 + e2) % p = (a + x) % p and d = (d1 + d2) % p = (b + y) % p") 
e = (e1 + e2) % p
d = (d1 + d2) % p

print("e,d = " + str(e) + "," + str(d))

print("\nP1 computes z1 and sends it to P2")
z1 = (c1 + e*y1 + d*x1 - e*d) % p

print("z1 = " + str(z1))

print("\nP2 computes z2 and sends it to P1")
z2 = (c2 + e*y2 + d*x2) % p

print("z2 = " + str(z2))

print("\nBoth P1 and P2 compute z = (z1 + z2) % p = (x*y) % p")
z = (z1 + z2) % p
print("z = " + str(z))
assert((x*y) % p == z)
