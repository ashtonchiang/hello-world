lemon_juice = int(input('Enter amount of lemon juice (in cups):\n'))
h20 = int(input('Enter amount of water (in cups):\n'))
agave_nectar = float(input('Enter amount of agave nectar (in cups):\n'))
servings = int(input('How many servings does this make?\n'))
print('')

print('Lemonade ingredients - yields {:.2f} servings'.format(servings))
print('{:.2f} cup(s) lemon juice'.format(lemon_juice))
print('{:.2f} cup(s) water'.format(h20))
print('{:.2f} cup(s) agave nectar'.format(agave_nectar))
print('')

servings2 = int(input('How many servings would you like to make?\n'))
x = servings2/servings
lemonJuice = lemon_juice * x
water = h20 * x
agaveNectar = agave_nectar * x
print('')

print('Lemonade ingredients - yields {:.2f} servings'.format(servings2))
print('{:.2f} cup(s) lemon juice'.format(lemonJuice))
print('{:.2f} cup(s) water'.format(water))
print('{:.2f} cup(s) agave nectar'.format(agaveNectar))
print('')

print('Lemonade ingredients - yields {:.2f} servings'.format(servings2))
print('{:.2f} gallon(s) lemon juice'.format(lemonJuice/16))
print('{:.2f} gallon(s) water'.format(water/16))
print('{:.2f} gallon(s) agave nectar'.format(agaveNectar/16))



