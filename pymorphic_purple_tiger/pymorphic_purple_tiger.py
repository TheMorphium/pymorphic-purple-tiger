import hashlib
from pymorphic_purple_tiger.compress import compress
from pymorphic_purple_tiger.adjectives import adjectives
from pymorphic_purple_tiger.animals import animals
from pymorphic_purple_tiger.colors import colors

def to_styled(words, style):
    styled_words = []
    if style == 'titlecase':
        for word in words:
            styled_words.append(word.title())
    elif style == 'lowercase':
        for word in words:
            styled_words.append(word.lower())
    elif style == 'uppercase':
        for word in words:
            styled_words.append(word.upper())
    else:
        raise ValueError('Unknown style')
    return styled_words


def animal_hash(input, style='titlecase', separator=' '):
    hex_digest = hashlib.md5(input.encode(encoding = 'UTF-8', errors = 'strict')).hexdigest()
    pairs = [hex_digest[i:i+2] for i in range(0, len(hex_digest), 2)]
    bytes = [int(pair, 16) for pair in pairs]
    compressed = compress(bytes, 3)



    adjective = adjectives[compressed[0]]
    color = colors[compressed[1]]
    animal = animals[compressed[2]]
    styled_words = to_styled([adjective, color, animal], style)


    return styled_words[0] + separator + styled_words[1] + separator + styled_words[2]



