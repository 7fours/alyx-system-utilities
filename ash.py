#!/usr/bin/env python3
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

parser = argparse.ArgumentParser()
parser.add_argument(
    '--dir',
    dest='directory',
    action='append',
    nargs='?'
)
args = parser.parse_args()
if args.directory == None:
    working_dir = '~'
else:
    _dir = '%s' % (
        args.directory
    )
    bracketless1 = _dir.replace('[', '')
    bracketless2 = bracketless1.replace(']', '')
    quotes = bracketless2.replace("'", '')
    commasWspace = quotes.replace(', ', ' ')
    commas = commasWspace.replace(',', ' ')
    working_dir = commas.replace(' ', ', ')

class frontend():
    def __parser__():
        user = 'aShell'
        grab = input( #use grab to write a shell script to then execute
    '''
        Alyx's Shell [ash]
            
    %s :: %s -->  ''' % (
                user, working_dir
            )
        )
    def __format__():
        trigger = '~/.ash/%s.tmp' % (
            frontend.grab
        )
        trigger_opened = os.open(
            '~/.ash/%s' % (
                trigger
            )
        )
        trigger_opened = os.write('#!/usr/bin/env bash')
        trigger_opened.close
        # os.system(
        #     'echo "#!/usr/bin/env bash" >> %s' % (
        #         trigger
        #     )
        # )
        os.system(
            'sudo chmod +x ~/.ash/%s.tmp' % (
                frontend.grab
            )
        )
    def __trigger__():
        os.system(
            '~/.ash/%s.tmp' % (
                frontend.grab
            )
        )
        os.remove(
            '~/.ash/%s.tmp' % (
                frontend.grab
            )
        )
    _exit(__code__=1)

    __parser__()
