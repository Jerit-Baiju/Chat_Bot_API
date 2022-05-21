class words():
    total = []

    def __init__(self, synonyms):
        self.synonyms = synonyms.split()
        words.total.append(self)

word_1 = words('hai hi hello hay')
word_2 = words('are r is was')
word_3 = words('you u your')
word_4 = words('time tym')
word_5 = words('develop developed')
word_6 = words('wisdom information knowledge')
word_7 = words('your ur')
word_8 = words('sofia sophia')
word_9 = words('anything something')
word_10 = words('game games')
word_11 = words('ok k')
word_12 = words('explain define')
word_13 = words('love like')
word_14 = words('song songs music musics')
word_15 = words('made create created')
word_16 = words('please plz plzz')
word_17 = words('colour color')
word_18 = words('robot bot robo')
word_19 = words('can could shall should will would')
word_20 = words('alexa jarvis clara elio elora')
word_21 = words('who what')

def run(word):
    for synonyms in words.total:
       if word in synonyms.synonyms:
           return synonyms.synonyms