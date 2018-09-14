#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* reverseString(char* s) {
    int length = 0;
    while(*(s+length) != '\0') {
        length++;
    }

    // s's length = length + 1('\0')
    char *reverseStr = (char *)malloc(length+1);
    for(int i = 0; i < length; i++) {
        reverseStr[i] = *(s+(length-1-i));
    }
    reverseStr[length] = '\0';

    return reverseStr;
}
