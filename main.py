import Plus 
"""basic sqr calculating with a while loop that shows you sqr is still going untill to stop it . 
i am very happy this is my first programm
"""

sqr_is_still_going=True
while sqr_is_still_going:
  try: 
    print("Enter a number: ")
    num=int(input())
    sqr=num**2 
    print("square of",num,"is",sqr)
  except ValueError:
    print("invalid input plz input numbers")
    
    
  













