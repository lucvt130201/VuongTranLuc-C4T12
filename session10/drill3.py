pokemon = {
"raichu" : "has a regional variant that is Electric/Psychic It evolves from Pikachu when exposed to a Thunder Stone. All Pikachu in Alola will evolve into this form regardless of their origin",
"onix" : "resembles a giant chain of gray boulders that become smaller towards the tail. It has a rocky spine on its head and a pair of black eyes right beneath it. This Pokémon has a magnet in its brain that serves as an internal compass. Its body absorbs many hard objects, making its body very solid. As it grows older, it becomes more rounded and smoother, eventually becoming similar to black diamonds.",
"ponyta" : " is very weak at birth. It can barely stand up. This Pokémon becomes stronger by stumbling and falling to keep up with its parent",
"pidgeot" :"is a Normal/Flying type Pokémon introduced in Generation 1. It is known as the Bird Pokémon.Pidgeot has a Mega Evolution, available from Omega Ruby & Alpha Sapphire onwards."

}
while True:
    ask = input("enter a pokemon name: ").lower()
    if ask in pokemon:
        print(pokemon[ask])
    else:
        print("there is no this pokemon in the dictionary.")