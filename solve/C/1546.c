#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    int arr[n];
    int max = 0;

    for(int i = 0; i < n; i ++){
        scanf("%d", &arr[i]);
        if(arr[i] > max)
            max = arr[i];
    }

    double sum = 0;
    for(int j = 0; j < n; j ++){
        sum = sum + ((double ) arr[j] / max) * 100;
    }
    printf("%f\n", (double ) sum/n);
}
