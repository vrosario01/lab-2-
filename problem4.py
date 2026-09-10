def wears_jackets(temp, raining):
    if temp < 60 or raining:
        return True
    else:
        return False

""" wears_jackets takes in values temp and raining and only returns true if the temp < 60 or it is raining and returns false otherwise"""
>>>print(wears_jackets(80, True))
true
>>>print(wears_jackets(80, False))






