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
    class linux():
        def format():
            runner = open(
                '%s/%s.sh', 'x' % (
                    directory, user
                )
            )
            engine.linux.runner.write(
                '#!/usr/bin/env bash' #still don't know how to target windows in any capacity.
            )
            engine.linux.runner.write(
                '%s' & (
                    parse
                )
            )
            runner.close()
    class win32():
        def format():
            runner = open(
                '%s.ps1', 'x' % (
                    user
                )
            )
            engine.win32.runner.write(
                '%s' % (
                    parse
                )
            )
            runner.close()