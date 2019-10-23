# -*- coding: utf-8 -*-
"""

PROBABILISTIC GRAPHICAL MODEL ASSIGNMENT

"""

class PGM():
    """

    This class represents a probabilistic graphical model (PGM), consisting of 
    three random variables, with the following structure:
    
                    (N0)
                    /  \
                   /    \
                 (N1)   (N2)
                  
    """

    def __init__(self, node_0, edge_0_1, edge_0_2):
        """

        This function initiallzes an instance of the PGM class.  It takes as 
        input one node potentiol (for N0) and two edge potentials (for the two
        edges).  And it initializes a data structure that represents the PGM.  
        The data structure that you use, and how you use it, is up to you.  My 
        recommendation is to pick a data structure that allows you to represent the 
        joint probability table for the PGM.
        
        Input
        -----
    
        - node_0: A prior probability distribution represented as a Python dictionary; 
                node0[h] gives the (unconditional) probability that h is the value
                of N0.

        - edge_0_1: A set of conditional probability distributions represented as 
                a Python dictionary of dictionaries; edge1[h][e] gives the 
                (conditional) probability that e is value of N1 given that
                h is the value of N1 (i.e., node1[h][e] equals P(N1 = e | N0 = h).

        - edge_0_2: Just like edge1 except that it is the edge potential for the edge
                connecting N0 and N2 rather than for the edge connecting N0 and N1.
                
        """

        # -------------------------------------------------------------------------
        # YOUR CODE GOES HERE
        #
        self.node_0=node_0
        self.edge_0_1=edge_0_1
        self.edge_0_2=edge_0_2

        #
        # END OF YOUR CODE
        # ----------------------------------------------------------------
        
    def update(self, observed):
        """

        This function updates the data structure that represents the PGM based 
        on the evidence e that is observed.
                
        Input
        -----
    
        - observed: The evidence e that is observed.

                
        """

        # -------------------------------------------------------------------------
        # YOUR CODE GOES HERE
        #
        prior=self.node_0
        self.node_0={}
        
        for key in prior:
            self.node_0[key]=0
            
        for h in self.edge_0_1:
            for e in self.edge_0_1[h]:
                if e == observed:
                    self.node_0[h] += prior[h]*self.edge_0_1[h][e]
        
        for h in self.edge_0_2:
            for e in self.edge_0_2[h]:
                if e == observed:
                    self.node_0[h] += prior[h]*self.edge_0_2[h][e]
        self.node_0=normalize(self.node_0)
        #
        # END OF YOUR CODE
        # -------------------------------------------------------------------------    

    def marginalize(self, axis):
        """

        This function consults the data structure that represents the PGM and
        returns the current probability distribution for one of the three 
        random variables.
                        
        Input
        -----
    
        - axis: 0, 1, or 2
        
        Output
        -----
    
        - dist: If x is the value of axis, dist is the current probability 
                distribution for random variable Nx represented as a Python
                dictionary.
                
        """
           
        dist = {}

        # -------------------------------------------------------------------------
        # YOUR CODE GOES HERE
        #
        if axis==0:
            dist=self.node_0;
        elif axis==1:
            for h in self.edge_0_1:
                for e in self.edge_0_1[h]:
                    dist[e]=0
            for h in self.edge_0_1:
                for e in self.edge_0_1[h]:
                    dist[e]+= self.node_0[h]*self.edge_0_1[h][e]
        elif axis==2:
            for h in self.edge_0_2:
                for e in self.edge_0_2[h]:
                    dist[e]=0
            for h in self.edge_0_2:
                for e in self.edge_0_2[h]:
                    dist[e]+= self.node_0[h]*self.edge_0_2[h][e]
        dist=normalize(dist)

        #
        # END OF YOUR CODE
        # -------------------------------------------------------------------------    

        return dist
    
def normalize(dist):
    """
    This function takes a distribution and normalizes it to produce a 
    probability distribution.
    
    Input
    -----

    - dist: A distribution represented as a Python dictionary. 
   
    Output
    -----
    
    - prob_dist: A probability distribution (i.e., a distribution where the 
            magnitudes of the values stay in the same ratios, but the sum of 
            the values adds up to 1) represented as a Python dictionary. 

    """
    
    prob_dist = {}

    # -------------------------------------------------------------------------
    # YOUR CODE GOES HERE
    #
    sum = 0
    for key in dist:
        sum+=dist[key]
        for key in dist:
            prob_dist[key]=round(dist[key]/sum,3)
    #
    # END OF YOUR CODE
    # -------------------------------------------------------------------------    
    
    return prob_dist
    

def main():

    # the priors and the likelihoods for the Chicken Pox example
    chicken_prior = {'NOPOX': 0.9, 'POX': 0.1}
    chicken_spots_conditional = {'NOPOX': {'NOSPOTS': 0.999, 'SPOTS': 0.001}, 'POX': {'NOSPOTS': 0.2, 'SPOTS': 0.8}}
    chicken_fever_conditional = {'NOPOX': {'NOFEVER': 0.95, 'FEVER': 0.05}, 'POX': {'NOFEVER': 0.4, 'FEVER': 0.6}}

    # create a PGM for the Chicken Pox example
    chicken = PGM(chicken_prior, chicken_spots_conditional, chicken_fever_conditional)
    
    print("My Answer:")
    print("The doctor's prior regarding chicken pox is ", chicken.marginalize(0)) 
    print("Expected Answer:")
    print("The doctor's prior regarding chicken pox is ", {'NOPOX': 0.9, 'POX': 0.1}) 
    print("")
    
    print("Suppose that the patient has spots.")
    chicken.update('SPOTS')
    
    print("My Answer:")
    print("The doctor's posterior regarding chicken pox is ", chicken.marginalize(0)) 
    print("Expected Answer:")
    print("The doctor's posterior regarding chicken pox is ", {'NOPOX': 0.011, 'POX': 0.989}) 
    print("")

    print("Suppose that the patient has fever as well.")
    chicken.update('FEVER')

    print("My Answer:")
    print("The doctor's posterior regarding chicken pox is ", chicken.marginalize(0)) 
    print("Expected Answer:")
    print("The doctor's posterior regarding chicken pox is ", {'NOPOX': 0.001, 'POX': 0.999}) 
    print("")

if __name__ == '__main__':
    main()
        

