    # : 1 Simple message
message = "hello , Python World!."    
print(message)
    # : 2 Simple message
message = "hello , Python World!. "
print(message)
message = "Welcome to Python Programming World!. "    
print(message)
    # : 3 Personal message
name = "sana "    
print(name)
message = f"Hello {name}, would you like to learn some python today?"
print(message)
    # : 4 Name case
person_name = "sana"
message = f"Hello {person_name}, Welcome to the Python Course!."
print(message) 
person_name = "sana "    
print(person_name.lower())
print(person_name.upper())
print(person_name.title())
    # : 5 Famous quote
Quote = "Life is like riding a bicycle. To keep your balance you must keep moving."
author = "Albert Einstein"
print(f"Quote: \"{Quote}\"")
print(f"-{author}" )
    # : 6 Famous quote 2
famous_person = "Albert Einstein"
Quote = "A person who never made a mistake never tried anything new."
print(f"{famous_person} once said, \"{Quote}\"")
famous_person = "Albert Einstein"
Quote = "A person who never made a mistake never tried anything new."
message = f"{famous_person} once said, \"{Quote}\""
print(message)
    # : 7 Stripping name
name_with_space = "    Albert Einstein   "
print(f"Name with spaces:", name_with_space)    
name_cleaned = name_with_space.strip()
print(f"name cleaned:", name_cleaned)
name_with_space = "    Albert Einstein   "
name_cleaned = name_with_space.strip()
Quote = "A person who never made a mistake never tried anything new."
message = f"\t{name_cleaned}\n{Quote}"
print("formatted message:\n", message)
name_with_space = "   Albert Einstein   "
print("name with space:")
print(f"'{name_with_space}'")
print(name_with_space.lstrip())
print(name_with_space.rstrip())
print(name_with_space.strip())
    # : 8 Variable sum
x=5
y=10
z=15
sum = (x+y+z)    
print(sum)
    # : 9 Variable swap

a = 12
b = 13 
print("Before swap:")
print("a =",a)
print("b =",b)
a , b = b , a
print("\nAfter swap")
print("a =",a)
print('b =',b)
    # : 10 Favorite color
Favorite_color = "Black"
print("favorite_color (initial variable):", Favorite_color)
new_Favorite_color = Favorite_color
print("Favorite_color (new variable name):", new_Favorite_color)
    # : 11 Changing Pet Name
pet_name = "Buddy"
pet_name = "Max"
print("The new pet name is:", (pet_name))    
    # : 12 Observing Name Error
sunshine = "weather"
sunsine = "weather"
print(sunshine)
print(sunsine)
    # : 13 Reassigning Score
score = "100"
print("Initial score:", score)
score = "50"
print("Updated score:", score)
    # : 14 City Name
city = "Lahore"
print(city)    
    # : 15 Title Case Text
Text = "python programming"  
Title_case_Text = Text.title()
print(Title_case_Text)
    # : 16 Lowercase Conversion
Mixed_case_string = "THIS is a MIXED case STRing."
Lowercase_string = Mixed_case_string.lower()     
print(Lowercase_string)
    # : 17 uppercase conversion
Mixed_case_string = "this is a mixed case string." 
Uppercase_string  =   Mixed_case_string.upper()
print(Uppercase_string) 
    #  : 18 Current Temperature
Temperature = 25 
print(f"The current temperature is {Temperature} degree.")
    # : 19 Printing a Poem
poem = """Roses is red,
Violets are blue,
sugar is sweet,
And so are you."""   
print(poem)

