import itertools
import sys
import re
from pysmt.smtlib.printers import SmtPrinter, SmtDagPrinter, quote
import pysmt.simplifier
import pysmt.smtlib
from pysmt.shortcuts import Symbol, And, GE, LT, Plus, Times,Equals, Int, Real, get_model, Min, Max
from pysmt.typing import INT, REAL


def readfile(file_path, var_str, coefficients, mins, maxes, constraint_terms,num_vars, num_expr, eqn_mins, eqn_maxes):
  file_obj = open(file_path,"r")
  i = 0
  for line in file_obj:
    #if i == 0 then we are parsing the line that holds the variables
    if(line == '\n' or line == ''):
      break
    if(i == 0):
      for var in line.strip().split(","):
        var_str.append(var)
      print("\tDefined Variables from input.txt:")
      for var in var_str:
        print("\t\t",var)
    #if i == 1 then we are parsing the line that holds number of variables and expressions
    elif(i == 1):
      nums = line.strip().split(",")
      num_vars.append(int(nums[0]))
      num_expr.append(int(nums[1]))
      print("\tnumber of variables: %s" % str(nums[0]))
      print("\tnumber of expressions: %s" % nums[1])
    #if i>num_expr then we ar parsing constraints
    elif(i > num_expr[0]+1):
      terms = line.strip().split(",")
      mins.append(float(terms[0]))
      coeffs = []
      #+1 is for the constant term in the linear constraint
      for k in range(1,num_vars[0]+2):
        coeffs.append(float(terms[k]))
      constraint_terms.append(coeffs)
      maxes.append(float(terms[num_vars[0]+2]))
    else:
      coeffs = line.strip().split(",")
      cs = []
      k = 0
      for coeff in coeffs:
        if(k == 0):
          eqn_mins.append(coeff)
        elif(k == len(coeffs) - 1):
          eqn_maxes.append(coeff)
        else:
          cs.append(coeff)
        k = k + 1

      coefficients.append(cs)
    i = i+1


def processor(config_file_name):
  var_str = []
  coefficients = []
  constrnt_mins = []
  constrnt_maxes = []
  constraint_terms = []
  num_vars = []
  num_expr = []
  terms = []
  eqn_mins = []
  eqn_maxes = []

  readfile(config_file_name,var_str,coefficients, constrnt_mins, constrnt_maxes, constraint_terms, num_vars, num_expr, eqn_mins, eqn_maxes)
  nvars = num_vars[0]
  nexpr = num_expr[0]
  symbols = [Symbol(X,REAL) for X in sorted(var_str)]
  symbols.append(Symbol("c",REAL))

  for x in itertools.combinations_with_replacement(symbols, 2):
    terms.append(x)
  for i in range(0,len(terms),1):
    terms[i] = list(terms[i])
  for i in range(0,len(terms),1):
    if(Symbol("c",REAL) in terms[i]):
      terms[i].remove(Symbol("c",REAL))
  # [('x1', 'x1'), ('x1', 'x2'), ('x1', 'c'), ('x2', 'x2'), ('x2', 'c'), ('c', 'c')]
  sorted(terms,key=lambda elem: elem[0])
  #print(terms)
  variables = set(symbols)
  d = []
  j = 0
  for CONSTRAINT in constraint_terms:
    C = []
    for i in range(0,len(CONSTRAINT),1):
      if(symbols[i] == Symbol("c",REAL)):
        C.append(Real(CONSTRAINT[i]))
      else:
        C.append(Times(Real(CONSTRAINT[i]),symbols[i]))
    C = Plus(C)
    d.append(And(GE(C,Real(constrnt_mins[j])),LT(C,Real(constrnt_maxes[j]))))
    j = j + 1

  domains = And(d)
  eqns = []
  i = 0
  for expr in coefficients:
    cur = []
    j = 0
    for term in expr:
      if(len(terms[j]) == 2):
        cur.append(  Times(Real(float(term)),Times(terms[j])) )
      elif(Symbol("c",REAL) in terms[j]):
        cur.append( Real(float(term)) ) 
      else:
        cur.append(Times(Real(float(term)),terms[j][0]))
      j= j+1
    cur = Plus(cur)
    eqns.append(cur)
    i= i+1
  formulas = []
  models = []
  satisfiable = bool(True)
  i = 0
  for eqn in eqns:
    p0 = And(domains,GE(Min(eqn),Real(float(eqn_mins[i]))))
    p1 = And(domains,LT(Max(eqn),Real(float(eqn_maxes[i]))))
    formulas.append(p0)
    formulas.append(p1)
    models.append(get_model(p0))
    models.append(get_model(p1))
    i = i + 1
  out_str = ""
  i = 0
  j = 0
  postfix = ["min satisfiability", "max satisfiability"]
  pat = re.compile(r'\d+/\d+')
  for model in models:
    print("\tModel {} {}: ".format(str(i),postfix[j % 2]))
    #formula_str = model.print#str(formulas[i].serialize())  
    cur_str =  pysmt.shortcuts.simplify(formulas[j]).serialize().replace("&","\n\t\t\t&")
    cur_str = re.sub(pat, lambda match: "{0}".format(str(float(str(match.group()).split("/")[0])/float(str(match.group()).split("/")[1]))), cur_str)

    if model:
      print("\t\tSerialization of the formula:")

      print("\t\t\t"+cur_str)
      
      #temp_strs = formula_str.split("&")
      #for k in range(1,len(temp_strs)):
      #  temp_strs[k] = "& " + temp_strs[k] 
      #formula_strs = []
      #for s in temp_strs:
      #  t = s.split(" + ")
      #  ts = []
      #  ts.append(t[0])
      #  for k in range(1,len(t)):
      #    ts.append(" + " + t[k])
      #  new_t = [a+b+c+d for a,b,c,d in zip(*[iter(ts)]*4)]
      #  final = ""
      #  for k in range(len(ts) - (len(ts) % 4), len(ts),1):
      #    final = final + ts[k]
      #  new_t.append(final)
      #  formula_strs.append(new_t)
      
      #for s in formula_strs:
      #  print("\t\t\t%s" % s)
      print("\t\tSolution: ")
      model_str = str(model)
      model_str = model_str.replace("\n","\n\t\t\t")
      print("\t\t\t%s" % model_str)
    else:
      print("\t\tSerialization of the formula: ")
      print("\t\t\t%s" % cur_str)
      print("\t\tNo solution found")
      satisfiable = False
    if j % 2 == 1:
      i = i+1
    j = j + 1
  print("\tResult: ")
  if(satisfiable):
    print("\t\tThe problem is satisfiable using the solutions given.")
  else:
    print("\t\tThe problem is not satisfiable")
  
  return satisfiable

  #eqn = Plus(Real(-0.998), Times(Real(0.579),symbols[0]), Times(Real(0.022),Times(symbols[0],symbols[0])))
  #problem = GE(eqn,Real(0)) #And(Equals(sum_hello, sum_world),
            #    Equals(sum_hello, Int(25)))
  #formula = And(domains, problem)


