import random

random_number=random.randint(1,100) # 1 ile 100 arasında rasgele bir tam sayı üret.
remaining_attempts=5 # 5 deneme hakkı tanındı
score=100 #başlangıç puanı
attempt_count=0 # deneme sayısı
print("Guess a number between 1 and 100") # 1 ile 100 arasında bir sayı tahmin et
print(f"Your starting score:{score}") # senin scorun {score} adında variable da saklı

while remaining_attempts>0:
    guess=int(input("Your guess:")) #tahmin ettiğin bir tam sayı gir
    attempt_count+=1 #deneme sayısını bir artır
    if guess<1 or guess>100:  # Eğer sayı 1 den küçük veya 100 den büyük ise
        print("Please!Enter a number between 1 and 100") # lütfen bir ille yüz arasında bir sayı gir
        continue #döngünün başına git ben altımdaki satırları çalıştırmıyorum
    if(guess==random_number): # Eğer tahmin ettiğin sayı random_number eşit ise 
        print(f"Congralations! You guessed the number correctly on your {attempt_count}.attempt") #tebrikler sayıyı doğru bir şekilde girdin.
        print(f"Your total score:{score}") # senin toplam puanın {score} yazıyor
        break #döngüyü kır ve sonlandır.
    elif(guess<random_number): #tahmini sayı random_number dan küçük ise
        print("Try a larger number.") # daha büyük bir sayı dene
    else: #değilse
        print("Try a smaller number.") # daha küçük bir sayı dene
        remaining_attempts-=1 # deneme sayısından 1 çıkar
        score-=10 #puanın 10 puanını sil
    if(remaining_attempts>0):
            print(f"Remaining attempts:{remaining_attempts}")
            print(f"Current score:{score}")
    else:
     print("Unfortunately! You ran out of attempts!")
     print(f"Your total score:{score}")
else:
    print(f"Unfortunately! You ran out of attempts!")
    print(f"Your total score:{score}")