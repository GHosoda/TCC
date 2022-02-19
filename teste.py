from inspect import getmembers, isfunction

import funcoes
x = (getmembers(funcoes, isfunction))
y = [i[0] for i in x]
