#include <string.h>
#include <stdio.h>
#include <stdlib.h>

const char* FILENAME = "input";
// const char* FILENAME = "test";
const int HAND_SIZE = 5;

int getScore(char* hand) {
    int max_count = 0;
    char max_card;
    int second_pair = 0;
    for (int i = 0; i < HAND_SIZE; i++) {
        int count = 1;
        char card = hand[i];
        for (int j = i+1; j < HAND_SIZE; j++)
            if (card == hand[j])
                count++;
        if (max_count >= 2 && count >= 2 && card != max_card)
            second_pair = 1;
        if (count >= max_count) {
            max_count = count;
            max_card = hand[i];
        }
    }
    int type_score = max_count*2 + second_pair;
    int score = 0;
    int power = 1;
    for (int i = HAND_SIZE-1; i >= 0; i--) {
        char card = hand[i];
        int val = 0;
        if (card == 'K') {val = 13;} else if (card == 'Q') {val = 12;}
        else if (card == 'J') {val = 11;} else if (card == 'T') {val = 10;}
        else if (card == 'A') {val = 14;} else { val = card - '0'; }
        score += power * val;
        power *= 15;
    }
    score += power * type_score;
    return score;
}

struct Node {
    int score;
    int bid;
    char* hand;
    struct Node* next;
};

struct Node* base = NULL;

void insertNode(char* hand, int score, int bid) {
    struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
    if (newNode == NULL) {
        fprintf(stderr, "Error: Unable to allocate memory for a new node.\n");
        exit(EXIT_FAILURE);
    }
    newNode->score = score;
    newNode->bid = bid;
    newNode->hand = strdup(hand);
    // printf("%d %s %d\n", score, hand, bid);

    if (base == NULL) {
        base = newNode;
    } else if (base->score > score) {
        newNode->next = base;
        base = newNode;
    } else {
        struct Node* head = base;
        while ((head->next != NULL) && (head->next->score < score)) {
            head = head->next;
        }
        newNode->next = head->next;
        head->next = newNode;
    }
}

int main(int argc, char *argv[]) {
    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    fp = fopen(FILENAME, "r");

    while ((read = getline(&line, &len, fp)) != -1) {
        char* hand = strtok(line, " ");
        int bid = atoi(strtok(NULL, "\n"));
        int score = getScore(hand);
        // printf(hand);
        insertNode(hand, score, bid);
    }

    int total = 0;
    struct Node* head = base;
    for (int rank=1; head != NULL; head = head->next, rank++) {
        printf("%d %s %d\n", rank, head->hand, head->bid);
        total += rank * head->bid;
        free(head->hand);
    }
    printf("%d\n", total);

    fclose(fp);
    free(line);
    exit(EXIT_SUCCESS);
}