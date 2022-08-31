def main():
  print("Welcome to my inches to feet converter!")
  inh=int(input("Please enter a number of inches:"))
  while inh!=0:
    
  
    if inh<0:
      print("Please enter a positive number!")
    else: 
      feet=inh/12
      print(round(feet,1), "feet")
    inh=int(input("Please enter a number of inches:"))
  print("Have a nice day!")
main()