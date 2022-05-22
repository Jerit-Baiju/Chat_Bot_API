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

    else:
        main = []
        for words in intents:
            if words not in main:
                main.append(words)
        response = data.bot(main)
        if response.op == False:
            try:
                return wikipedia.summary("Wikipedia")
            except:
                return 'no result were found on network'
        else:
            return response.op

