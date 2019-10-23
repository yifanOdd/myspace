# -*- coding: utf-8 -*-
"""

CONDITIONALIZE ASSIGNMENT

"""

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
         prob_dist[key]=round(dist[key]/sum,5)
    #
    # END OF YOUR CODE
    # -------------------------------------------------------------------------    

    return prob_dist

def conditionalize(prior, conditional, observed):
    """

    This function takes an agent's prior probability distribution and (using the
    agent's likelihoods) conditionalizes on an observed datum to produce a 
    posterior probability distribution.

    Input
    -----

    - prior: A prior probability distribution represented as a Python dictionary; 
            prior[e] gives the (unconditional) probability that e is the outcome.

    - conditional: A set of conditional probability distributions represented as 
            a Python dictionary of dictionaries; conditional[h][e] gives the 
            (conditional) probability that e is the evidence that is observed given 
            that hypothesis h is true (i.e., conditional[h][e] equals P(e | h).

    - observed: The evidence e that is observed.

    Output
    -----

    - posterior: A posterior probability distribution represented as a Python dictionary.


    """

    posterior = {}

    # -------------------------------------------------------------------------
    # YOUR CODE GOES HERE
    #
    for key in prior:
        posterior[key]=0
        
    for h in conditional:
        for e in conditional[h]:
            if e == observed:
                posterior[h] += round(prior[h]*conditional[h][e],5)
    posterior=normalize(posterior)
    print(posterior)
    #
    # END OF YOUR CODE
    # -------------------------------------------------------------------------    

    return posterior



def main():

    # Chicken Pox inference

    chicken_prior = {'NOPOX': 0.9, 'POX': 0.1}
    chicken_spots_conditional = {'NOPOX': {'NOSPOTS': 0.999, 'SPOTS': 0.001}, 'POX': {'NOSPOTS': 0.2, 'SPOTS': 0.8}}

    print("The doctor's prior regarding chicken pox is ", chicken_prior) 

    print("Suppose that the patient has spots.")
    chicken_posterior = conditionalize(chicken_prior, chicken_spots_conditional, 'SPOTS')

    print("My answer:")
    print("The doctor's posterior regarding chicken pox is ", chicken_posterior) 

    print("Expected answer:")
    print("The doctor's posterior regarding chicken pox is ", {'NOPOX': 0.01, 'POX': 0.99}) 

if __name__ == '__main__':
    main()

