

plus_isnot_over=True
while plus_isnot_over:
  try:
    print("Enter Number:")
    numb_1= float(input())
    print("Enter +: ")
    plus=input()
    print("Enter another number: ")
    numb_2=float(input())
    if plus == "+":
      print(int(numb_1+numb_2))
    else:
      print("invalid operator! ")
  except ValueError :
    print("invalid input! ")
    