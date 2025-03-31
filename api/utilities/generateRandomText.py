import random, string

def generateRandomText(length = 32):
    """
    GENERATES A RANDOM STRING WITH AT LEAST 1 NUMBER AND 1 SPECIAL CHARACTER.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    result = []

    # ENSURE AT LEAST ONE NUMBER AND ONE SPECIAL CHARACTER
    result.append(random.choice(string.digits))
    result.append(random.choice(string.punctuation))

    # FILL THE REMAINING CHARACTERS
    remaining_length = length - 2
    if remaining_length > 0:
        result.extend(random.choice(characters) for _ in range(remaining_length))

    # SHUFFLE THE RESULT TO MIX THE CHARACTERS
    random.shuffle(result)
    return ''.join(result)

print(generateRandomText())