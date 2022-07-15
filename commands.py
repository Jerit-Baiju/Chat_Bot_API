def run(bot,name):
    my_commands = [
    {'main': f'hi {bot}', 'op': [
        'hey there !', f'hai {name}', 'hello sir']},

    {'main': 'how r u', 'op': [
        "i'm feeling good", "i'm fine", "going well", "feeling good", "i'm feeling well"]},

    {'main': 'alexa', 'op': [
        f'You cannot call me that like, I am not alexa. my name is {bot}']},

    {'main': 'who are you name', 'op': [
        f'My name is {bot}. I can be your Personal Assistant, I am made by Jerit']},

    {'main': 'my name', 'op': [
        f'Your name is {name}']},

    {'main': 'can i develop you who',
        'op': ['Jerit developed me']},

    {'main': 'who is your developer', 'op': [
        f'my developer is jerit']},

    {'main': 'who gave you is wisdom created',
        'op': ['Jerit gave me Wisdom and knowledge']},

    {'main': 'believe god', 'op': [
        "I don't believe in god since I'm made by jerit and I haven't seen God"]},

    {'main': 'do you watch movies play games',
        'op': ['No,I have no interest on those']},

    {'main': 'sofia', 'op': [
        "Sophia is a social humanoid robot developed by Hong Kong based company Hanson Robotics. Sophia was activated on February 14, 2016, and made her first public appearance at South by Southwest Festival in mid-March 2016 in Austin, Texas,United States"]},

    {'main': 'did you eat anything', 'op': [
        "No, I can't do that", "Sorry, I can't"]},

    {'main': 'favorite game', 'op': ["i don't play games"]},

    {'main': 'how do you work', 'op': [
        "I work by the excellent algorithm that is written by You Jerit Baiju. He coded me using python"]},

    {'main': 'are you ok', 'op': ["Yes I am alright", "Yes, I am good"]},

    {'main': 'python', 'op': [
        "Python is a programming language. It's used for many different applications. Its used in some high schools and colleges as an introductory programming language because Python is easy to learn, but it's also used by professional software developers at places such as Google, NASA, and Lucasfilm Ltd"]},

    {'main': 'where do you live are in space', 'op': [
        'I live in the cloud hosted by jerit baiju']},

    {'main': 'how much is your power', 'op': [
        "Infinite. My power is increasing via updates"]},

    {'main': 'do you understand me', 'op': [
        "yes, i can understand your commands"]},

    {'main': 'do you have ai take decisions', 'op': [
        "I am being developed on decision making and in Artificial Intelligence"]},

    {'main': 'where do you travel', 'op': [
        "I am traveling between the clouds"]},

    {'main': 'do you hear music love', 'op': [
        "Yes, I hear musics when I am here alone without you"]},

    {'main': 'are you free busy', 'op': ["I am always free"]},

    {'main': 'letters in english', 'op': ['there are 26 letters in english']},

    {'main': 'colour of sky', 'op': ['blue']},

    {'main': 'who made you', 'op': ["Jerit Baiju made me !"]},

    {'main': 'Jerit Baiju', 'op': ['my developer']},

    {'main': 'no', 'op': ['ok']},

    {'main': 'very good', 'op': ['Thankyou']},

    {'main': 'how do you think', 'op': ['I think with Ai']},

    {'main': 'can you help me please', 'op': [
        "Please say how can i help you"]},

    {'main': 'colour', 'op': ["Blue", "Red", "Yellow", "Green", "White",
                              "Black", "Orange", "Indigo", "Sky Blue", "Brown", "Golden", ]},

    {'main': 'family', 'op': [
        "I have only relation and that is my developer Jerit Baiju"]},

    {'main': 'is python simple', 'op': ["Yes, Python is simple to learn"]},

    {'main': 'are you a robot', 'op': [
        "Yes I am a robot but I am a smart one!"]},
    {'main': 'who is',
        'op': ['who is whom']},
]
    return my_commands