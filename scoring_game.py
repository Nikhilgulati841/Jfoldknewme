# import PyInstaller.__main__

# PyInstaller.__main__.run([
#     'scoring_game.py',
#     '--onefile',
#     '--console',
#     '-n Score'
# ])

print('''\n----Instructions to play----
Get the BAR value to 3, to win the Game.\n
- Two types of Points --> PowerFull | Powerless
- PowerFull will give the sum of all 3 Points
- PowerLess will only give it for the first 2 Points''')

def game(a,b,c,attempt,bar):

    a=int(input("\nPoint 1: "))
    b=int(input("Point 2: "))
    c=int(input("Point 3: "))

    if a+b>c:
        score=a+b+c
        print(f"\n{msgnew} | Score:{score}")
        bar+=1
        print(f"ATTEMPT:{attempt} | BAR:{bar}")
        
    elif a+b==c:
        score=a+b+c
        print(f"\n{msgnew} | Score:{score}")
        bar+=1
        print(f"ATTEMPT:{attempt} | BAR:{bar}")

    else:
        score=a+b
        print(f"\n{msgnew} | Score:{score}")
        bar-=1
        print(f"ATTEMPT:{attempt} | BAR:{bar}")

    attempt+=1

    return attempt, bar



msgnew="PowerFull Points"
msgold="PowerLess Points"
barmsg="\nAchieved"

attempt=0
bar=0

while True:
    if bar==3:
        print(f"{barmsg} (Bar:{bar} have Achieved @Attempt:{attempt})")
        break
    else:
        attempt,bar=game(1,1,1,attempt,bar)

#when the loop is breaked after reaching BAR:3
#print this below if condition meet.

if attempt==bar:
    print("\n|Also, BAR:3 is Achieved on the same number Attempt:3|")
    print("|-----------All Attempts PowerFull Points------------|\n")

input()

# Yo Rottweiler

