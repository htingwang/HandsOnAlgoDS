char* countAndSay(int n) {
    //                      1, 1 
    //                     11, 1->11, 2
    //         2            1, 11->21, 2
    //        12           11, 21->1211, 4
    //111      2 2          1, 12->1112, 6
    //31      22           11, 22->22, 6
    //1311    22 2          1, 8
    //1113    2132         11, 10
    //3113   12    1113 12 2 1, 14
    //132113 1112  3113 11 22 11, 20
    //111 31   22 11 33 11 2132     11 321    222 1, 26
    //31   1311 22 21 23 21 12111312 21 131211 32 11, 34
    //1321 1321 32  11121312 21
    
    char* ret;
    if (n==1) {
        ret = (char*)malloc(2*sizeof(char));
        ret[0]='1';
        ret[1]='\0';
    }
    else {
        char* prev = countAndSay(n-1);
        int prevlen = strlen(prev);
        ret = (char*)malloc(prevlen*2*sizeof(char));
        int i, j, cnt, idx=0;
        for (i=0; i<prevlen;) {
            cnt=1;
            for(j=i+1; j<prevlen;j++) {
                if (prev[j] == prev[i]) {
                    cnt++;
                }
                else {
                    break;
                }
            }
            sprintf(ret+idx, "%d", cnt);
            ret[idx+1] = prev[i];
            idx += 2;
            i += cnt;
        }
        ret[idx] = '\0';
        free(prev);
    } 
    return ret;
}
