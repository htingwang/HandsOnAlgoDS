int romanToInt(char* s) {
    //I: 0x49, 0001,
    //V: 0x56, 0110,
    //X: 0x58, 0000,
    //L: 0x4C, 1100,
    //C: 0x43, 0011,
    //D: 0x44, 0100,
    //M: 0x4D, 1101,
    int hashTable[1<<5];
    hashTable['I'&0xf]=1;
    hashTable['V'&0xf]=5;
    hashTable['X'&0xf]=10;
    hashTable['L'&0xf]=50;
    hashTable['C'&0xf]=100;
    hashTable['D'&0xf]=500;
    hashTable['M'&0xf]=1000;
    int i, ret=0, len=strlen(s);
    ret += hashTable[s[len-1]&0xf];
    for (i=len-2; i>=0; i--) {
        if (hashTable[s[i]&0xf] < hashTable[s[i+1]&0xf])
            ret -= hashTable[s[i]&0xf];
        else
            ret += hashTable[s[i]&0xf];
    }
    return ret;
}
