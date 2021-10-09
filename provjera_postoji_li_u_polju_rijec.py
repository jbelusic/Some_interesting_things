
print("Start")

a = ["ana", "ivo", "lili", "kika"]
b = ("KE", "NT", "KA", "ELJ")

ai = iter(a)

fleg = 0

while True:
  try:
    if next(ai).upper()[-2:] in b:
      fleg = 1
      break
  except Exception as e:
    print(e)
    break

if fleg == 0:
  print("nije")
else:
  print("je")

print("End")