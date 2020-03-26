void reverse(int begin, int end, char* s) {
    while (begin < end) {
        s[begin] = s[begin] ^ s[end]; //b^e
        s[end] = s[begin] ^ s[end]; //b^e^e
        s[begin] = s[begin] ^ s[end]; //b^e^b
        begin++;
        end--;
    };
}
char* reverseStr(char* s, int k) {
    int len=strlen(s);
    for (int i=0; i<len; i+=(k<<1)) {
        if (i+k-1 < len)
            reverse(i, i+k-1, s);
        else
            reverse(i, len-1, s);
    }

    return s;
}
