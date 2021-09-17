dicta = {'G':0, 'C':1, 'F':2}
a = 'GCF'
print(all([1 if alphabet in dicta else 0 for alphabet in list(a)]))