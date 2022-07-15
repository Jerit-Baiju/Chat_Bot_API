import main

while True:
    intents = input("--> ")
    data = main.run(intents)
    try:
        op = {
            'percentage': data.per,
            'op': data.op
        }
    except:
        print(data)