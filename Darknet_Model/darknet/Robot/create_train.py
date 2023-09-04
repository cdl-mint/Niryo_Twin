#!/usr/bin/python

import os

#start editable vars
outputfile	= 'test.txt'	    # file to save the results to
folder		= './test'		# the folder to inventory
#end editable vars

#print ("xyz")

with open(outputfile, "w") as txtfile:
    for path,dirs,files in os.walk(folder):   
        for filename in sorted(files):           
          if filename.endswith('.jpg'):           
            txtfile.write("Robot/Data/%s\n" % filename)    
    
txtfile.close()
