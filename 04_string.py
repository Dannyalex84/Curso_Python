name = 'Danny'
last_name = 'Belandria'
print(name)
print(last_name)

full_name = name + ' ' + last_name
print(full_name)

quote = "I'm Danny"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

#format
Template = "Hola, mi nombre es " + name + " y mi apellido es " + last_name
print('v1', Template)

Template ="Hola, mi nombre es {} y mi apellido es {}".format(name, last_name)
print('v2', Template)

Template = f"Hola, mi nombre es {name} y mi apellido es {last_name}"
print('v3', Template)

