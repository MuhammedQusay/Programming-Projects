#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void calculate_standard_deviation(double data[], int n) {
    double mean = 0.0, sum_deviation = 0.0;
    for (int i = 0; i < n; ++i) mean += data[i];
    mean /= n;
    for (int i = 0; i < n; ++i) sum_deviation += pow(data[i] - mean, 2);
    printf("Standard Deviation: %.2f\n", sqrt(sum_deviation / n));
}

void calculate_mean(double data[], int n) {
    double sum = 0.0;
    for (int i = 0; i < n; ++i) sum += data[i];
    printf("Mean: %.2f\n", sum / n);
}

void calculate_variance(double data[], int n) {
    double mean = 0.0, sum_deviation = 0.0;
    for (int i = 0; i < n; ++i) mean += data[i];
    mean /= n;
    for (int i = 0; i < n; ++i) sum_deviation += pow(data[i] - mean, 2);
    printf("Variance: %.2f\n", sum_deviation / n);
}

void calculate_euclidean_distance(double a[], double b[], int n) {
    double sum = 0.0;
    for (int i = 0; i < n; ++i) sum += pow(a[i] - b[i], 2);
    printf("Euclidean Distance: %.2f\n", sqrt(sum));
}

void calculate_manhattan_distance(double a[], double b[], int n) {
    double sum = 0.0;
    for (int i = 0; i < n; ++i) sum += fabs(a[i] - b[i]);
    printf("Manhattan Distance: %.2f\n", sum);
}

void calculate_histogram(double data[], int n, int intervals) {
    double min = data[0], max = data[0];
    for (int i = 1; i < n; ++i) {
        if (data[i] < min) min = data[i];
        if (data[i] > max) max = data[i];
    }
    double interval_width = (max - min) / intervals;
    int histogram[intervals];
    for (int i = 0; i < intervals; ++i) histogram[i] = 0;
    for (int i = 0; i < n; ++i) {
        int interval_index = (int)((data[i] - min) / interval_width);
        if (interval_index == intervals) interval_index--;
        histogram[interval_index]++;
    }
    printf("Histogram:\n");
    for (int i = 0; i < intervals; ++i) {
        printf("Interval %d: %d\n", i + 1, histogram[i]);
    }
}

void normalize_data(double data[], int n) {
    double min = data[0], max = data[0];
    for (int i = 1; i < n; ++i) {
        if (data[i] < min) min = data[i];
        if (data[i] > max) max = data[i];
    }
    printf("Normalized Values:\n");
    for (int i = 0; i < n; ++i) {
        printf("%.2f ", (data[i] - min) / (max - min));
    }
    printf("\n");
}

void calculate_chebyshev_distance(double a[], double b[], int n) {
    double max_diff = 0.0;
    for (int i = 0; i < n; ++i) {
        double diff = fabs(a[i] - b[i]);
        if (diff > max_diff) max_diff = diff;
    }
    printf("Chebyshev Distance: %.2f\n", max_diff);
}

void calculate_cosine_similarity(double a[], double b[], int n) {
    double dot_product = 0.0, a_magnitude = 0.0, b_magnitude = 0.0;
    for (int i = 0; i < n; ++i) {
        dot_product += a[i] * b[i];
        a_magnitude += pow(a[i], 2);
        b_magnitude += pow(b[i], 2);
    }
    printf("Cosine Similarity: %.2f\n", dot_product / (sqrt(a_magnitude) * sqrt(b_magnitude)));
}

int main() {
    int choice, n, intervals;
    printf("Select an operation:\n");
    printf("1. Standard Deviation\n2. Mean\n3. Variance\n4. Euclidean Distance\n5. Manhattan Distance\n6. Histogram\n7. [0, 1] Normalization\n8. Chebyshev Distance\n9. Cosine Similarity\n");
    scanf("%d", &choice);

    system("cls");

    if ((choice >= 1 && choice <= 3) || choice == 6 || choice == 7) {
        printf("Enter the number of data points: ");
        scanf("%d", &n);
        double data[n];
        printf("Enter the data points: ");
        for (int i = 0; i < n; ++i) scanf("%lf", &data[i]);

        system("cls");
        
        printf("Entered Data: ");
        for (int i = 0; i < n; ++i) printf("%.2f ", data[i]);
        printf("\n");

        switch (choice) {
            case 1:
                calculate_standard_deviation(data, n);
                break;
            case 2:
                calculate_mean(data, n);
                break;
            case 3:
                calculate_variance(data, n);
                break;
            case 6:
                printf("Enter the number of intervals: ");
                scanf("%d", &intervals);
                calculate_histogram(data, n, intervals);
                break;
            case 7:
                normalize_data(data, n);
                break;
        }
    } else if ((choice >= 4 && choice <= 5) || choice == 8 || choice == 9) {
        printf("Enter the number of dimensions: ");
        scanf("%d", &n);
        double a[n], b[n];
        printf("Enter the first data set: ");
        for (int i = 0; i < n; ++i) scanf("%lf", &a[i]);
        printf("Enter the second data set: ");
        for (int i = 0; i < n; ++i) scanf("%lf", &b[i]);

        system("cls");
        
        printf("Entered First Data Set: ");
        for (int i = 0; i < n; ++i) printf("%.2f ", a[i]);
        printf("\nEntered Second Data Set: ");
        for (int i = 0; i < n; ++i) printf("%.2f ", b[i]);
        printf("\n");

        switch (choice) {
            case 4:
                calculate_euclidean_distance(a, b, n);
                break;
            case 5:
                calculate_manhattan_distance(a, b, n);
                break;
            case 8:
                calculate_chebyshev_distance(a, b, n);
                break;
            case 9:
                calculate_cosine_similarity(a, b, n);
                break;
            default:
                printf("Invalid Choice\n");
                break;
        }
    } else {
        printf("Invalid Choice\n");
    }

    return 0;
}
