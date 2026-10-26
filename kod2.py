def korn(a, b, D):
  x1 = (-b + (D ** 0.5)) / (2 * a)
  x2 = (-b - (D ** 0.5)) / (2 * a)
  print("x1 =", x1)
  print("x2 =", x2)

def dis(a, b, c):
  D = b**2 - 4 * a * c
  print("Diskriminants ir:", D )
  korn(a, b, D)

print("ax + bx + c = 0")
a = float(input("ievadiet a: "))
b = float(input("ievadiet b: "))
c = float(input("ievadiet c: "))
print(f"{a:g}x + ({b:g})x + ({c:g}) = 0")
dis(a, b, c)
