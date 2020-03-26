/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** findWords(char** words, int wordsSize, int* returnSize) {
    //QWERTYUIOP
    //ASDFGHJKL
    //ZXCVBNM
    //ABCDEFGHIJKLMNO PQRSTUVWXYZ
    //122101110111220 00010020202
    char lineidx[27]={3,1,2,2,1,0,1,1,1,0,1,1,1,2,2,0,0,0,0,1,0,0,2,0,2,0,2};
    int retcnt=0, i=0, j=0, cnt=0;
    char** returnArray=(char**)malloc(wordsSize*sizeof(char*));
    char preline=0;
    for (i=0; i< wordsSize; i++) {
        int wordLen=strlen(words[i]);
        char isSameLine=1;
        preline=lineidx[words[i][0]&0x1f];
        for (j=1; j<wordLen; j++) {
            if (preline != lineidx[words[i][j]&0x1f]) {
                isSameLine=0;
                break;
            }
            preline = lineidx[words[i][j]&0x1f];
        }
        if (isSameLine) {
            returnArray[cnt] = (char*)malloc((wordLen+1)*sizeof(char));
            strcpy(returnArray[cnt], words[i]);
            cnt++;
        }
    }
    *returnSize = cnt;
    return returnArray;
}
