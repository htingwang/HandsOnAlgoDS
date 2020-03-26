/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findRepeatedDnaSequences(char* s, int* returnSize) {
    int len=strlen(s), i=0, hashNum=0, cnt=0;
    if (len<11) return NULL;
    //A:0x41, C:0x43, G:0x47, T:0x54
    //X&7: 0x1(001), 0x3(011), 0x7(111), 0x4(100)
    //(X&7)>>1: 00, 01, 11, 10
    //use 2-bit represent each character
    //use 20-bit represent a key
    //4^10=2^20=1<<21 different keys
    int* hashTable = (int*)malloc((1<<21)*sizeof(int));
    char** returnArray=(char**)malloc(len*sizeof(char*));
    memset(hashTable, 0, (1<<21)*sizeof(int));
    //*returnSize = 0;
    for (i=0; i<9; i++)
        hashNum = (hashNum<<2) | (((*(s+i))&7)>>1);
    for (i=9; i<len; i++) {
        hashNum = ((hashNum<<2) | (((*(s+i))&7)>>1)) & 0xfffff; //20-bit
        if (hashTable[hashNum]++ == 1) {
            returnArray[cnt] = (char*)malloc((10+1)*sizeof(char));
            strncpy(returnArray[cnt], s+i-9, 10);
            returnArray[cnt++][10] = '\0';
        }
    }
    free(hashTable);
    *returnSize = cnt;
    return returnArray;
}
