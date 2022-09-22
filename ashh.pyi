#!/usr/bin/env python3
import os
import argparse
import threading
from xml.etree.ElementTree import TreeBuilder

parser = argparse.ArgumentParser()
parser.add_argument(
    '--dir',
    dest='directory_change',
    action='append',
    nargs='?'
)
parser.add_argument(
    '--usr',
    dest='user',
    action='append',
    nargs='?'
)
parser.add_argument(
    dest='target',
    action='append',
    nargs='?'
)
args = parser.parse_args()
class dialogHandler():
    class general():
        rawInput = '%s' % (args.target)
        bracketless1 = rawInput.replace('[', '')
        bracketless2 = bracketless1.replace(']', '')
        quotes = bracketless2.replace("'", '')
        commasWspace = quotes.replace(', ', ' ')
        commas = commasWspace.replace(',', ' ')
        syscom = commas
        sysout = syscom.replace(' ', ', ')
    class user():
        rawInput = '%s' % (args.user)
        bracketless1 = rawInput.replace('[', '')
        bracketless2 = bracketless1.replace(']', '')
        quotes = bracketless2.replace("'", '')
        commasWspace = quotes.replace(', ', ' ')
        commas = commasWspace.replace(',', ' ')
        syscom = commas
        sysout = syscom.replace(' ', ', ')
    class dir():
        rawInput = '%s' % (args.directory_change)
        bracketless1 = rawInput.replace('[', '')
        bracketless2 = bracketless1.replace(']', '')
        quotes = bracketless2.replace("'", '')
        commasWspace = quotes.replace(', ', ' ')
        commas = commasWspace.replace(',', ' ')
        syscom = commas
        sysout = syscom.replace(' ', ', ')


if dialogHandler.dir.sysout != 'None':
    directory = '%s' % (
        dialogHandler.dir.sysout
    )
else:
    directory = 'home'

if dialogHandler.user.sysout != 'None':
    user = '%s' % (
        dialogHandler.user.sysout
    )
else:
    user = 'live'

parse = input(
    '''
%s::%s :: ''' % (
        user, directory
    )
)

class engine():
    def create():
        os.system(
            'touch %s/%s.script' % (
                directory, parse
            )
        )
        runner = '%s/%s.script' % (directory, parse)
    def format():
        os.system(
            'echo "#!/usr/bin/env bash" >> %s' % (
                engine.runner
            ) #could work but would be cumbersome user side so probably won't keep
              #I would like to get it working before making it better, though
        )
        os.system(
            'echo "%s" >> ~/.ash/%s.script' % (

            )
        )