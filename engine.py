from commands import run as commands
import root

def run():
    data_file = open('data.py', 'w')
    data_file.write('')
    data_file.close()
    data_file = open('data.py', 'a')
    model_file = open('model.py', 'r')
    ai_file = open('bot.py', 'r')
    dict_file = open('dictionary.py', 'w')
    dict_file.write('')
    dict_file.close()
    dict_file = open('dictionary.py', 'w')
    
    var = 0
    dict_file.write("""class words():
    total = []

    def __init__(self, synonyms):
        self.synonyms = synonyms.split()
        words.total.append(self)\n\n""")

    for words in open('dict.txt').readlines():
        word = words.split()
        strings = ' '.join(word)
        var = var + 1
        dict_file.write(f"word_{var} = words('{strings}')\n")

    dict_file.write("""\ndef run(word):
    for synonyms in words.total:
       if word in synonyms.synonyms:
           return synonyms.synonyms""")

    dict_file.close()

    var = 0
    data_file.write(model_file.read() + '\n')
    for cmd in commands(root.bot,root.name):
        var = var + 1
        main = cmd['main'].casefold()
        op = cmd['op']
        data_file.write(f"cmd_{var} = cmd('{main}')\ncmd_{var}.op = {op}\n\n")
    data_file.write('\n'+ai_file.read())
    data_file.close()
    model_file.close()
    ai_file.close()
if __name__ == "__main__":
    run()