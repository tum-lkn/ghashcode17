# -*- coding: utf-8 -*-

import os
from objects import *


def read_input(inputf):
    
    inputf = os.path.join("data/", inputf)    
    
    with open(inputf) as f:
        data = f.readlines()
    
    info = data[0].split(" ")     
    V=int(info[0])     
    E=int(info[1])     
    R=int(info[2])     
    C=int(info[3])    
    X=int(info[4].strip())    
    
    servercaches = [Cache(c, X) for c in range(C)]    
    
    print("--> Reading from %s." % inputf)
    
    print("--> Videos: %d" % V)
    print("--> Endpoints: %d" % E)
    print("--> Number of caches: %d" % C)
    print("--> Cache size: %d" % X)
    
    videos = [Video(idx, int(s)) for idx, s in enumerate(data[1].strip().split(" "))] 
    
    #print("Video sizes: %s" % [v.size for v in videos])    
    
    eidx = 2
    endpoints = []
    for e in range(E):

        latency, nr_of_caches = [int(d) for d in data[eidx].strip().split(" ")]
        
        #print("Endpoint %d: Latency: %d, Caches: %d" % (e, latency, nr_of_caches))
        
        caches = []
        for c in range(nr_of_caches):
                        
            eidx += 1                        
                        
            cache, clatency = [int(d) for d in data[eidx].strip().split(" ")]                        
 
            caches.append((cache, clatency)) 
 
            #print("-> Latency of cache %d is %d" % (cache, clatency))

        eidx += 1        
        
        e = EndPoint(e, latency, caches)
        endpoints.append(e)
        
        for cidx, latency in e.cache_latencies.items():
            servercaches[cidx].endpoints.append(e)
        
    requests = []
    for r in range(R):
        
        video, endpoint, nr_of_requests = [int(d) for d in data[eidx].strip().split(" ")]
        
        #print("%d requests for video %d coming from endpoint %d" % (nr_of_requests, video, endpoint))        
        
        eidx += 1
        
        robj = Req(video, endpoint, nr_of_requests)
        requests.append(robj)
        endpoints[endpoint].reqs.append(robj)

    return endpoints, requests, videos, servercaches
    

if __name__ == "__main__":    
    input_data = read_input("me_at_the_zoo.in")
