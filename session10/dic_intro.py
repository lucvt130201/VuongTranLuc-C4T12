person  = {
"name" : "lampard",
"club" : "Chelsea"

}
key = input("what is do you want to add?: ")
value = input("description of your things: ")

ask_key = input("which information do you want to know?")
if ask_key in person:
    print(person[ask_key])
else:
    print("This information are not in the dictionary")

person[key] = value

dele = input("which one do you want to delete?: ")
if dele in person:
    del(person[dele])
    print(person)
else:
    print("this one are not in the dictionary.")
