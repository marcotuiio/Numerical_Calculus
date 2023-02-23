#include <stdio.h>

int main () {
    float mat[2][2] = {{10, 1}, {1, 8}};
    float b[2] = {23, 26};
    float x[2] = {0, 0};
    float aux[2] = {0, 0};

    for (int k = 0; k < 3; k++) {
        for (int i = 0; i < 2; i++) {
            float soma = 0;
            for (int j = 0; j < 2; j++) {
                if (i != j) {
                    soma = -mat[i][j] * x[j] + soma;
                }
            }
            aux[i] = (b[i] + soma) / mat[i][i];
            printf("x [%d] = %f   aux [%d] = %f\n", i, x[i], i, aux[i]);
        }
        for (int i = 0; i < 2; i++) {
            x[i] = aux[i];
        }
    }
    return 0;
}