
class Solution{
    public double minmaxGasDist(int[] A, int k) {
        double L = 0, R = 100000000;
        while (R - L > 0.000001) {
            double mid = L + (R - L) / 2;
            if (tooLarge(A, mid, k)) L = mid;
            else R = mid;
        }
        return R; // we got k > target k
    }

    public boolean tooLarge(int[] A, double dist, int targetK) {
        int cnt = 0;
        for (int i = 0; i < A.length - 1; i++) {
            cnt += (A[i + 1] - A[i]) / dist;
        }
        return cnt > targetK;
    }
}

