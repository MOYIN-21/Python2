amount_of_water = float(input("Enter amount of water: "))
initial_temperature = float(input("Enter initial temperature: "))
final_temperature = float(input("Enter final temperature: "))
q = amount_of_water * (final_temperature - initial_temperature) * 4184
print("The energy needed is", q)