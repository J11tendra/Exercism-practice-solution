def is_isogram(string):

    # first lets do some cleaning of the string
    # remove all the whitespace, hypens, everything except letters
    # make it lowercase

    string = string.lower()
    string = string.replace("-", '')
    string = string.replace(" ", '')

    # loop throught the string and match the letter
    for outter_letter in string:
        count=0 # letter counter
        for inner_letter in string:
            if inner_letter == outter_letter:
                count+=1

        if count >= 2:
            return False

    return True
