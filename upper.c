#include <stdio.h>
#include <string.h>

int main(void) {
    const char *mystr = "I wish it was apero already.";
    int i;

    for(i = 0; i < strlen(mystr); i++) {
        printf("%c", mystr[i] - 32);
    }
    printf("\n");
    return 0;
}
