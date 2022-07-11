
def sentence_maker(phrase):
    capitalized = phrase.capitalize()
    interrogatives = ("how", "what", "why", "when", "do", "does", "did", "is")
    if phrase.startswith(interrogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []
while True:
    user_input = input("Say a phrase: ")
    if user_input == "end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))
