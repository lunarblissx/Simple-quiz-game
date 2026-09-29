
print("==== QUIZ ====")
print("Welcome to a quiz game please chose the option yoou think is correct by entering thir serial number:")

score=0

q1={"question":"What is the capital of India??", "options":["Mumbai", "New Delhi", "Kolkata", "Chennai"], "answer":2}

q2={"question":"What is the result of 5+3??", "options":["6", "7", "8", "9"], "answer":3}

q3={"question":"Which of these is a Python data type??", "options":["list", "screen", "button", "window"], "answer":1}

q4={"question":"How many bits are there in 1 byte??", "options":["4", "8", "16", "32"], "answer":2}

q5={"question":"Which is the keyword used to define a function in Python??", "options":["function", "define", "def", "fun"], "answer":3 }



lis=[q1, q2, q3, q4, q5]

for items in lis:
    print(items["question"])
    for index, options in enumerate(items["options"], start=1):
        print(index,options)

    while True:
        ans=int(input("Enter your choice:"))
        if ans>4 or ans<1:
            print("Invalid choice")
            continue
        else:
            break

        
    if items["answer"]==ans:
        print("Your answer is correct")
        score=score+1

    else:
        print("Invalid answer please answer again")

print(f"Your total score is{score}")
