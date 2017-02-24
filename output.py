# -*- coding: utf-8 -*-

import time


def write_output(inputf, servers):
    
    timestr = time.strftime("%Y%m%d-%H%M%S")     
    
    outputf = "results/%s_%s.txt" % (inputf, timestr)    
    
    print("Writing solution to %s" % outputf)

    f = open(outputf, "w")

    f.write("%d\n" % len(servers))

    for s in servers:
        #
        # Write solution generation here   
        #

        line = "%d" % s.idx

        for v in s.videos:
            line += (" %d" % v.idx)

        line += "\n"

        f.write(line)

    f.close()
