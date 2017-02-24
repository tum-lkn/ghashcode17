# -*- coding: utf-8 -*-

import time
from input import read_input
from output import write_output
from solver import solve

if __name__ == "__main__":

    inputfs = ["me_at_the_zoo.in", "videos_worth_spreading.in", "trending_today.in", "kittens.in"]

    for inputf in inputfs:

        # Read the input file
            
        print("")
        print("#############################################")
        print("Scenario: %s" % inputf)
        print("#############################################")
        print("")
        
        start = time.time()
        endpoints, requests, videos, caches = read_input(inputf)
        duration = time.time() - start        

        print("Reading %s .. took %.3fs." % (inputf, duration))

        # Solve the problem
        
        print("Solving ..")
        
        start = time.time()
        solve(endpoints, requests, videos, caches)
        duration = time.time() - start

        print("Solving .. took %.3fs." % duration)        

        # Output the solution
        
        write_output(inputf, caches)
