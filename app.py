#include <stdio.h>

int main() {
    int num1, num2, sum;

    // Ask the user for two numbers
    printf(Enter two integers: );
    
    // Read and store the user's input
    scanf(%d %d, &num1, &num2);

    // Calculate the sum
    sum = num1 + num2;

    // Display the result
    printf(Sum: %dn, sum);

    return 0;
}

