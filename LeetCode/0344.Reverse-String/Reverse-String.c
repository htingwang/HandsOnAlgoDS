char* reverseString(char* s) {
    int len=strlen(s), i=0, j=len-1;
    char tmp;
    while(i<j) {
        tmp=s[i];
        s[i]=s[j];
        s[j]=tmp;
        i++;
        j--;
    }
    return s;
}
