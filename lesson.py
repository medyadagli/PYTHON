name=input("What is your name?")
age=int(input("How old are you?"))
department=input("What is your department?")
study_time=float(input("How many hours do you study per day?"))
weekly_study=  study_time * 7
weekly_goal=40

if weekly_study > 40:
    print("You study a lot!")
elif weekly_study >= 20:
    print("You have a good study routine!")
else:
    print("You should study more regularly")
if study_time >= 8:
    print("You study hard every day!")
elif study_time >=4:
    print("Please study a little harder.")
else:
    print("You don't study enough.")

if weekly_study >= weekly_goal:
    print("You reached your weekly goal.")
else:
    print("You haven't reached your weekly goal yet.")

print(f"Name:{name}")
print(f"Age:{age}")
print(f"Department:{department}")
print(f"Study Time:{study_time}")
print(f"Weekly Study:{weekly_study}")
