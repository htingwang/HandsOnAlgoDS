int commonPrefixLen(char* str1, char* str2) {
    int len1=strlen(str1), len2=strlen(str2);
    int commonLen=0;
    for (int i=0; i<len1, i<len2; i++) {
        if (str1[i] == str2[i])
            commonLen++;
        else
            break;
    }
    return commonLen;
}
char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) return "";
    int commonLen=strlen(strs[0]);
    char* returnStr=(char*)malloc((commonLen+1)*sizeof(char));
    strcpy(returnStr, strs[0]);
    for (int i=1; i<strsSize; i++) {
        int tmpLen = commonPrefixLen(returnStr, strs[i]);
        if (tmpLen < commonLen) {
            commonLen = tmpLen;
            returnStr[commonLen]='\0';
        }
    }
    
    returnStr[commonLen]='\0';
    return returnStr;
}
