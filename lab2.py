class MyClass:
    def __init__ (self, mydict):
        self.mydict = mydict
    def keysum (self, a, b):
        c = self.mydict.get(a, 0)
        if c==0: print("Key", a, "does not exist")
        else: print("The sum of the elements of the list-value with the", a, "key is", sum(c))
        d = self.mydict.get(b, 0)
        if d==0: print("Key", b, "does not exist")
        else: print("The sum of the elements of the list-value with the", b, "key is", sum(d))
        if c!=0 and d!=0: print ("The sum of the elements of both value lists is", sum(c)+sum(d))
        print()

# Lists-values in these dictionaries contain integers, so their sum can be zero
# However, a zero in the program is also displayed when there are no string keys in the dictionary
# So I preferred just verbal output in case of missing key (to avoid ambiguity)
# Also, I did not really understand the task: if both keys are present, you need to display the sum of the elements of the lists individually or jointly
# Therefore, I have provided for both cases, as well as a situation when one of the entered keys exists, and the other does not

ex1 = MyClass({'one': [1, 10, 100], 'two': [2, 20, 200], 'three': [3, 30, 300], 'for': [4, 40, 400]})
ex2 = MyClass({'a': [12, 13], 'asd': [10, 20, 30, 40], 'qw': [600]})
ex3 = MyClass({'gerb': [12, -20, 3, 2, 3], 'flag': [-10, -5], 'gimn': [7, 8]})
# An example of the presence of both keys
ex1.keysum('one', 'two')
# An example of the absence of the first key
ex1.keysum('zero', 'for')
# An example of the presence of both keys
ex2.keysum('qw', 'asd')
# An example of the absence of the second key
ex2.keysum('a', 'b')
# An example of missing of both keys
ex2.keysum('zx', 'cv')
# An example of zero sum of elements for one of the value lists
ex3.keysum('gerb', 'flag')
# An example of zero joint sum of items for two lists of values
ex3.keysum('gimn', 'flag')