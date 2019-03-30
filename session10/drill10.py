book = {
    "name" : "The Diary of a Cricket",
    "author" : "To Hoai",
    "released year" : 1941,
    "main characters" : ["Men", "Trui","Uncle Xen Toc"]
}

book["country"] = "Vietnam"


MCQ = {
    "Q1" : """What is the author of 'The Diary of a Cricket?' 
            A: To Hoai
            B: To Huu
            C: Xuan Dieu  
    """,

    "Q2" : """What is the main character of this book?
            A: Chi Pheo
            B: Men
            C: Lao Hac

    """
            

}

Ans = {
    "Q1":"A",
    "Q2":"B"
}

correct = 0

for key, value in MCQ.items():
    print(value)
    ans = input("Your answer is: ").lower()
    
    if ans == Ans[key].lower():
        print("Correct!")
        correct += 1

    else: 
        print("Incorrect!")

percent = (correct/2)*100
print("percentage of correct answer is:", percent, "%")


# MCQ = {
#     "what is the author of the book?:" : 
# }

# for key, value in MCQ.items():
#     ans = input(key).lower()

#     if ans == value.lower():
#         print("Correct!")
#     else:
#         print("Wrong!")
    