first_name="khalil  "
second_name= "  mehdi"
family_name= "  Mimouni    "

print(f"{first_name}{second_name}{family_name}" )
first_name=first_name.rstrip()
second_name=second_name.lstrip()
family_name=family_name.strip()
print(f"\n\t{first_name.title()} {second_name.title()} {family_name.upper()}")