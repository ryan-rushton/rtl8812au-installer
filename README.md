# rtl8812au-installer
Installer/reloader for the rtl8812au wireless driver (https://github.com/gnab/rtl8812au)
--------------------------------------
What is this?
-------------------------------
The installer that came with the gnab driver never really cut it for me. I always had the problem that I needed to physically remove and plug in the the wifi device after an install and sometimes after a reboot.

What it does?
--------------------------------
This python script will install unzip the package, place the driver in the net/wireless folder, and inserts the driver, removes it and then inserts it again. I found this fixed my problems of needing to reinsert the physical wifi device. 

How to use it.
-----------------------------------
1) Place in the same directory as the rtl8812au-master.zip file.

2) It needs to be run as root and needs either install (for a full install) or a reload (to reload the module, the insert, remove insert process I described) as a command line parameter. 

3) To run use 
  `sudo ./installWifiDriver install` or `sudo ./installWifiDriver reload` 
from the directory where it has been placed.

A nice customisation, should you choose to, would be to place it in /usr/bin and then hardcode the location of your rtl8812au-master.zip file so that it can be run from any directory.
