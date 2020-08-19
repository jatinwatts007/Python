thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
thisset.update(["orange", "mango", "grapes"])
print(len(thisset))
thisset.remove("banana")
thisset.discard("banana")
x = thisset.pop()
print(x)
thisset.clear()
del thisset
for x in thisset:
  print(x)
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
