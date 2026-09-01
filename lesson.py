print("CINEMA TICKET STATION")
age=int(input("How old are you?"))

if age<18:
    print("A ticket for 100 TL")
if age >= 65 :
    print("A ticket for 150 TL")
if  18 <= age <= 64:
    student=input("Are you a student? Yes/No: ")
if student == "YES":
 
  print("YES,a  ticket for 100 TL")
else:
   print("No,a full ticket costs 200 TL")


                  