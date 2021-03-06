try:
    # Apparently not all implementations have SystemRandom defined, so I expect
    # this import to fail, if that's the case.
    from random import SystemRandom
    randomizer = SystemRandom()
except:
    import random as randomizer

import datetime

# This alphabet removes vowels (and the letter 'V' which looks like a 'U'),
# make it very hard for this to generate words. This is for profanity
# avoidance.  It also removes characters that in poor fonts might be confusing
# such as B,8,5,S,0,O,1,I,Q

SAFE_ALPHABET_STRING = '234679CDFGHJKMNPRTWXYZ'
SAFE_ALPHABET = list(SAFE_ALPHABET_STRING)


def safe_generate(length=8):
    """This generates a random travel-style record locator using the safe
    alphabet. """

    return ''.join(randomizer.choice(SAFE_ALPHABET) for i in range(0, length))

def timestamp_generate():
    """ This uses a combination of random digits and microseconds to generate a
    unique value. This is intended to be used in instances where
    safe_generate() keep producing duplicates. """

    microsecond = datetime.datetime.now().microsecond
    remaining_length = 16 - (len(str(microsecond)) + 1)
    random = safe_generate(remaining_length)
    return '%s-%s' % (random, microsecond)
