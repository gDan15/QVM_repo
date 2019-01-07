# QVM - Python
## Version
    Python 3.7.1
## Installed packages
    pip install pyquil
## Use
### Start servers like so:
    $ qvm -S
    $ quilc -S
### It's possible to directly write Quil in a file
     DECLARE ro BIT[1]
     RX(pi/2) 0
     CZ 0 1
### Then execute what's in it by doing so :
     $ qvm -e < example.quil
     
