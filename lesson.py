input_number=int(input("Enter a number:"))
prime_numbers=[]
if input_number<0:
    print("Entered a negative number.Enter positive a number.")
elif input_number>0 and input_number<2:
    print("The smallest prime number is two")
else:
    prime_numbers.append(2)
    for i in range(3,input_number+1,2):
         for j in range(3,int(i**0.5)+1):
          if(i %j == 0):
             break
         else:
             prime_numbers.append(i)
    print(f"{prime_numbers}")