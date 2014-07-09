""" This is an implementation of l stsrems"""
#!/usr/bin/python

def yeast_model(n):
    """ Computes the l system for yeast"""
    rule = {'A':'AB', 'B':'A'}
    initiator = list('A')
    #TODO should be recursive
    for i in range(n):
        last = len(initiator)
        letter = initiator[last-1]
        sub = rule[letter]
        print "sub is "+sub
        initiator = initiator[:len(initiator)-1] + list(sub)
        print initiator
    return initiator

def head(coll):
    return coll[0]
def tail(coll):
    return coll[1:]

def lsystem(n,initiator,rules):#TODO this is a cheaty way the
    #recursive l function is wrong and needs tweeking REMOVE THIS
    #REFACTOR EVERRy THING
    result = recursiveL(n,initiator,rules)
    return "".join(result)
    
def proc(seed,acc,rules):
    if len(seed) == 0:
        return acc
    else:
        first = head(seed)
        product = list(first)
        if rules.has_key(first):
            product = list(rules[first])
        return proc(tail(seed),acc + product,rules)
        
def recursiveL(n, initiator, rules):
    if n == 0:
        return initiator
    else:
        acc = proc(initiator,[],rules)
        return recursiveL(n-1, acc, rules)
