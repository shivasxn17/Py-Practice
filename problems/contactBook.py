# Enter your code here. Read input from STDIN. Print output to STDOUT

import os
import sys


if __name__ == '__main__':
    output = open(os.environ['OUTPUT_PATH'],'w')

    n = int(input()) # no of entries in notebook
    notebook = {}

    for each in range(n):
        contact = input().split(" ")
        notebook[contact[0]] = contact[1]

    input_given = True
    while input_given:
        query_name = input()
        if query_name != None:
            if query_name in notebook:
                output.write(query_name + "=" + str(notebook[query_name]) + '\n')
            else:
                output.write("Not found\n")
        else:
            input_given = False