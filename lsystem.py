

class lsystem:

    def __init__(self):
        self.rules = {}
        self.rules['A'] = 'AB'
        self.rules['B'] = 'A'
        self.rules['F'] = 'F-F+F+F-F'
    
    def head(self,coll):#TODO make private
        """
        
        Always returns the first element of a collection such that
        
        a = [1, 2, 3]
        head(a) === 1

        """
        return coll[0]
    def tail(self,coll):
        """
        
        Returns the tail of a collection which is the collection without its first element, designed to be used in
        conjunction with the head function for better recursive programming

        """

        return coll[1:]
    
    def rewrite_system(self,seed,acc):
        """

        Rewrites one word in parallel. The seed is the word to be rewritten IE. A or AB such that
        A becomes AB and AB becomes ABA, acc holds the new word that is build up through the recursive function
        calls. Every thing must be a list such that the seed must be a list of string characters and the acc must
        be an empty list.

        """
        if len(seed) == 0:
            return acc
        else:
            first = head(seed)
            product = list(first)
            if self.rules.has_key(first):
                product = list(self.rules[first])
            return rewrite_system(tail(seed),acc + product)

    def compute_system(self,n, initiator):
        """
        
        Computes a whole lsystem expansion of an axiom or seed this is the initator according to a set of rules
        for a predefined limit of expansions as specified by the parameter n, n is the number of times this should
        expand the axiom to produce a complete l system

        """
        if n == 0:
            return initiator
        else:
            acc = rewrite_system(initiator,[])
            return compute_system(n-1, acc)
