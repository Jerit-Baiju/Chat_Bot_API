import basic
import engine


def run():
    print(">>> "+str(['add', 'scan']))
    main = basic.inp()
    if main == 'add':
        add = True
        f = open('dict.txt', 'r')
        dict = f.read().split()
        new = basic.sub('enter the words')
        words = new.split()
        for word in words:
            if word in dict:
                basic.out(f'the word "{word}" already exists in dict.txt')
                add = False
                break
        f.close()
        if add == True:
            f = open('dict.txt', 'r')
            read = f.readlines()
            f.close()
            initial = []
            for x in read:
                initial.append(x.split()[0])
            basic.out(str(initial))
            match = basic.sub(
                'leave blank if you need to add new synonyms, else type the synonym initial')
            if match == "":
                basic.info('set blank')
                f = open('dict.txt', 'a')
                f.write(new+"\n")
                f.close()
                basic.out('process completed')
            else:
                for x in read:
                    if x.split()[0] == match:
                        section = x
                        section = section.replace('\n', '')
                basic.info(f'section --- {section}')
                f = open('dict.txt', 'r')
                words = f.read()
                words = words.replace(section, f"{section} {new}")
                f.close()

                f = open('dict.txt', 'w')
                f.write(words)
                f.close()

    elif main in ['scan', 'check']:
        f = open('dict.txt', 'r')
        dict = f.read().split()
        new = []
        for word in dict:
            if word not in new:
                new.append(word)
            else:
                basic.out(f'the word "{word}" already exists')
        basic.out('scan finished')
        f.close()

    elif main == 'x':
        exit()

    else:
        basic.out('unknown command')
    
    engine.run()
    run()

run()
