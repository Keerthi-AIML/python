

#while loop
is_failed=True
i=1
while is_failed:
    if i%2!=0:
        i=i+1
        continue
    print(f"Try {i}")
    i=i+1
    if i>100:
        break
print("I GAVE UP")

# to print number 1 to 10 using while loop
i=1
while i<=10:
  print(i)
  i=i+1

i=0
while i<10:
  x=0
  while x<i:
    print("keerthi")
    x=x+1
  i=i+1

i=0
while i<10:
  x=0
  while(x<i):
    print("keerthi",end="")
    x=x+1
 print("")
 i=i+1

i=0
while i<10:
  x=0
  while(x<i):
      print("keerthi",end="*")
      x=x+1
  print("")
  i=i+1

i=5
while i>=1:
    print(i)
    i=i-1

i=1
while i<=5:
    print(i)
    i=i+1

sheep_count=1
while sheep_count<=10:
  print(f"sheep{sheep_count}")
  if sheep_count==5:
    print("that's enough counting")
    break
  sheep_count+=1