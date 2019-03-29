high_scores = [45, 67, 56, 78]
high_scores.sort()
for i, item in enumerate(high_scores):
    print(i+1,'.',item )

ask = int(input("Enter your new score: "))
if ask in high_scores:
    print("no change in your high score")
    for i, item in enumerate(high_scores):
        print(i+1,'.',item )

else:
    
    high_scores.append(ask)
    high_scores.sort()

    print("new high score: ")
    for i, item in enumerate(high_scores):
        print(i+1,'.',item )




