# -*- coding: utf-8 -*-

from objects import *
import time
from knapsack import solveKnapsackHeuristic


def sort_caches(caches, videos=None):
    return reversed(sorted(caches, key=lambda x: x.compute_gain()))

def solve(endpoints, requests, videos, caches):

    cacheslen = len(caches)

    print("--> Sorting caches ..")

    start = time.time()
    caches = sort_caches(caches, videos)
    duration = time.time() - start
    
    print("--> Sorting caches .. took %.3fs." % duration)
    
    for cnum, cache in enumerate(caches):

        start = time.time()

        video_dict = {}

        for e in cache.endpoints:

            delay_score = e.dc_latency - e.cache_latencies[cache.idx]

            assert(delay_score > 0)

            for request in e.reqs:

                if request.v_idx in video_dict:

                    size, score = video_dict[request.v_idx]

                    video_dict[request.v_idx] = (size, score+delay_score*request.num)
                else:
                    video_dict[request.v_idx] = (videos[request.v_idx].size,
                                                 delay_score*request.num)

        # Solve Knapsack
        knapsack = []
        for v_idx, (size, score) in video_dict.items():
            knapsack.append((size, score, v_idx))

        solved = solveKnapsackHeuristic(knapsack, cache.max_capacity)

        for v_idx in solved:
            cache.add_video(videos[v_idx])

        # Update data structure
        for e in cache.endpoints:
            new_req_lists = []
            for req in e.reqs:
                if not videos[req.v_idx] in cache.videos:
                    new_req_lists.append(req)
            e.reqs = new_req_lists

        duration = time.time() - start
            
        if cnum % 25 == 0:
            print("--> Cache %d/%d finished. Last one took %.1fs." % (cnum+1, cacheslen, duration))

    return True

if __name__ == "__main__":

    from input import read_input
    from output import write_output

    #inputf = "example.in"
    inputf = "me_at_the_zoo.in"
    #inputf = "videos_worth_spreading.in"
    #inputf = "trending_today.in"
    #inputf = "kittens.in"

    endpoints, requests, videos, caches = read_input(inputf)
    solve(endpoints, requests, videos, caches)
    write_output(inputf, caches)
    