import os
import argparse
import sys

#alyx's "shell"
#meant to be a wrapper for asu allowing for linux and win32 executions
#implements apm as well as other system utilties later down
#this shell is where the other functions will be parsed and then called from. 
#may need to develop "custom" parser..

def _exit(__code__):
    print(
        '%s' % (__code__)
    )
    exit()

parser = argparse.ArgumentParser()
parser.add_argument(
    '--dir',
    dest='directory',
    action='append',
    nargs='?'
)
parser.add_argument(
    '--test',
    dest='test',
    action='store_true'
)
args = parser.parse_args()
class directory():
    rawInput = args.directory
    bracketless1 = rawInput.replace('[', '')
    bracketless2 = bracketless1.replace(']', '')
    quotes = bracketless2.replace("'", '')
    commasWspace = quotes.replace(', ', ' ')
    commas = commasWspace.replace(',', ' ')
    syscom = commas
    sysout = syscom.replace(' ', ', ')


def __parser__():
    user = 'ashEll'
    cd = '%s' % (
        directory.syscom
    )
    if directory.syscom == 'None':
        cd = '\/'
    grab = input(
        '''
        Alyx's Shell
        [ash]
        
        %s :: %s -->
        ''' % (
            user, cd
        )
    )
    os.system(
        '%s' % (
            grab
        )
    )

__parser__()
