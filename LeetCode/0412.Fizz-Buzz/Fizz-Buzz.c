/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** fizzBuzz(int n, int* returnSize) {
    int i=0;
    char** returnArray=(char**)malloc(n*sizeof(char*)+n*11*sizeof(char));
    char* pData=returnArray+n;//(char*)malloc(n*11*sizeof(char));
    for(i=0; i<n; i++, pData+=11*sizeof(char)) {
        returnArray[i] = pData;
        if((i+1)%3==0) {
            if((i+1)%5==0) {
                //returnArray[i]=(char*)malloc(9*sizeof(char));
                strncpy(returnArray[i], "FizzBuzz", 8);
                returnArray[i][8] = '\0';
            }
            else {
                //returnArray[i]=(char*)malloc(5*sizeof(char));
                strncpy(returnArray[i], "Fizz", 4);
                returnArray[i][4] = '\0';
            }
            continue;
        }
        if((i+1)%5==0) {
            //returnArray[i]=(char*)malloc(5*sizeof(char));
            strncpy(returnArray[i], "Buzz", 4);
            returnArray[i][4] = '\0';
            continue;
        }
        char buf[11];
        sprintf(buf,"%d",i+1);
        //returnArray[i]=(char*)malloc((strlen(buf)+1)*sizeof(char));
        strncpy(returnArray[i], buf, strlen(buf));
        returnArray[i][strlen(buf)] = '\0';
    }
    *returnSize = n;
    return returnArray;
}
