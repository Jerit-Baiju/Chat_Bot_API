from pprint import pprint
import commands




def run():
    lines = open('story.txt', 'r').read().replace('\n','').split('.')
    # print(lines)

run()