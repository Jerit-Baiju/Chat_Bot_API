class words():
    total = []

    def __init__(self, synonyms):
        self.synonyms = synonyms.split()
        words.total.append(self)

word_1 = words('hai hi hello haai')
word_2 = words('are r')
word_3 = words('you u your')
word_4 = words('time tym tim')
word_5 = words('made create created developed develop')
word_6 = words('wisdom information knowledge')
word_7 = words('your ur')
word_8 = words('sofia sophia')
word_9 = words('anything something')
word_10 = words('game games')
word_11 = words('ok k okay')
word_12 = words('explain define')
word_13 = words('love like')
word_14 = words('song songs music musics')
word_15 = words('please plz plzz')
word_16 = words('colour color')
word_17 = words('robot bot robo')
word_18 = words('can could shall should will would')
word_19 = words('alexa jarvis clara elio elora')
word_20 = words('who what')
word_21 = words('clr clear')
word_22 = words('movies shows films')
word_23 = words('no nope nop')
word_24 = words('yes yup yep')
word_25 = words('awesome good nice')

def run(word):
    for synonyms in words.total:
       if word in synonyms.synonyms:
           return synonyms.synonyms