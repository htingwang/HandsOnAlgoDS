char* addBinary(char* a, char* b) {
    int len_a=strlen(a);
    int len_b=strlen(b);
    int len = len_a+1;
    if (len_b > len_a) len = len_b+1;
    char* ret = (char*)malloc((len+1)*sizeof(char));
#if 1
    int i=len_a-1, j=len_b-1, k, carry=0;
    for (k=len-2; k>=0; k--) {
        char bit_a=(i>=0)?a[i--]&1:0;
        char bit_b=(j>=0)?b[j--]&1:0;
        ret[k] = (bit_a^bit_b^carry)? '1':'0';
        //carry = (bit_a&bit_b) | (bit_a&carry) | (bit_b&carry);
        //carry = ((bit_a+bit_b+carry)>=2)? 1:0;
        carry = (bit_a+bit_b+carry)>>1;
    }
    
    if (carry) {
        for (k=len-1; k>0; k--) {
            ret[k] = ret[k-1];
        }
        ret[0] = '1';
        ret[len] = '\0';
    }
    else {
        ret[len-1] = '\0';
    }

#else //need to check overflow, int is not enough
    int num_a=0, num_b=0, num_ret;
    int i;
    for (i=0; i<len_a||i<len_b; i++) {
        if (i<len_a)
            num_a += a[i]&1? (1<<(len_a-1-i)):0;
        if (i<len_b)
            num_b += b[i]&1? (1<<(len_b-1-i)):0;            
    }
    num_ret = num_a+num_b;
    /*sprintf(ret, "%d", num_ret);
    if (len_a==1 && a[0]=='1' && len_b==1 && b[0]=='0')
    return ret;
    if (len_a==1 && a[0]=='0' && len_b==1 && b[0]=='1')
    return ret;*/
    //a="0", b="1"
    //len_a=1, len_b=1, len=2;
    
    if (num_ret>>(len-1) == 0) {
        len--;
    }
    for (i=0;i<len;i++) {
        ret[i] = (num_ret>>(len-1-i))%2? '1':'0';
    }
    ret[len] = '\0';
#endif
    return ret;
}
