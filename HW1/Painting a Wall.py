import math

height = int(input('Enter wall height (feet):\n'))
width = int(input('Enter wall width (feet):\n'))
area = height * width

print('Wall area:', area, 'square feet')

gal_paint = 350
paint_need = area/gal_paint

print('Paint needed: {:.2f} gallons'.format(paint_need))
cans_need = int(math.ceil(paint_need))
print('Cans needed:', cans_need, 'can(s)')
print()

pain_cost_dict = {'red': 35, 'blue': 25, 'green': 23}
color = input('Choose a color to paint the wall:\n')
if color in pain_cost_dict:
    rate = pain_cost_dict.get(color)
    cost = cans_need * rate
    print('Cost of purchasing {} paint: ${}'.format(color, cost))