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
cmd_3.op = ['NO you cannot, I am not alexa. my name is <<root-bot>>']

cmd_4 = cmd('can i')
cmd_4.op = ['no you cannot']

cmd_5 = cmd('who are you name')
cmd_5.op = ['My name is <<root-bot>>. I can be your Personal Assistant, I am made by Jerit']

cmd_6 = cmd('my name')
cmd_6.op = ['Your name is <<root-name>>']

cmd_7 = cmd('can i develop you who')
cmd_7.op = ['Jerit developed me']

cmd_8 = cmd('who is your developer')
cmd_8.op = ['my developer is jerit']

cmd_9 = cmd('who gave you is wisdom created')
cmd_9.op = ['Jerit gave me Wisdom and knowledge']

cmd_10 = cmd('believe god')
cmd_10.op = ["I don't believe in god since I'm made by jerit and I haven't seen God"]

cmd_11 = cmd('do you watch movies play games')
cmd_11.op = ['No,I have no interest on those']

cmd_12 = cmd('can u do my homework')
cmd_12.op = ['No, I am being developed for chatting and AI']

cmd_13 = cmd('sofia')
cmd_13.op = ['Sophia is a social humanoid robot developed by Hong Kong based company Hanson Robotics. Sophia was activated on February 14, 2016, and made her first public appearance at South by Southwest Festival in mid-March 2016 in Austin, Texas,United States']

cmd_14 = cmd('did you eat anything')
cmd_14.op = ["No, I can't do that", "Sorry, I can't"]

cmd_15 = cmd('favorite game')
cmd_15.op = ["i don't play games"]

cmd_16 = cmd('how do you work')
cmd_16.op = ['I work by the excellent algorithm that is written by You Jerit Baiju. He coded me using python']

cmd_17 = cmd('are you ok')
cmd_17.op = ['Yes I am alright', 'Yes, I am good']

cmd_18 = cmd('python')
cmd_18.op = ["Python is a programming language. It's used for many different applications. Its used in some high schools and colleges as an introductory programming language because Python is easy to learn, but it's also used by professional software developers at places such as Google, NASA, and Lucasfilm Ltd"]

cmd_19 = cmd('where do you live are in space')
cmd_19.op = ['I live in the cloud hosted by jerit baiju']

cmd_20 = cmd('how much is your power')
cmd_20.op = ['Infinite. My power is increasing via updates']

cmd_21 = cmd('do you understand me')
cmd_21.op = ['yes, i can understand your commands']

cmd_22 = cmd('do you have ai take decisions')
cmd_22.op = ['I am being developed on decision making and in Artificial Intelligence']

cmd_23 = cmd('where do you travel')
cmd_23.op = ['I am traveling between the clouds']

cmd_24 = cmd('do you hear music love')
cmd_24.op = ['Yes, I hear musics when I am here alone without you']

cmd_25 = cmd('are you free busy')
cmd_25.op = ['I am always free']

cmd_26 = cmd('letters in english')
cmd_26.op = ['there are 26 letters in english']

cmd_27 = cmd('colour of sky')
cmd_27.op = ['blue']

cmd_28 = cmd('who made you')
cmd_28.op = ['Jerit Baiju made me !']

cmd_29 = cmd('jerit baiju')
cmd_29.op = ['my developer']

cmd_30 = cmd('no')
cmd_30.op = ['ok']

cmd_31 = cmd('very good')
cmd_31.op = ['Thankyou']

cmd_32 = cmd('how do you think')
cmd_32.op = ['I think with Ai']

cmd_33 = cmd('can you help me please')
cmd_33.op = ['Please say how can i help you']

cmd_34 = cmd('colour')
cmd_34.op = ['Blue', 'Red', 'Yellow', 'Green', 'White', 'Black', 'Orange', 'Indigo', 'Sky Blue', 'Brown', 'Golden']

cmd_35 = cmd('family')
cmd_35.op = ['I have only relation and that is my developer Jerit Baiju']

cmd_36 = cmd('is python simple')
cmd_36.op = ['Yes, Python is simple to learn']

cmd_37 = cmd('are you a robot')
cmd_37.op = ['Yes I am a robot but I am a smart one!']

cmd_38 = cmd('who is')
cmd_38.op = ['who is whom']


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
