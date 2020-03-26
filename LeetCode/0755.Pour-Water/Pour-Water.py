class Solution(object):
    def pourWater(self, H, V, K):
        for _ in xrange(V):
            for d in (-1, 1):
                idx = best = K;
                while 0 <= idx+d < len(H) and H[idx+d] <= H[idx]:
                    if H[idx+d] < H[idx]: best = idx+d;
                    idx += d;
                if H[best] < H[K]:
                    H[best] += 1;
                    break;
            else:
                H[K] += 1;
        return H
