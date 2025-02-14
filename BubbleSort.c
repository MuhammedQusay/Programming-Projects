#include <stdio.h>
#define SIZE 10

// Bubble sort function
void bubbleSort(int * const array, const size_t size) {
    for (size_t pass = 0; pass < size - 1; ++pass) { // Number of passes
        for (size_t i = 0; i < size - pass - 1; ++i) { // Compare adjacent elements
            if (array[i] > array[i + 1]) { // Swap if out of order(i > i+1 [1,2,3] | i < i+1 [3,2,1])
                int temp = array[i];
                array[i] = array[i + 1];
                array[i + 1] = temp;
            }
        }
    }
}

int main(void) {
    // Initialize the array
    int a[SIZE] = {2, 6, 4, 8, 10, 12, 89, 68, 45, 37};

    // Print the original array
    puts("Data items in original order");
    for (size_t i = 0; i < SIZE; ++i) {  //size_t = Only pozitif ints, uses for memory operators
        printf("%4d", a[i]);
    }

    // Sort the array
    bubbleSort(a, SIZE);

    // Print the sorted array
    puts("\nData items in ascending order");
    for (size_t i = 0; i < SIZE; ++i) {
        printf("%4d", a[i]);
    }
    puts(""); // New line after the output

    
    printf("%d",sizeof(a)/sizeof(a[0]));


    return 0;
}
