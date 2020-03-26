class Solution{
    public int target;
    class Pair{
        int x;
        int v;
        double t;
        public Pair(int xi, int vi) {
            x = xi; // int x (x)
            v = vi; // int y (x)
            t = (target - x + 0.0) / vi;        
        }
    }
    public int carFleet(int T, int[] X, int[] V) {// X: position V: speed T: target position
        target = T;
        int m = X.length;
        Pair[] cars = new Pair[m];
        for (int i = 0; i < m; i++) {
            cars[i] = new Pair(X[i], V[i]);
        }
        Arrays.sort(cars, (a,b)->(b.x - a.x)); //decending order

        int res = m;// car#
        int mCnt = 0;
        for (int i = 1; i < m; i++) {
            //double pre = cars[i - 1].t;
            //double cur = cars[i].t;
            if (Double.compare(cars[i].t, cars[i - 1].t) <= 0) {
            // [chialin] if (cars[i - 1].t > cars[i].t) {
            // System.out.printf(“%d %f”,i, cars[i].t);
                mCnt++;
                cars[i].t = cars[i - 1].t;
            }
        }
        res -= mCnt;
        return res;
    }
}
