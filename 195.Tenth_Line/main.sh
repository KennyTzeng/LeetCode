#!/bin/bash
# Read from the file file.txt and output the tenth line to stdout.

lc=`wc -l < file.txt`                  
                                
if (( $lc >= 10 ));
then
    head -n 10 file.txt | tail -n 1
fi                              