import os
import random
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(os.path.dirname(__file__))
    filename = os.path.join(base_path, 'words.txt')

with open(filename) as word_file:
    responses = word_file.read().split('\n')

# todo: add foobar

ball = """
       _.a$$$$$a._
     ,$$$$$$$$$$$$$.
   ,$$$$$$$$$$$$$$$$$.
  d$$$$$$$$$$$$$$$$$$$b
 d$$$$$$$$~'"`~$$$$$$$$b
($$$$$$$p   _   q$$$$$$$)
$$$$$$$$   (_)   $$$$$$$$
$$$$$$$$   (_)   $$$$$$$$
($$$$$$$b       d$$$$$$$)
 q$$$$$$$$a._.a$$$$$$$$p
  q$$$$$$$$$$$$$$$$$$$p
   `$$$$$$$$$$$$$$$$$'
     `$$$$$$$$$$$$$'
       `~$$$$$$$~'

{}"""
answer = 'ask a question: '
while True:
    os.system('clear')
    print(ball.format(answer))
    input('> ')
    answer = random.choice(responses)
