int climbStairs(int n) {
    if (n==1) return 1;
    if (n==2) return 2;
    int first=1, second=2, third;
    for (int i=2; i<n; i++) {
        third = first+second;
        first = second;
        second = third;
    }
    return third;
}
