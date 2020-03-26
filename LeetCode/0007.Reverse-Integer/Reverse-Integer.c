int reverse(int x) {
    //123
    //loop 0: res=0+3=3, x=12
    //loop 1: res=30+2=32, x=1
    //loop2: res=32+1, x=0
    long res=0;
    while (x) {
        res = res*10 + x%10;
        x /= 10;
    }
    if (res < INT_MIN || res > INT_MAX) return 0;
    return res;
}
