import random

sarkanie = [1, 3, 5, 7, 9, 12, 14, 18, 19, 21, 25, 27, 30, 32, 34, 36]
melnie = [2, 4, 6, 8, 10, 11, 13, 15, 16, 17, 20, 22, 23, 24, 28, 29, 31, 33, 35]
vesture = []
nauda = 72
print("-----------Godiga rulete-------------")
print("Ja skaitlis uz rulete ir sarkans tad tava likme x2")

while nauda > 0:
  likme = float(input("Cik gamble?: "))
  krasa = int(input("sarkans - 1, melns -2, zero -0"))
  nauda = nauda - likme

  skaitlis = random.randint(0, 36)
  vesture.append(skaitlis)
  print("Izkrita:", skaitlis)
  

  if krasa == 1:
    if skaitlis in sarkanie:
      nauda = nauda + likme * 2
    else:
      print("ne sarkans plak plak")
  elif krasa == 2:
    if skaitlis in melnie:
      nauda = nauda + likme * 2
    else:
      print("ne melns plak plak")
  else:
    print("bro tu kreizi")
    if skaitlis == 0:
      nauda = nauda + likme * 10
    else:
      print("nu un ko tu grib ja uz zero")

  print("Atlikums:", nauda)
print("tu viss patere")
