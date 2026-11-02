print("Welcome to the Interactive Personal Data Collector")
print('''
''')
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height= float(input("Enter your height: "))
number = int(input("Enter your favorite number: "))
print('''
''')

print("Thank You! Here is the information we collected: ")
print(''' ''')

print(f"Name: {name} (Type: {type(name)}, Memory Address: {id(name)})")
print(''' ''')

print(f"Age: {age} (Type: {type(age)}, Memory Address: {id(age)})")
print(''' ''')
print(f"Height: {height} (Type: {type(height)}, Memory Address: {id(height)})")
print(''' ''')
print(f"Favourite number: {number} (Type: {type(number)}, Memory Address: {id(number)})")
print(''' ''')

birth_year=2026-age
print(f"You birth year is approximately {birth_year} (Based on your age {age})")
print('''
''')
print("Thank you for using the Interactive Personal Data Collector, Goodbye!")