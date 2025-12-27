def response(hey_bob):
    hey_bob = hey_bob.strip()
    hey_bob = hey_bob.replace(" ", "")
    hey_bob = hey_bob.replace("'", "")

    if hey_bob == "":
        return "Fine. Be that way!"
    elif hey_bob[-1] == "?" and hey_bob[:-1].isalpha() and hey_bob[:-1].isupper():
            return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper() and hey_bob[-1] != "!":
        return "Whoa, chill out!"
    elif (hey_bob.isupper() and hey_bob[-1] == "!" and hey_bob[:-1].isalpha()):
        return "Whoa, chill out!"
    elif hey_bob[-1] == "!" and hey_bob[1:].islower():
        return "Whatever."
    elif hey_bob[-1] == "!":
        return "Whoa, chill out!"
    elif hey_bob[-1] == "?":
        return "Sure."
    else:
        return "Whatever."