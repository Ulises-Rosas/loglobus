#!/usr/bin/env python3


# passwordless entrance to clusters:
# $ ssh-keygen # (leave it without password)
# $ ssh-copy-id -i /Users/admin/.ssh/id_rsa ulisesrosasp@login.colonialone.gwu.edu
# $ ssh ulisesrosasp@login.colonialone.gwu.edu # (test it)
# source: https://askubuntu.com/questions/46930/how-can-i-set-up-password-less-ssh-login

import os
import sys
import shutil
import argparse
import subprocess

# handy default files
# COLONIAL_PATH = '/lustre/groups/ortilab/bb1/target'
# PEGASUS_PATH  = '/lustre/groups/ortilab/protacanthopterygii/target'

def getOpts():
    
    parser = argparse.ArgumentParser( 
        formatter_class = argparse.RawDescriptionHelpFormatter, 
        description = '''
                        Transfer of directories from 
                        colonialone to pegasus
                        using keys
                        ''')
    parser.add_argument('-f', '--file',
                        metavar  = "",
                        type     = str,
                        required = True,
                        help     = '[Optional] File with list of directories [Default = None]')
    parser.add_argument('-k1', '--colonial_key',
                        metavar  = "",
                        type     = str,
                        required = True,
                        help     = '[Optional] Colonial ssh key [Default = None]')
    parser.add_argument('-p1', '--colonial_path',
                        metavar  = "",
                        type     = str,
                        required = True,
                        help     = '[Optional] Path where files are at colonial one [Default = None]')
    parser.add_argument('-k2', '--pegasus_key',
                        metavar  = "",
                        type     = str,
                        required = True,
                        help     = '[Optional] Pegasus ssh key [Default = None]')
    parser.add_argument('-p2', '--pegasus_path',
                        metavar  = "",
                        type     = str,
                        required = True,
                        help     = '[Optional] Path where files are at colonial one [Default = None]')
    return parser.parse_args()

def main():  
    args = getOpts()
    
    frc = "scp -q -o LogLevel=QUIET -i {k1} -r ulisesrosasp@login.colonialone.gwu.edu:{p1}/{d} ."
    toc = "scp -q -o LogLevel=QUIET -i {k2} -r {d} ulisesrosasp@pegasus.colonialone.gwu.edu:{p2}"
    # dirs = [
    #     "Myctophidae_Lampichthys_procerus_EPLATE_49_H06",
    #     "Mormyridae_Marcusenius_sanagaensis_EPLATE_58_A05"
    # ]
    dirs = open(args.file, "r").readlines()

    for d in dirs:
        tmp  = d.strip()
        
        # down
        sys.stdout.write("\n    ,   : %s\r" % tmp)
        downd = frc.format(k1 = args.colonial_key,
                           d  = tmp,
                           p1 = args.colonial_path).split()
        subprocess.Popen(downd).communicate()
        sys.stdout.write( "Down,   : %s\r" % tmp)
        
        # up
        upd   = toc.format(k2 = args.pegasus_key,
                           d  = tmp,
                           p2 = args.pegasus_path).split()
        subprocess.Popen(upd).communicate()
        sys.stdout.write( "Down, Up: %s" % tmp)
        shutil.rmtree(tmp)

    sys.stdout.write("\n\n")
  
if __name__ == "__main__":
    main()
