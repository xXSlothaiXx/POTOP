# POTOP TCP/UDP Flooder

This is a local TCP/UDP Flooder made with python to test open ports for local devices on wifi

### SETUP
```
pip install bcolors && pip install pyfiglet 

python potop.py
```
## GENERAL Information 

This script uses TCP and UDP sockets for sending multiple connections to a device

2 threads are utilized and create instances of TCP and UDP connection flooding

If the script is working, You should see BOTH TCP AND UDP connection messages when sending connections.

If the script is only sending UDP packets, it means that the port is not working or open. 

Be careful when testing this script on Samsung galaxy devices. The galaxy devices seem to have a protocol that disconnects from wifi if it is receiving too many pakcets. THIS SCRIPT WILL create authentication errors with wifi to the target who owns a samsung device

### I AM NOT RESPONSIPLE FOR HOW YOU USE THIS. If you are DOS'ing devices without permission, you are liable and will face legal repercussions.  
