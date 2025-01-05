import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy, try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

# 8 Ball ASCII
print("       _.a$$$$$a._")
print("     ,$$$$$$$$$$$$$.")
print("   ,$$$$$$$$$$$$$$$$$.")
print("  d$$$$$$$$$$$$$$$$$$$b")
print(" d$$$$$$$$~'\"`~$$$$$$$$b")
print("($$$$$$$p   _   q$$$$$$$)")
print("$$$$$$$$   (_)   $$$$$$$$")
print("$$$$$$$$   (_)   $$$$$$$$")
print("($$$$$$$b       d$$$$$$$)")
print(" q$$$$$$$$a._.a$$$$$$$$p")
print("  q$$$$$$$$$$$$$$$$$$$p")
print("   `$$$$$$$$$$$$$$$$$'")
print("     `$$$$$$$$$$$$$'")
print("       `~$$$$$$$~'")
print(" ")


# Ask the user for a question
input("Ask a yes-or-no question: ")

# Generate a random number and get the fortune
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
