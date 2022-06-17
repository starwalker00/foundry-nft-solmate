#!/usr/bin/python3
"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

import subprocess

def main():
    """ Main entry point of the app """
    for x in range(1, 12):
        print(f"Iteration {x}")
        # build command
        contract = "0x227a705c89254e7eba4187081c15a480506598f3"
        mintTo = "0x235596F35fdeAc45a59bf38640dD68F19A85dE39"
        envCmd = ". ./.env.sh"
        castCmd = "cast send --rpc-url=$RPC_URL --value 0.012ether "+contract+" \"mintTo(address)\" "+mintTo+" --private-key=$PRIVATE_KEY"
        fullCmd = [envCmd + "&&" + castCmd]
        print(fullCmd)
        proc = subprocess.Popen(fullCmd,stdout=open('python_logs.txt', 'a'),stderr=subprocess.PIPE, text=True, shell=True)

        # handle stuck proc/tx with timeout
        try:
            outs, errs = proc.communicate(timeout=15)
        except subprocess.TimeoutExpired:
            proc.kill()
            outs, errs = proc.communicate()

        # handle errors, break on first one
        if len(errs)>0:
            print("ERROR---------------------")
            print(errs)
            return -1

    print("ALL DONE")
    return 0

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()

