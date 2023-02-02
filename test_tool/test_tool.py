from pymorphic_purple_tiger import animal_hash
from pymorphic_purple_tiger import compress
from pymorphic_purple_tiger import adjectives
from pymorphic_purple_tiger import colors
from pymorphic_purple_tiger import animals
from pymorphic_purple_tiger.pymorphic_purple_tiger import animal_hash

def describe_anmial_hash():
    print('should turn arbitrary string input into an animal hash')
    expect_val = 'Rapid Grey Rattlesnake'
    print(animal_hash('my ugly input string') == expect_val)

    print('should use a specified separator')
    expect_val = 'Rapid-Grey-Rattlesnake'
    print(animal_hash('my ugly input string', separator='-') == expect_val)

    print('should support lowercased style')
    expect_val = 'rapid grey rattlesnake'
    print(animal_hash('my ugly input string', style='lowercase') == expect_val)

    print('should support uppercased style')
    expect_val = 'RAPID GREY RATTLESNAKE'
    print(animal_hash('my ugly input string',style='uppercase') == expect_val)

    print('should throw an error if passed an unknown style')
    try:
        animal_hash('xyz', style='garbage')
    except:
        print('/Unknown style/')


def describe_compress():
    print('compresses an md5 hash into an array of requested length integers')
    bytes = [ 23, 45, 234, 111, 46, 165, 33, 58, 156, 140, 91, 138, 50, 245, 103, 210 ]
    compressed = [ 145, 174, 163 ]
    print(compress(bytes, 3) == compressed)

    print('should throw an error if given fewer bytes than requested output')
    try:
        compress([ 23 ], 3)
    except:
        print('/Fewer input bytes/')

def describe_wordlist():
    print('should contain no duplicate entries')
    word_list = adjectives + colors + animals
    word_count = len(word_list)
    test_list, dupes = [], False
    for word in word_list:
        if word not in test_list:
            test_list.append(word)
        else:
            dupes = True
            print(f'{word} is a duplicate')
    print(word_count)
    print(word_count == (256 * 3))
    if not dupes:
        print('No duplicates found')

    # There are in fact a number of duplicates.  In order to keep this library identical to the Helium library
    # Those duplicates will remain until that library is updated.


describe_anmial_hash()
describe_compress()
describe_wordlist()