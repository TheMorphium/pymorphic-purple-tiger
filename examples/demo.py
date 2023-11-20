import random
from pymorphic_purple_tiger.pymorphic_purple_tiger import animal_hash

string = ''.join(f'{random.randint(0, 9)}' for _ in range(100))
print(animal_hash(string))