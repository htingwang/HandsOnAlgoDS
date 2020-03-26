int lengthOfLastWord(char* s) {
    int len=0;
    int tail=strlen(s)-1;
    while (tail >= 0 && s[tail] == ' ') tail--;
    while (tail >= 0 && s[tail] != ' ') {
        tail--;
        len++;
    }
    return len;
}
