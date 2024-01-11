def pig_latin(text):
    say = []
    words = text.split()
    for word in words:
        word = word[1:] + word[0] + "ay"
        say.append(word)
    return " ".join(say)

print(pig_latin(input("")))