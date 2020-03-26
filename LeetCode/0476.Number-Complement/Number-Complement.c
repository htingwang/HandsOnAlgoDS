int findComplement(int num) {
    int mask=0xffffffff;
    while (num & mask) mask<<=1; //mask=111111...000..., # of zeros is bitcnt
    return ~num & ~mask;
}
