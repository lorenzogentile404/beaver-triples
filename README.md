# beaver-triples

A simple Python script to illustrate how to compute a privacy-preserving multiplication between `x` and `y` using Beaver's triples. 

## Example of output

```console
(base) user@host:~$ python beaver_triples.py 
x = 2
y = 2
a,b,c = 4,2,3

Shares of the Beaver's triple sent to P1 by the dealer
a1,b1,c1 = 4,0,4

Shares of the Beaver's triple sent to P2 by the dealer
a2,b2,c2 = 0,2,4

Computation:

P1 computes shares of x, x1 and x2 and sends x2 to P2
x1,x2 = 3,4

P2 computes shares of y, y1 and y2 and sends y1 to P1
y1,y2 = 2,0

P1 computes e1 and d1 and sends them to P2
e1,d1 = 2,2

P2 computes e2 and d2 and sends them to P1
e2,d2 = 4,2

Both P1 and P2 reconstruct e and d, indeed e = (e1 + e2) % p = (a + x) % p and d = (d1 + d2) % p = (b + y) % p
e,d = 1,4

P1 computes z1 and sends it to P2
z1 = 4

P2 computes z2 and sends it to P1
z2 = 0

Both P1 and P2 compute z = (z1 + z2) % p = (x*y) % p
z = 4
```
