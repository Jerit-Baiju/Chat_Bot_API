class words():
    total = []

    def __init__(self, synonyms):
        self.synonyms = synonyms.split()
        words.total.append(self)

word_1 = words("hai hi hello haai")
word_2 = words("are r")
word_3 = words("you u your ur")
word_4 = words("time tym tim")
word_5 = words("made create created developed develop")
word_6 = words("wisdom information knowledge")
word_7 = words("sofia sophia")
word_8 = words("anything something")
word_9 = words("game games")
word_10 = words("ok k okay")
word_11 = words("explain define")
word_12 = words("love like")
word_13 = words("song songs music musics")
word_14 = words("please plz plzz")
word_15 = words("colour color")
word_16 = words("robot bot robo")
word_17 = words("can could shall should will would")
word_18 = words("alexa jarvis clara elio elora")
word_19 = words("who what")
word_20 = words("clr clear")
word_21 = words("movies shows films")
word_22 = words("no nope nop")
word_23 = words("yes yup yep")
word_24 = words("awesome good nice")
word_25 = words("pass passed passes")
word_26 = words("thats that's")

def run(word):
    for synonyms in words.total:
       if word in synonyms.synonyms:
           return synonyms.synonyms