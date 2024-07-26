import os
import random 
import time

file_name = 'motto.txt'
try:
    path = os.path.dirname(os.path.abspath(__file__))

    source_handle = open(path + '/' + file_name, 'w')
    source_handle.write('Fiat Lux!\n')

except IOError:
    print("IO Error! Please check valid file names and paths")
    exit
finally:
    source_handle.close()

try: 
    source_handle = open(path + '/' + file_name, 'r')
    for line in source_handle:
        print(line)
    source_handle_append = open(path + '/' + file_name, 'a')
    source_handle_append.write("Let there be light!")
except IOError:
    print("IO Error! Please check valid file names and paths")
    exit 

finally: 
    source_handle.close()


