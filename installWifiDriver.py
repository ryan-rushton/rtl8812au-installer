#!/usr/bin/python3

import os
import getpass
import platform
import shutil
import subprocess
import sys
import time
import zipfile

if getpass.getuser() != 'root':
    print('This must be run as root')
    sys.exit()

if len(sys.argv) == 1 or sys.argv[1] not in ['install', 'reload']:
    print('Use arguement \'reload\' to reload the driver and \'install\' to ' +
          'do a full install')
    sys.exit()

if sys.argv[1] == 'install':
    if os.path.isdir(os.path.join(os.getcwd(), 'rtl8812au-master')):
        shutil.rmtree('rtl8812au-master')

    if not os.path.isfile('rtl8812au-master.zip'):
        print('This must be run from the dir that contains the ' +
              'rtl8812au-master.zip file')
        sys.exit()

    os.mkdir('rtl8812au-master')

    print('Extracting files')
    z = zipfile.ZipFile(os.path.join(os.getcwd(), 'rtl8812au-master.zip'))
    z.extractall(os.getcwd())
    z.close()

    os.chdir('rtl8812au-master')

    print('Starting make')
    subprocess.Popen('make').wait()
    shutil.copy('8812au.ko', '/lib/modules/' + platform.release() +
                '/kernel/drivers/net/wireless/8812au.ko')
    subprocess.Popen('depmod').wait()

    os.chdir('..')

    if os.path.isdir(os.path.join(os.getcwd(), 'rtl8812au-master')):
        shutil.rmtree('rtl8812au-master')

lsmod = subprocess.Popen(['lsmod'], stdout=subprocess.PIPE)
std_out, std_err = lsmod.communicate()

print('Inserting module')
if b'8812au' in std_out:
    subprocess.Popen(['rmmod', '8812au.ko']).wait()
    subprocess.Popen(['insmod', '/lib/modules/' + platform.release() +
                      '/kernel/drivers/net/wireless/8812au.ko']).wait()
else:
    subprocess.Popen(['insmod', '/lib/modules/' + platform.release() +
                      '/kernel/drivers/net/wireless/8812au.ko']).wait()
    subprocess.Popen(['rmmod', '8812au.ko']).wait()
    subprocess.Popen(['insmod', '/lib/modules/' + platform.release() +
                      '/kernel/drivers/net/wireless/8812au.ko']).wait()
