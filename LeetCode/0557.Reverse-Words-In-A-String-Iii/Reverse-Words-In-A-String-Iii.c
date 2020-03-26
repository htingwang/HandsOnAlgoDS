char* reverseWords(char* s) {
    int len = strlen(s);
    char* n = (char*)malloc(len+1);
    char* retstr = (char*)malloc(len+1);
    char* tmpstr=retstr;
    int sublen=0;
    
    for (int i=0; i<len; i++) {
        if (s[i] != ' ') {
            n[sublen++] = s[i];
        }
        else {
            n[sublen] = '\0';
            for(int j=0; j< sublen; j++) {
              tmpstr[j] = n[sublen-1-j];  
            }
            //tmpstr = strrev(n, sublen);
            tmpstr[sublen] = ' ';
            tmpstr += sublen+1;
            sublen = 0;
        }
    }
    for(int j=0; j< sublen; j++) {
      tmpstr[j] = n[sublen-1-j];  
    }
    tmpstr[sublen] = '\0';
    free(n);
    return retstr;
    //free(tmpstr);
}
