# passwordless entrance to clusters:
# $ ssh-keygen # (leave it without password)
# $ ssh-copy-id -i /Users/admin/.ssh/id_rsa ulisesrosasp@login.colonialone.gwu.edu
# $ ssh ulisesrosasp@login.colonialone.gwu.edu # (test it)
# source: https://askubuntu.com/questions/46930/how-can-i-set-up-password-less-ssh-login

import os
import sys
import shutil
import subprocess

frc = "scp -q -o LogLevel=QUIET -i /Users/admin/.ssh/id_rsa         -r ulisesrosasp@login.colonialone.gwu.edu:/lustre/groups/ortilab/bb1/target/{d} ."
toc = "scp -q -o LogLevel=QUIET -i /Users/admin/.ssh/id_rsa_pegasus -r {d} ulisesrosasp@pegasus.colonialone.gwu.edu:/lustre/groups/ortilab/protacanthopterygii/target"

# dirs = [
#     "Myctophidae_Lampichthys_procerus_EPLATE_49_H06",
#     "Mormyridae_Marcusenius_sanagaensis_EPLATE_58_A05"
# ]

dirs = open("target_dirs.txt", "r").readlines()

for d in dirs:
    tmp  = d.strip()
    # down
    sys.stdout.write("\n    ,   : %s\r" % tmp)
    downd = frc.format(d = tmp).split()
    subprocess.Popen(downd).communicate()
    sys.stdout.write( "Down,   : %s\r" % tmp)
    # up
    upd   = toc.format(d = tmp).split()
    subprocess.Popen(upd).communicate()
    sys.stdout.write( "Down, Up: %s" % tmp)
    shutil.rmtree(tmp)
    
sys.stdout.write("\n\n")
