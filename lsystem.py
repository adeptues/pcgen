
class Lsystem:
    
    #constants do not modify
    KOCH_CURVE = "KOCH_CURVE"
    DRAGON = "DRAGON"
    F_PLANT = "FRACTAL_PLANT"

    def __init__(self,system_type):
        self.rules = {}

        if system_type is Lsystem.KOCH_CURVE:
            self.axiom = "F"
            self.rules['F'] = 'F+F-F-F+F'
        elif system_type is Lsystem.DRAGON:
            self.rules['X'] = 'X+YF'
            self.rules['Y'] = 'FX-Y'
            self.axiom = 'FX'
        elif system_type is Lsystem.F_PLANT:
            raise NotImplementedError("The fractal plant is not implemented yet!")
        else:
            raise Exception('Must have a valid system type')
            

        
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
    
    def rewrite_system(self,seed,acc = []):
        """

        Rewrites one word in parallel. The seed is the word to be rewritten IE. A or AB such that
        A becomes AB and AB becomes ABA, acc holds the new word that is build up through the recursive function
        calls. Every thing must be a list such that the seed must be a list of string characters and the acc must
        be an empty list.

        """
        if len(seed) == 0:
            return acc
        else:
            first = self.head(seed)
            product = list(first)
            if self.rules.has_key(first):
                product = list(self.rules[first])
            return self.rewrite_system(self.tail(seed),acc + product)

    def rewrite_system_alt(self,seed,acc=[]):
        """
        
        This is the alternate non recursive implementation on rewrite system
        """
        for i in range(len(seed)):
            first = self.head(seed)
            product = list(first)
            if self.rules.has_key(first):
                product = list(self.rules[first])
            acc = acc+product
            seed  = self.tail(seed)
        return acc
            #TODO update so doesnt change function args as sideeffects
    def compute_system_alt(self,n,initiator=""):
        """
        
        This is the alternate implementation of compute_system that uses good old iteration, while this algorithm
        is a genuine recursive one it should still work find and avoid pythons limit on recursion

        """
        for i in range(n):
            if initiator is '':
                initiator = self.axiom
            initiator = self.rewrite_system_alt(initiator)
        return "".join(initiator)
                
    def compute_system(self,n,initiator = ""):
        """
        
        Computes a whole lsystem expansion of an axiom or seed this is the initator according to a set of rules
        for a predefined limit of expansions as specified by the parameter n, n is the number of times this should
        expand the axiom to produce a complete l system

        THIS IS DEPRACATED AS NO TAIL  CALL OPTIMISATION
        """
        if n == 0:
            return "".join(initiator)
        else:
            if initiator is '':
                initiator = self.axiom
            acc = self.rewrite_system(initiator)
            return self.compute_system(n-1, acc)
