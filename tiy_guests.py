#try it yourself of page 42
#working with lists

guests=["Amel","Amine","Akram","Faycal"]
print(f"salut {guests[0]}, tu es invitee a diner chez moi demain")
print(f"salut {guests[1]}, tu es invite a diner chez moi demain")
print(f"salut {guests[2]}, tu es invite a diner chez moi demain")
print(f"salut {guests[3]}, tu es invite a diner chez moi demain")

#remove faycal from list and replace it by pitchou

print(f"\n Malheureusement, {guests[3]} ne pourra pas assister au diner")
guests.remove("Faycal")
guests.append("pitchou")
print(guests)
print(f"salut {guests[3]}, tu es invite a diner chez moi demain")

#add more guests
print("\nsalut les amis, j'ai pu avoir une plus grande table au restaurant, nous serons donc plus nombreux")
guests.insert(0,"Ibtissem")
guests.insert(2,"Kahina")
guests.append("Khaoula")
print(f"\nsalut {guests[0]}, tu es invite a diner chez moi demain")
print(f"salut {guests[2]}, tu es invite a diner chez moi demain")
print(f"salut {guests[6]}, tu es invite a diner chez moi demain")

#shrinking guest list to 2 people
print(guests)

print("\nsalut les amis, cet exercice est tres bizarre. \nil s'avere que la grande table n'est pas disponible, je ne peux inviter que 2 personnes \n desole pour les autres ")
cancelled= guests.pop(2)
print(f"\n\tdesole {cancelled}, je ne pourrais pas t'inviter ce soir, on refait ca")
cancelled= guests.pop(2)
print(f"\tdesole {cancelled}, je ne pourrais pas t'inviter ce soir, on refait ca")
cancelled= guests.pop(2)
print(f"\tdesole {cancelled}, je ne pourrais pas t'inviter ce soir, on refait ca")
cancelled= guests.pop(2)
print(f"\tdesole {cancelled}, je ne pourrais pas t'inviter ce soir, on refait ca")
cancelled= guests.pop(2)
print(f"\tdesole {cancelled}, je ne pourrais pas t'inviter ce soir, on refait ca")

print(f"\n {guests[0]} ca tient toujours pour demain, RDV a 19h")
print(f"\n {guests[1]} ca tient toujours pour demain, RDV a 19h")

del guests[0]
del guests[0]
print()
print(guests)