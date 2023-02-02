import random
from pymorphic_purple_tiger.pymorphic_purple_tiger import animal_hash

string = ''
i = 0
while i < 100:
  string += f'{random.randint(0,9)}'
  i += 1

print(animal_hash(string))