#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

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
                        help     = 'File with list of directories [Default = None]')
    parser.add_argument('-g', '--globals',
                        metavar  = "",
                        type     = str,
                        default  = None,
                        help     = '[Optional] File with globals patterns [Default = None]')
    parser.add_argument('-k1', '--colonial_key',
                        metavar  = "",
                        type     = str,
                        required = True,
                        help     = 'Colonial ssh key [Default = None]')
    parser.add_argument('-p1', '--colonial_path',
                        metavar  = "",
                        type     = str,
                        required = True,
                        help     = 'Path where files are at colonial one [Default = None]')
    parser.add_argument('-k2', '--pegasus_key',
                        metavar  = "",
                        type     = str,
                        required = True,
                        help     = 'Pegasus ssh key [Default = None]')
    parser.add_argument('-p2', '--pegasus_path',
                        metavar  = "",
                        type     = str,
                        required = True,
                        help     = 'Path where files are at colonial one [Default = None]')
    return parser.parse_args()


run_string = lambda a: subprocess.Popen(a.split()).communicate()

def get_downlist(globalvar, frc):
    if globalvar:
        global_pattern = open(globalvar, "r").readlines()
        
        frc_list = []
        for g in global_pattern:
            frc_list.append( frc % ("/" + g.strip()) )
        
        return frc_list
    else:
        return [frc % ""]

def run_downlist(globalvar, down_list, directory, key1, path1):
    
    if globalvar:
        if not os.path.isdir(directory):
            os.mkdir(directory)
        
    for dl in down_list:
        
        if globalvar:
            cmd = dl.format(k1 = key1, p1 = path1,
                            d  = directory, local_d = directory)
        else:
            cmd = dl.format(k1 = key1, p1 = path1, 
                            d  = directory, local_d = ".")
            
        run_string(cmd)

def write_rest(dirs, out, done):
#     out   = "rest_" + file
    out_l = sorted(set(dirs) - set(done))
    
    with open(out, 'w') as f:
        f.writelines( out_l )

def main():  
    args = getOpts()
    
    frc = "scp -q -o LogLevel=QUIET -i {k1} -r ulisesrosasp@login.colonialone.gwu.edu:{p1}/{d}%s {local_d}"
    toc = "scp -q -o LogLevel=QUIET -i {k2} -r {d} ulisesrosasp@pegasus.colonialone.gwu.edu:{p2}"

    # dirs = [
    #     "Myctophidae_Lampichthys_procerus_EPLATE_49_H06",
    #     "Mormyridae_Marcusenius_sanagaensis_EPLATE_58_A05"
    # ]
    dirs      = open(args.file, "r").readlines()
    down_list = get_downlist(args.globals, frc)

    rest_out  = "rest_" + args.file
    done      = []

    for d in dirs:

        tmp  = d.strip()
        
        # down
        sys.stdout.write("\n")
        sys.stdout.write("    ,     : %s\r" % tmp)
        sys.stdout.flush()

        run_downlist(
         globalvar = args.globals,
         down_list = down_list,
         directory = tmp,
         key1      = args.colonial_key,
         path1     = args.colonial_path
        )
        sys.stdout.write("Pull,     : %s\r" % tmp)
        sys.stdout.flush()

        
        # up
        run_string(
            toc.format(
                d  = tmp,
                k2 = args.pegasus_key,
                p2 = args.pegasus_path
            )
        )
        sys.stdout.write("Pull, Push: %s\r" % tmp)
        sys.stdout.flush()
        shutil.rmtree(tmp)

        done += [d]
        write_rest(dirs, rest_out, done)

    sys.stdout.write("\n\n")
    os.remove(rest_out)
  
if __name__ == "__main__":
    main()
