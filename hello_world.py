print("Hello World")
x = "Hello Python"
print(x)
y = 42
print(y)

#this file is for Python review!
'''
nothing in this line will show up
nothing in this line either
also this one or any amount of lines in between triple quotations
'''

# define a function that says hello to the name provided
# this starts a new block
def say_hello(name):
  #these lines are indented therefore part of the function
  if name:
   print 'Hello, ' + name + ' from inside the function'
  else:
   print 'No name'
# now we're unindented and have ended the previous block
print 'Outside of the function'
say_hello('Juanito')

drawer = [
  'documents',
  'envelopes',
  'pens',
  'markers'
]
# =ENUMERATE=
j = enumerate(drawer)
'''
enumerate(sequence) built in function is used in a for loop
context to return two-item-tuple for each item in the list
indicating the index followed by the value at that index.
'''

for x in j:
  print x
'''
iterating through j now returns a different tuple for item
that was in the sequence
=> (0, 'documents')
=> (1, 'envelopes')
=> (2, 'pens')
=> (3, 'markers')
'''
# =MAP=
def mashup_dog(item_in_sequence):
  mutation = 'Dog ' + item_in_sequence
  return mutation

print map(mashup_dog, drawer) 
''' 
map(function, sequence) built in function is used to apply
a specific function to every item of a sequence you pass in.
Returns a list of the results.
=> ['Dog documents', 'Dog envelopes', 'Dog pens', 'Dog markers']
'''
# =MAP=
print('min_min, ', min([2,3,4,-22,10])) # => -22
print('min_min, ', min(['cow','chicken','cows'])) # => cow

'''
min returns the lowest value in a sequence if theyre numbers
passing strings returns the first of the strings in alphabetical orders 
'''
# =SORTED=

'''
returns a sorted sequence
'''
print(sorted([5,4,6,18,19,11,9,7,3,1,2,8,10,14,16,20,12,13,15,17]))
# => [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print(sorted(['cow','china','apple','ten','bat']))
# => ['apple', 'bat', 'china', 'cow', 'ten']

'''
-v-THESE METHODS ARE SPECIFIC TO LIST ONLY-v-
'''
# =APPEND= append takes an argument and inputs it at the end of a given list

fridge = ['milk', 'carrots', 'ham', 'eggs']

fridge.append('ketchup')
print(fridge) # => ['milk', 'carrots', 'ham', 'eggs', 'ketchup']


# =EXTEND= adds all values from a second sequence to the end of the original sequence.


farm = ['cow', 'pig', 'horse']
farm_equipment = ['tractor', 'laso', 'ax', 'hammer']

farm.extend(farm_equipment)

print(farm)

# =POP= remove a value at given position. if no parameter is passed, defaults to final value in the list.


farm.pop()
print(farm) # => ['cow', 'pig', 'horse', 'tractor', 'laso', 'ax']
farm.pop(3) 
print(farm) # => ['cow', 'pig', 'horse', 'laso', 'ax']

# =INDEX=  returns the index position in a list for the given parameter.

likes = ['Kevin','Mike', 'Ricardo', 'Alex', 'David', 'Manny']

print(likes.index('Ricardo')) # => 2

# =FOR LOOPS=
for count in range(0,5):
  print"looping - ", count

'''
v The Logic Behind The For loop v
for <counter> in <sequence or range>:
  # do something
'''

rando_list = [2, 'ten', ['pizza','corn'], 'pressure', 'scream', 12, [1,2,3,4]]

for ele in rando_list:
  print(ele)

# =WHILE LOOPS=

'''
While loops are often used when we don't know how many times we have to repeat
a block of code but we know we have to do it until a certain condition is met.
Remember this for loop?
'''

count = 0
while count < 5: 
  print 'looping - ', count
  count += 1

# =BREAK=

'''
The break statement exits the current loop prematurely, resuming execution at the
first post-loop statement, just like the traditional break found in C or JavaScript.
The most common use for the break is when some external condition is triggered,
requiring a hasty exit from a loop. The breakstatement can be used in both while 
and for loop. When loops are nested, a break will only exit from the innermost loop
in which case you would use return.
'''
for val in "construction":
  if val == "i":
    break
  print val

print '======================'

list1 = ['s', 't','r','qwee','n','i','g']
list2 = ['s', 't','r','qweie','n','g']
list3 = ['s', 't','i' ,'r','qwee','n','g']
def stop_at_I(item):
  for val in item:
    for val2 in val:
      if val2 == 'i':
        return
      print val2
      
stop_at_I(list1)
print '======================'
stop_at_I(list2)
print '======================'
stop_at_I(list3)
print '======================'

# =CONTINUE=
'''
The continue statement is usefull to skip certain iterations of a loop 
and continue to the next.
'''
for val in "shopping cart":
  if val == 'p':
    continue
  print val

lst1 = ['h','o','w',' ','much',' ', 'w', 'o', 'o', 'd']
lst2 = ['c','o','u','l','d',' ','a',' ','woodchuck',' ','c','h','u','c','k']
lst3 = ['if',' ','a',' ','w','o','o','d','c','h','u','c','k',' ','could']
lst4 = ['chuck',' ','w','o','o','d','?']

def skip(letter, string):
  for val in string:
    for val2 in val:
      if val2 == letter:
        continue
      print val2
print '======================'
skip('u', lst1)
print '======================'
skip('c', lst2)
print '======================'
skip('d', lst3)
print '======================'
skip('w', lst4)
print '======================'

