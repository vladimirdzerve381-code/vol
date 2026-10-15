import random

sarkanie = [1, 3, 5, 7, 9, 12, 14, 18, 19, 21, 25, 27, 30, 32, 34, 36]
melnie = [2, 4, 6, 8, 10, 11, 13, 15, 16, 17, 20, 22, 23, 24, 28, 29, 31, 33, 35]
vesture = []
nauda = 100
print("-----------Godiga rulete-------------")

def izmaksa(likme, reizinatajs=2):
  return likme * reizinatajs

def ir_sarkans(skaitlis):
  return skaitlis in sarkanie

def ir_melns(skaitlis):
  return skaitlis in melnie
  
while nauda > 0:
  likme = float(input("Cik gamble?: "))
  krasa = int(input("sarkans - 1, melns -2, zero -0: "))
  nauda = nauda - likme

  skaitlis = random.randint(0, 36)
  vesture.append(skaitlis)
  print("Izkrita:", skaitlis)
  
  if krasa == 1:
    if ir_sarkans(skaitlis):
      nauda = nauda + izmaksa(likme)
    else:
      print("ne sarkans plak plak")
  elif krasa == 2:
    if ir_melns(skaitlis):
      nauda = nauda izmaksa(likme)
    else:
      print("ne melns plak plak")
  else:
    if skaitlis == 0:
      nauda = nauda + likme * 10
    else:
      print("nu un ko tu grib ja uz zero")

  print("Atlikums:", nauda)
  print("Vesture:", vesture)
print("tu viss patere")
