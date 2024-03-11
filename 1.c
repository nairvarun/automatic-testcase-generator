#include<stdio.h>
int main() {
    int work;
    double payment = 0;
    scanf("%d", &work);
    if (work > 10) {
        payment = 10;
    } else {
        payment = 0;
    }
    printf("succs %f\n", payment);
}
