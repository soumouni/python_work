#try it yourself page 56
#pizzas

pizzas=["saumon", "creme fraiche" , "tuna"]
print("\nmy favorite pizzas are:")
for pizza in pizzas:
    print(f"I like {pizza.title()} pizza")      #end of for loop
print("I really like pizza, but kowing it is not very healthy, I rarely eat pizza")

# try it yourself page 65
friend_pizzas=pizzas[:]
pizzas.append("carre")
friend_pizzas.append("fumato")
print("my favorite pizzas are")
for pizza in pizzas:
    print (pizza)
print("\n my friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)




#animals
animals=["dog", "cat", "chicken"]
print("\nin a farm you can find")
for animal in animals:
    print(animal)
print(f"\n{animals[0]} and {animals[1]} would make great pets")
print(f"{animals[2]} gives eggs")
print("\nany of these animals are a must in a farm\n")