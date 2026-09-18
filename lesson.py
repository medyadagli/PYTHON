input_number=int(input("Enter a number:"))
isPrime=True
if(input_number<0):
    print("Entered a negative number. Enter a positive number")
elif(input_number>0 and input_number<2):
 print("The smallest prime number is two.")
else:
   for i in range(2,int((input_number**0.5)+1)):
      if(input_number %i == 0):
         isPrime=False
         break
   if(isPrime):
      print(f"{input_number},it is a prime number.")
   else:
      print(f"{input_number},it is not a prime number.")
      