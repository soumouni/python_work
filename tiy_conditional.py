#try it yourself page 78
#5.1conditional tests

dinner="soupe"
print("is dinner == 'soupe' I predict true.")
print(dinner=="soupe")

print("\nis dinner == 'kebab' I predict false.")
print(dinner=="kebab")

#create 10 tests, seriously!!!
today="thursday"
print("\nreception day is monday")
print(today=="monday")
print(f"Today is {today} so you can't see the director")
print("\nCan I have an apointment for monday")
appointment="monday"
if appointment == "monday" : 
    print("of course you can. Monday is reception day")

month="December"
year=2021
if month.lower() == "december":
    print(f"\n{month} is the best month of the year, enjoy!")
if year != "2022":
    print("we did not celebrate new year yet, it is still 2021")

time=1.08
if time > 1.30:
    print("\nwe are already in the second half of the hour")
if time < 1.30:
    print("\nwe are in the first half of the hour")

boyfriend=True
if boyfriend ==True:
    print(f"{boyfriend==True} you are dating someone")

happy=False
if boyfriend == True and happy == False:
    print("\nend this relation and move on")

shoppings=["jeans", "polair","sousvet", "pyjamas"]
if "socks" not in shoppings:
    shoppings.append("socks")
    print(f"\nshopping list: {shoppings}")

if ("socks"in shoppings)or("chaussette"in shoppings):
    print("\nok! socks are included")
