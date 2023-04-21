import datetime
import pytz
import basic
import data
import wikipedia


def run(main):
    intents = main.split()

    if basic.check(intents, ['time', 'tym', 'tme']) == True:
        return "The time is "+datetime.datetime.now(pytz.timezone("Asia/Kolkata")).strftime("%H:%M")

    elif basic.check(intents, ['date']) == True:
        return "the date is " + str(datetime.datetime.now(pytz.timezone("Asia/Kolkata")).date())

    elif main == 'total':
        return str(len(data.cmd.total)) + ' commands'

    elif main == 'cmds':
        cmds = []
        for cmd in data.cmd.total:
            op = f"{cmd.words} = {cmd.op}"
            cmds.append(op)
        return str(cmds)

    elif main == "x":
        exit()

    else:
        main = []
        for words in intents:
            if words not in main:
                main.append(words)
        response = data.bot(main)
        if response.op == False or response.per < 50:
            try:
                return wikipedia.summary(main, sentences=2)
            except:
                return 'no result were found on network'
        else:
            return response


while True:
    intents = input('--> ')
    bot_data = run(intents)
    try:
        op = {
            'percentage': bot_data.per,
            'op': bot_data.op
        }
        print(op)
    except:
        print(bot_data)
