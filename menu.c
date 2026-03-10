#include<stdio.h>
int main(){
    int a[50], n, i, j, pos, val, del-val, found, choice;
    printf("enter size of the array: ");
    scanf("%d",n);
    printf("enter elements of the array: ");
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);

    } 

    while (1) {
        printf("\nMenu:\n");
        printf("1. Insert Element\n");
        printf("2. Delete Element\n");
        printf("3. Merge with Another Array\n");
        printf("4. Display Array\n");
        printf("5. Exit\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                if (n >= 50) {
                    printf("Array is full. Cannot insert more elements.\n");
                    break;
                }
                printf("Enter position to insert (0 to %d): ", n);
                scanf("%d", &pos);
                if (pos < 0 || pos > n) {
                    printf("Invalid position.\n");
                
                } 
                else {
                    printf("Enter value to insert: ");
                    scanf("%d", &val);
                    for (i = n; i > pos; i--) {
                        a[i] = a[i - 1];
                    }   
                    a[pos] = val;
                    n++;
                    printf("Element inserted successfully.\n");
                }
                break;
            case 2:
                if (n == 0) {
                    printf("Array is empty. Cannot delete elements.\n");
                    break;
                }
                printf("Enter position to delete (0 to %d): ", n - 1);
                scanf("%d", &pos);
                if (pos < 0 || pos >= n) {
                    printf("Invalid position.\n");
                }
                else {
                    val = a[pos];
                    for (i = pos; i < n - 1; i++) {
                        a[i] = a[i + 1];
                    }
                    n--;
                    printf("Element %d deleted successfully.\n", val);
                }   
                break;
            case 3:
                   
}
}



}