import dictionary as dict


class cmd:
    total = []

    def __init__(self, words):
        self.words = words.split()
        self.op = ''
        self.per = 0
        self.call = 0
        cmd.total.append(self)

cmd_1 = cmd('hi <<root-bot>>')
cmd_1.op = ['hey there !', 'hai <<root-name>>', 'hello sir']

cmd_2 = cmd('how r u')
cmd_2.op = ["i'm feeling good", "i'm fine", 'going well', 'feeling good', "i'm feeling well"]

cmd_3 = cmd('can i call you alexa')
cmd_3.op = ['NO you cannot, I am not alexa. my name is Abettor']

cmd_4 = cmd('who are you name')
cmd_4.op = ['My name is <<root-bot>>. I can be your Personal Assistant, I was made by Jerit']

cmd_5 = cmd('can i develop you who')
cmd_5.op = ['Jerit developed me']

cmd_6 = cmd('who gave you is your developer wisdom created developed')
cmd_6.op = ['Jerit gave me Wisdom and knowledge']

cmd_7 = cmd('do you believe in god who is your')
cmd_7.op = ["I don't believe in god since I'm made by jerit and I haven't seen God"]

cmd_8 = cmd('do you u watch movies shows films play games')
cmd_8.op = ['No,I have no interest on those']

cmd_9 = cmd('can u you do my homework')
cmd_9.op = ['No, I am being developed for chatting and AI']

cmd_10 = cmd('who is sofia')
cmd_10.op = ['Sophia is a social humanoid robot developed by Hong Kong based company Hanson Robotics. Sophia was activated on February 14, 2016, and made her first public appearance at South by Southwest Festival in mid-March 2016 in Austin, Texas,United States']

cmd_11 = cmd('did you eat anything')
cmd_11.op = ["No, I can't do that", "Sorry, I can't"]

cmd_12 = cmd('favorite game')
cmd_12.op = ["i don't play games"]

cmd_13 = cmd('how do you work')
cmd_13.op = ['I work by the excellent algorithm that is written by You Jerit Baiju. He coded me using python']

cmd_14 = cmd('are you ok')
cmd_14.op = ['Yes I am alright', 'Yes, I am good']

cmd_15 = cmd('python')
cmd_15.op = ["Python is a programming language. It's used for many different applications. Its used in some high schools and colleges as an introductory programming language because Python is easy to learn, but it's also used by professional software developers at places such as Google, NASA, and Lucasfilm Ltd"]

cmd_16 = cmd('where do you live are in space')
cmd_16.op = ['I live in the cloud hosted by jerit baiju']

cmd_17 = cmd('how much is your power')
cmd_17.op = ['Infinite. My power is increasing via updates']

cmd_18 = cmd('do you understand me')
cmd_18.op = ['yes, i can understand your commands']

cmd_19 = cmd('do you have ai take decisions')
cmd_19.op = ['I am being developed on decision making and in Artificial Intelligence']

cmd_20 = cmd('where do you travel')
cmd_20.op = ['I am traveling between the clouds']

cmd_21 = cmd('do you hear music love')
cmd_21.op = ['Yes, I hear musics when I am here alone without you']

cmd_22 = cmd('are you free busy')
cmd_22.op = ['I am always free']

cmd_23 = cmd('letters in english')
cmd_23.op = ['there are 26 letters in english']

cmd_24 = cmd('colour of sky')
cmd_24.op = ['blue']

cmd_25 = cmd('who made you')
cmd_25.op = ['Jerit Baiju made me !']

cmd_26 = cmd('jerit baiju')
cmd_26.op = ['my developer']

cmd_27 = cmd('no')
cmd_27.op = ['ok']

cmd_28 = cmd('very good')
cmd_28.op = ['Thankyou']

cmd_29 = cmd('how do you think')
cmd_29.op = ['I think with Ai']

cmd_30 = cmd('can you help me please')
cmd_30.op = ['Please say how can i help you']

cmd_31 = cmd('colour')
cmd_31.op = ['Blue', 'Red', 'Yellow', 'Green', 'White', 'Black', 'Orange', 'Indigo', 'Sky Blue', 'Brown', 'Golden']

cmd_32 = cmd('family')
cmd_32.op = ['I have only relation and that is my developer Jerit Baiju']

cmd_33 = cmd('is python simple')
cmd_33.op = ['Yes, Python is simple to learn']

cmd_34 = cmd('are you a robot')
cmd_34.op = ['Yes I am a robot but I am a smart one!']


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
