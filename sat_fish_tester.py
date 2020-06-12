import sys
import csv
import random
import time
import importlib
from math import comb
sys.path.append(".")
import sat_fish_processor

num_vars = [4]
num_expr = [4,5,6,7,8,9,10]
num_constr = [4,5]
var_names = ["x0","x1","x2","x3","x4","x5","x6","x7","x8","x9","x10","x11","x12","x13","x14","x15"]
filename = ""
for v in num_vars:
    for e in num_expr:
        for c in num_constr:    
            elapsed = 0
            print("Processing " + str(v) + " variables, " + str(e) + " expressions " + str(c) + " constraints.")
            filename = "./input" + str(v) + str(e) + str(c) + ".csv"
            with open("./input" + str(v) + str(e) + str(c) + ".csv","w",newline = '') as csvfile:
                filewriter = csv.writer(csvfile,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                #write the variable names
                filewriter.writerow(var_names[:int(v)])
                #write the number of variables and the number of expressions in this file
                filewriter.writerow([str(v),str(e)])
                #write the expressions to be minimized
                for i in range(0,e,1):
                    row = []
                    #minimum value for this expression
                    row.append(round(random.uniform(-1,0),3))
                    #expression definition
                    for j in range(0,comb(v + 2, 2),1):
                        row.append(round(random.uniform(-1,1),3))
                    #maximum value for this expression
                    row.append(round(random.uniform(0.01,1),3))
                    filewriter.writerow(list(map(str,row)))
                #write the constraints
                for i in range(0,c):
                    row = []
                    #minimum for this constraint
                    row.append(round(random.uniform(-1,0),3))
                    #constraint defintion
                    for j in range(0,v+1,1):
                        row.append(round(random.uniform(-1.0*random.uniform(0,1),random.uniform(0,1)),3))
                    #maximum for this constraint
                    row.append(round(random.uniform(0.01,1),3))
                    filewriter.writerow(list(map(str,row)))
                    
            t0 = time.perf_counter_ns()
            out = sat_fish_processor.processor(filename)
            t1 = time.perf_counter_ns()
            elapsed = round((t1 - t0)/1000000, 5)
            with open("./results.csv","a",newline = '') as csvfile:
                filewriter = csv.writer(csvfile,delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                filewriter.writerow([str(v), str(e), str(c), elapsed,str(out)])
            











        

