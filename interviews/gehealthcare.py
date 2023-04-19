'''
conversionList  = [("A", "B", 1.1), ("A", "C", 2.1), ("A", "D", 2.64), ("B", "C", 2.0),
                   ("B", "D", 2.4), ("B", "E", 4.0), ("C", "E", 2.1), ("C", "D", 1.26), 
                   ("F", "C", 3.0), ("D", "F", 2.7), ("F", "G", 2.0)]

Write a function like calculateConversion(source, destination, conversionList), that will take a source country, destination, and the list of conversions, and returns the conversion steps, and overall conversion factor, if there is any.

calculateConversion("A", "E", conversionList) =>   [A, B, E] = 4.4,
calculateConversion("F", "D", conversionList) =>   F->C->D = 6.3
'''

# hash[A] = [("B",1.1), ("C", 2.1)]
# hash[B] = [("D",2.4), ("E", 4.0)]
def say_hello():
    print('Hello, World')

def calculateConversion(source, destination, conversionList):
    # create hashmap (O(n))
    hash = {}
    for tup in conversionList:
        if tup[0] in hash:
            hash[tup[0]].append((tup[1], tup[2]))
        else:
            hash[tup[0]] = [(tup[1], tup[2])]

    conv_steps = []
    final_conv = 1
    
    conv_steps.append(source)

    return findSteps(source, destination, final_conv, conv_steps, hash)


# hash[A] = [("B",1.1), ("C", 2.1)]
# hash[B] = [("D",2.4), ("E", 4.0)]
def findSteps(source, destination, final_conv, conv_steps, hash):
    # find list of destinations in hash[source]
    # look for desired destination
    # if not there, call for each potential step
    if source not in hash:
        conv_steps.pop()
        return (conv_steps, final_conv)
    for dest in hash[source]:
        # hash[source] is final destination
        if dest[0] == destination:
            print("found destination")
            conv_steps.append(dest[0])
            final_conv*=dest[1]
            print(conv_steps)
            return (conv_steps, final_conv)
        # hash[source] is not final destination
        else:
            conv_steps.append(dest[0])
            print(dest[0])
            print("Calling findSteps")
            final_conv*=dest[1]
            (conv_steps, final_conv) = findSteps(dest[0], destination, final_conv, conv_steps, hash)
            if conv_steps[len(conv_steps)-1] == destination:
                return (conv_steps, final_conv)
            print(conv_steps)
            conv_steps.pop()
            final_conv/=dest[1]
            #first iteraton findSteps(B, E, 1, [A], hash)
            #second iteraton findSteps(D, E, 1, [A], hash)
            #first iteraton findSteps(B, E, 1, [A], hash)

    return (conv_steps, final_conv)

conversionList  = [("A", "B", 1.1), ("A", "C", 2.1), ("A", "D", 2.64), ("B", "C", 2.0),
                   ("B", "D", 2.4), ("B", "E", 4.0), ("C", "E", 2.1), ("C", "D", 1.26), 
                   ("F", "C", 3.0), ("D", "F", 2.7), ("F", "G", 2.0)]
                   
(conv_steps, final_conv) = calculateConversion("A", "E", conversionList) 
print(conv_steps)
print(final_conv)
