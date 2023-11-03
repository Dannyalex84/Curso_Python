import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0

rounds = 1

while True:
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)

    print('computer_wins', computer_wins)
    print('user_wins', user_wins)

    user_option = input('piedra, papel o tijera => ')
    user_option = user_option.lower()
    
    rounds += 1

    if not user_option in options:
        print('esa opcion no es valida')
        continue

    computer_option = random.choice(options)

    print('User option =>', user_option)
    print('Computer option =>', computer_option)

    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('Ganaste!')
            user_wins += 1
        else:
            print('Papel gana a piedra')
            print('Perdiste!')
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('Ganaste!')
            user_wins += 1
        else:
            print('Tijera gana a papel')
            print('Perdiste!')
            computer_wins += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('Ganaste!')
            user_wins += 1
        else:
            print('Piedra gana a tijera')
            print('Perdiste!')
            computer_wins += 1
            
    if computer_wins == 2:
        print('El ganador es la PC')
        break
    elif user_wins == 2:
        print('El ganador es el usuario')
        break
        
        
        
        
        
        
        
# if user_option == computer_option:
#     print('Empate!')
# elif user_option == 'piedra':
#     if computer_option == 'Tijera':
#         print('Piedra gana a Tijera')
#         print('Ganaste!')
#     elif computer_option == 'tijera':
#         print('Perdiste!')
#     else:
#         print('empate')
# elif user_option == 'papel':
#     if computer_option == 'piedra':
#         print('Perdiste!')
#     elif computer_option == 'tijera':
#         print('Ganaste!')
#     else:
#         print('Empate!')
# elif user_option == 'tijera':
#     if computer_option == 'papel':
#         print('Perdiste!')
#     elif computer_option == 'piedra':
#         print('Ganaste!')
#     else:
#         print('Empate!')
