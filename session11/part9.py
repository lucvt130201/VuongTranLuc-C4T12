import random

Skill = [
    {
        "Name" : "TACKLE",
        "Minimum level" : 1,
        "Damage" : 5,
        "Hit rate" : 0.3
    },

    {
        "Name" : "QUICK ATTACK",
        "Minimum level" : 2,
        "Damage" : 3,
        "Hit rate" : 0.5
    },

    {
        "Name" : "STRONG KICK",
        "Minimum level" : 4,
        "Damage" : 9,
        "Hit rate" : 0.2
    }
]

print("Your character's skills: ")
for i, k in enumerate(Skill):
   print(i+1, k["Name"], sep = ":")

character_level = 2
while True:
    ask = input("Which skill do you want to use?: ").upper()

    for i in Skill:
        if ask == i["Name"]:
            if i["Minimum level"] <= character_level:
                # print("Damage: ", i["Damage"])
                rate = round(random.uniform(0,1), 1)
                if rate < i["Hit rate"]:
                    print("Damage: ", i["Damage"])
                else:
                    print("Do not hit the target")     

            else:
                print("You cannot you this skill in this level!")
                

        
                
        
       
    
