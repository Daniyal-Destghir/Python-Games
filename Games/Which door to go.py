import time

print("Which door to go?")
time.sleep(2)

Q1 =input("Which door to go? White or Black: ")
time.sleep(2)

if Q1 == "White":
    print("Are you racist?")
    time.sleep(2)
    print("You lost.")

if Q1 == "Black":
    print("#BLM")
    time.sleep(2)
    Q2 =input("Which makes more sense(1+1 = 2 or 1+1 = 11. Choose 2 or 11?): ")
    if Q2 == "2":
        print("Lol")
        time.sleep(2)
        print("You lost")
    if Q2 == "11":
        print("NOICE!")
        time.sleep(2)
        print("You survived")
        Q3 =input("Which makes more sense(2+2 = 4 or 2+2 = 22): ")
        if Q3 == "22":
            print("HAHAHAHA")
            time.sleep(3)
            print("Lol, you lost")
        if Q3 == "4":
            print("Yass, you won!")

