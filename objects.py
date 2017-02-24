
class Video:

    def __init__(self, idx, size):
        self.size = size
        self.idx = idx


class Req:
    def __init__(self, v_idx, e_idx, num):
        self.v_idx = v_idx
        self.e_idx = e_idx
        self.num = num
        self.num_remaining = num


class EndPoint:

    def __init__(self, idx, dc_latency, cache):
        self.idx = idx
        self.dc_latency = dc_latency

        self.cache_latencies = {}
        for c in cache:
            self.cache_latencies[c[0]] = c[1]

        self.reqs = []

class Cache:

    def __init__(self, idx, max_capacity):
        self.idx = idx
        self.videos = []

        self.endpoints = []

        self.capacity_used = 0
        self.max_capacity = max_capacity
        self.gain = None
        self.comnect = None

    def compute_gain(self):

        if self.gain is None:

            gain = 0
            for ep in self.endpoints:

                number = sum([r.num for r in ep.reqs])

                gain += (ep.dc_latency - ep.cache_latencies[self.idx])*number

            self.gain = gain

        return self.gain

    def add_video(self, v):
        if self.capacity_used + v.size > self.max_capacity:
            raise ValueError("Max capacity exceeded! stupid!")
            # return False
        else:
            self.capacity_used += v.size
            self.videos.append(v)
