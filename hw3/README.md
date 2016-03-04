Homework 3 - question

    For each of the following RNG determine the number of samples necessary to achieve a 99% 
        confidence interval for the mean and verify that the correct mean is achieved by
        the RNG.
        Also use the Chi Squared GoF test with significance level 1% to check the distribution
        of the RNG


    1. Test the bad linear congruential generator from homework 1 as a generator
        for a uniform distributino in the interval [0,1)
    2. Test the built-in rand function as a generator for a uniform distribution
        in the interval (0,1)
    3. Test the normal RNG from homework 2 using the Box-Mueller transformation. Modify it
        to have mean = 0 and variance = 0.1
    4. Use the fundamental transformation law to determine a transformation for
        generating random values from the Cauchy distribution (from homework 2)
        Since the mean and variance are not finite values, the Central Limit Theorem
        cannot be used. You can use the Chi Squared test. What mean do you get from
        1,000 samples? Variance? 10,000 samples?
    5. Test the gamma-distributed RNG from hw2

USAGE
    +Run hw3_main.py
    +or  goodness_of_fit_lcg.py
    +    goodness_of_fit_rand.py
    +    goodness_of_fit_boxmuller.py
    +    goodness_of_fit_cauchy.py
    +    goodness_of_fit_gamma.py
    make sure all code files in this folder are present

