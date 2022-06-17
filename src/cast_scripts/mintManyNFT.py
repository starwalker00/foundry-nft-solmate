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
    for x in range(1, 2):
        print(f"Iteration {x}")
        # build command
        contract = "0xb3de220de2488071fc362141a939fb6689e0c52c"
        mintTo = "0x235596F35fdeAc45a59bf38640dD68F19A85dE39"
        envCmd = ". ./.env.sh"
        castCmd = "cast send --rpc-url=$RPC_URL "+contract+" \"mintTo(address)\" "+mintTo+" --private-key=$PRIVATE_KEY"
        fullCmd = [envCmd + "&&" + castCmd]
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

