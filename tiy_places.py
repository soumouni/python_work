#tiy page 46
# seeing the world

places=["cuba", "suisse","suede","indonesie","thailand","kenya"]
print(places)
print("\nin alphabetical order")
print(sorted(places))
print(places)          #still same list
print("\nin reverse alphabetical order")
print(sorted(places,reverse=True))
print(places)           #still same list
print("\nin reverse order")
places.reverse()
print(places)
places.reverse()
print(places)            #back to original
print("\nalphabetical permanent")
places.sort()
print (places)
print("\nreverse alphabetical permanent")
places.sort(reverse=True)
print (places)

print("number of places I want to visit is:")
print(len(places))