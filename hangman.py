import random
import pyfiglet
hangman = [

"""
   _________
    |/
    |
    |
    |
    |
    |
    |___
    """,

"""
   _________
    |/   |
    |
    |
    |
    |
    |
    |___
    H""",

"""
   _________
    |/   |
    |   (_)
    |
    |
    |
    |
    |___
    HA""",

"""
   ________
    |/   |
    |   (_)
    |    |
    |    |
    |
    |
    |___
    HAN""",


"""
   _________
    |/   |
    |   (_)
    |   /|
    |    |
    |
    |
    |___
    HANG""",


"""
   _________
    |/   |
    |   (_)
    |   /|\\
    |    |
    |
    |
    |___
    HANGM""",



"""
   ________
    |/   |
    |   (_)
    |   /|\\
    |    |
    |   /
    |
    |___
    HANGMA""",


"""
   ________
    |/   |
    |   (_)
    |   /|\\
    |    |
    |   / \\
    |
    |___
    HANGMAN"""]


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def answer(space):
    new = space.replace(" ","")
    return new


attempt = 8
start = 0
words = ["caterpillar","absurd","scatter","dictionary","tuple","python","political","infosys","jeppiaar","marvel","avengers","panther","bottle","environmental"]
current = random.choice(words)
cur_lst=list(current)
space = (" ".join(["_"]*len(current)))
lst = []
while attempt>0:

    if answer(space)==current:
        print(space)
        print(pyfiglet.figlet_format("Congrats", font = "slant"  ))
        print(pyfiglet.figlet_format("You did it.", font = "slant"  ))
        break


    print()
    print(f"Guess the word: {space}")
    print()
    val = input("Type a letter: ")

    if val in cur_lst:
        if val in lst:
            print()
            print("You have already entered this letter. Try something else:)")
            print()
            attempt-=1
            if attempt==0:
                print(hangman[start])
                print()
                print("You're so cruel.You killed him. Go get yourself a dictionary")
                print()
                print(f"Ans is {current}")
                break

            print(hangman[start])
            print()
            print(f"Words used: {lst}")
            start+=1
            print(f"you have {attempt} more attempts")


        else:
            lst.append(val)
            index = find(current,val)
            space = space.split()
            for j in index:
                space[j] = current[j]
            space = " ".join(space)
            print()
            print(f"Words used: {lst}")
            print()
            print(f"you have {attempt} more attempts")
            continue

    elif len(val)>1:
        lst.append(val)
        print()
        print("Type a single character")
        print()
        attempt-=1
        if attempt==0:
            print(hangman[start])
            print()
            print("You're so cruel.You killed him. Go get yourself a dictionary")
            print()
            print(f"Ans is {current}")
            break

        print(hangman[start])
        print()
        print(f"Words used: {lst}")
        start+=1
        print(f"you have {attempt} more attempts")

    else:
        lst.append(val)
        print()
        attempt-=1
        if attempt==0:
            print(hangman[start])
            print()
            print("You're so cruel.You killed him. Go get yourself a dictionary")
            print()
            print(f"Ans is {current}")
            break
        else:
            print(hangman[start])
            print()
            print(f"Words used: {lst}")
            start+=1
            print(f"you have {attempt} more attempts")
            print(attempt)
