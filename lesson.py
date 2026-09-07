#while loop
start_number=int(input("Enter the start number:"))
end_number=int(input("Enter the ending number:"))
while(start_number<end_number):
    if(start_number %2 == 0):
        print(start_number,end=" ")
    start_number+=1