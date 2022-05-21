def bot(raw):
    intents = []
    initial = 0
    initial_per = 0

    for words in raw:
        triggers = dict.run(words)
        if triggers != None:
            for trigger in triggers:
                if trigger not in intents:
                    intents.append(trigger)
        else:
            if words not in intents:
                intents.append(words)

    for command in cmd.total:
        command.per = 0
        command.call = 0

    for word in intents:
        for command in cmd.total:
            if word in command.words:
                command.call = command.call + 1
                command.per = (command.call/len(command.words)) * 100

    for command in cmd.total:
        if command.call > initial:
            initial = command.call

    if initial == 0:
        command.op = False
        return command

    for command in cmd.total:
        if command.per > initial_per:
            initial_per = command.per

    for command in cmd.total:
        if command.per == initial_per:
            return command
