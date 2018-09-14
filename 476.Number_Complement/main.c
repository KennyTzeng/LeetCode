#include <limits.h>

int findComplement(int num) {
    int mask = INT_MAX;
    while((num & mask) == num) {
        mask = mask >> 1;
    }
    if(mask != INT_MAX) {
        mask = (mask << 1) + 1;
    }

    return num ^ mask;
}
