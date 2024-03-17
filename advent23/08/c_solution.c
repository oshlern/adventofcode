#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <regex.h>

// const char* FILENAME = "input";
// const char* FILENAME = "test";
const char* FILENAME = "test2";

struct Node {
    // char name[4], R_name[4], L_name[4];
    char *name, *R_name, *L_name;
    struct Node *R, *L, *next;
};

struct Node* base = NULL;


void processLine(char* line) {
    char name[4], R[4], L[4];
    strncpy(name, line, 3);
    strncpy(R, line + 7, 3);
    strncpy(L, line + 12, 3);
    name[3] = '\0';
    R[3] = '\0';
    L[3] = '\0';

    struct Node* node = (struct Node*) malloc(sizeof(struct Node));
    node->name = name;
    node->R_name = R;
    node->L_name = L;
    node->next = base;
    base = node;
}


int main(int argc, char *argv[]) {
    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    fp = fopen(FILENAME, "r");

    int n_dirs = ((int) getline(&line, &len, fp)) - 1;
    line[n_dirs] = '\0'; //replaces '\n'
    char *dirs = (char *) malloc(n_dirs+1);
    strcpy(dirs, line);
    printf("_%s_\n", line);
    printf("_%s_\n", dirs);


    getline(&line, &len, fp); // empty row
    while (getline(&line, &len, fp) != -1)
        processLine(line);

    struct Node *AAA, *ZZZ;
    struct Node* head1 = base;
    while (head1 != NULL) {
        if (strcmp(head1->name, "AAA") == 0)
            AAA = head1;
        if (strcmp(head1->name, "ZZZ") == 0)
            ZZZ = head1;

        struct Node* head2 = base;
        while (head2 != NULL) {
            if (strcmp(head2->R_name, head1->name) == 0)
                head2->R = head1;
            if (strcmp(head2->L_name, head1->name) == 0)
                head2->L = head1;
            head2 = head2->next;
        }
        head1 = head1->next;
    }

    struct Node* cur = AAA;
    int iters = 0;
    while (cur != ZZZ) {
        if (cur == NULL) {
            printf("ouch\n");
        }
        if (*(dirs + (iters % n_dirs)) == 'R') {
            printf("rrrr\n");
            cur = cur->R;
        // } else if (*(dirs + (iters % n_dirs)) != 'L') {
        //     // printf("%d, %d, %s", iters, iters % n_dirs, dirs
        //     // )
        //     printf("----------------MISDIRECTION------------------\n");
        } else {
            printf("llll\n");
            cur = cur->L;
        }
        iters++;
    }
    printf("_%s_\n", dirs);

    printf("%d\n", iters);


    struct Node* head = base;
    while (head != NULL) {
        struct Node* temp = head;
        head = head->next;
        free(temp);
    }
    free(dirs);
    fclose(fp);
    free(line);
    exit(EXIT_SUCCESS);
}