from pprint import pprint
from commands import run


lines = open('story.txt', 'r').read().replace('\n','').split('.')
# print(lines)
cmds = run(bot='elio', name='jerit')
op = {"main": "ijk", "op": ["mkl"]}
cmds.append(op)
# print(cmds)
f = open('trial.py', 'w')
f.write(f'def run(bot, name):\n\tmy_commands = {cmds}\n\treturn my_commands')
