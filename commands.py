def run(bot, name):
    my_commands = [
        {"main": f"hi {bot}", "op": [
            "hey there !", f"hai {name}", "hello sir"]},
        {"main": "hi", "op": ["hey there !", f"hai {name}", "hello sir"]},
        {
            "main": "alexa",
            "op": ["i think you're getting me confused with someone else", " i know you know my real name"],
        },
        {"main": "how r u", "op": ["i'm splendid! Thank you for asking",
                                   "i'm doing alright, thanks for asking. i hope you're safe and feeling well."]},
        {
            "main": "you name",
            "op": [
                f"My name is {bot}. I can be your Personal Assistant, I am made by Jerit"
            ],
        },
        {"main": "my name", "op": [f"Your name is {name}"]},
        {"main": "can i develop you who", "op": ["Jerit developed me"]},
        {
            "main": "who is your developer",
            "op": [
                f"my developer is jerit baiju, you can reach him at https://jerit.herokuapp.com"
            ],
        },
        {
            "main": "who gave you is wisdom created",
            "op": ["Jerit baiju designed me"],
        },
        {
            "main": "believe god",
            "op": [
                "i'm still learning about religion."
            ],
        },
        {
            "main": "do you watch movies play games",
            "op": ["No,I have no interest on those"],
        },
        {
            "main": "sofia",
            "op": [
                "Sophia is a social humanoid robot developed by Hong Kong based company Hanson Robotics. Sophia was activated on February 14, 2016, and made her first public appearance at South by Southwest Festival in mid-March 2016 in Austin, Texas,United States"
            ],
        },
        {
            "main": "did you eat anything",
            "op": ["i'm already full... of information"],
        },
        {"main": "favorite game", "op": ["i don't play games"]},
        {
            "main": "how do you work",
            "op": [
                "I work by the excellent algorithm that is written by You Jerit Baiju. He coded me using python"
            ],
        },
        {"main": "are you ok", "op": ["i'm great! I hope you're having a wonderful day.",
                                      "Yes, I'm doing great. Thanks for asking.", "i'm pretty good, thanks for asking.", "i'm perfectly okay and happy to be here."]},
        {
            "main": "python",
            "op": [
                "Python is a programming language. It's used for many different applications. Its used in some high schools and colleges as an introductory programming language because Python is easy to learn, but it's also used by professional software developers at places such as Google, NASA, and Lucasfilm Ltd"
            ],
        },
        {
            "main": "where do you live are in space",
            "op": ["I live in the cloud hosted by jerit baiju"],
        },
        {
            "main": "how much is your power",
            "op": ["Infinite. My power is increasing via updates"],
        },
        {"main": "do you understand me", "op": [
            "i sure can, and i'm here if you need help with anuything"]},
        {
            "main": "take decisions",
            "op": [
                "I am being developed on decision making and in Artificial Intelligence"
            ],
        },
        {"main": "do you have ai", "op": [
            "my intelligence is artificial, it's true.", "yes, all the intelligence i have is artificial."]},
        {
            "main": "do you hear music love",
            "op": ["Yes, I hear musics when I am here alone without you"],
        },
        {"main": "are you free busy", "op": [
            "of course i am, i'm always here for you whenever you need me. "]},
        {"main": "letters in english", "op": [
            "there are 26 letters in english"]},
        {"main": "colour of sky", "op": ["blue"]},
        {"main": "who made you", "op": ["Jerit Baiju made me !"]},
        {"main": "Jerit Baiju", "op": ["my developer"]},
        {"main": "no", "op": ["ok"]},
        {"main": "very good", "op": ["Thankyou"]},
        {"main": "how do you think", "op": ["I think with Ai"]},
        {"main": "help me please", "op": [
            "Please say how can i help you"]},
        {
            "main": "family",
            "op": ["I have only relation and that is my developer Jerit Baiju"],
        },
        {"main": "is python simple", "op": ["Yes, Python is simple to learn"]},
        {"main": "are you a robot", "op": [
            "i'd prefer to think of myself as your friend. who also happens to be artificially intelligent."]},
        {"main": "who is", "op": [f"i'm your {bot}. how can i help you?"]},
        {"main": "so you r working now", "op": ["that's great"]},
        {"main": "u r awesome", "op": [
            "thanks for taking the time to chat with me - you make this job fun"]},
        {"main": "ok", "op": ["fine", "good"]},
        {"main": "fine", "op": ["cool, anything else i can do?"]},
        {"main": "thats great", "op": ["indeed!"]},
        {"main": "i'm happy", "op": [
            "yay!", "thats wonderful to hear! keep feeling happy", "i'm happy you're happy"]},
    ]
    return my_commands
