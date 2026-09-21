number1=int(input("Enter the first number:")) #ilk sayıyı giriniz.
number2=int(input("Enter the second number:")) #2. sayıyı giriniz
smaller=min(number1,number2) #iki sayıdan küçük olanı alınız.

for i in range(smaller,0,-1): # küçük sayıyı belirledikten sonra sıfıra kadar birer azaltınız.
    if number1%i == 0 and number2%i ==0: #birinci sayının bölümünden kalan sıfır ve ikinci sayıdan bölümü kalan sıfır 
        gcd=i #ebobu gösterir.[cisidi]
        break
lcm=(number1*number2)//gcd #lcm ekok 
print(f"The GCD of {number1} and {number2} is {gcd}")
print(f"The LCM of {number1} and {number2} is {lcm}")

