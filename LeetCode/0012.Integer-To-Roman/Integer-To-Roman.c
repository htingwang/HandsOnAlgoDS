char* intToRoman(int num) {
    //I: 0x49, 0001, 1
    //V: 0x56, 0110, 5
    //X: 0x58, 0000, 10
    //L: 0x4C, 1100, 50
    //C: 0x43, 0011, 100
    //D: 0x44, 0100, 500
    //M: 0x4D, 1101, 1000
    char* ones[10]={"", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"};
    char* tens[10]={"", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"};
    char* hundreds[10]={"", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"};
    char* thousands[4]={"", "M", "MM", "MMM"};
    char* retArray=(char*)malloc(16*sizeof(char));
    char* pTmp;
    pTmp=retArray;
    int idx;
    if (idx = num/1000) {
        strcpy(pTmp, thousands[idx]);
        pTmp += strlen(thousands[idx]);
    }
    if (idx = (num/100)%10) {
        strcpy(pTmp, hundreds[idx]);
        pTmp += strlen(hundreds[idx]);
    }
    if (idx = (num/10)%10) {
        strcpy(pTmp, tens[idx]);
        pTmp += strlen(tens[idx]);
    }
    if (idx = num%10) {
        strcpy(pTmp, ones[idx]);
        //pTmp += strlen(thousands[idx]);
    }
    return retArray;
}
