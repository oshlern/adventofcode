// #define _GNU_SOURCE
#include <string.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

const char* FILENAME = "input";
const int NUM_SEEDS = 20;
// const char* FILENAME = "test";
// const int NUM_SEEDS = 4;

struct Node* seeds_base = NULL;
struct Node* news_base = NULL;


// Linked list
struct Node {
    long start;
    long end;
    struct Node* next;
};

struct Node* createNode(long start, long end, struct Node* next) {
    struct Node* newNode = (struct Node*) malloc(sizeof(struct Node));
    if (newNode != NULL) {
        newNode->start = start;
        newNode->end = end;
        newNode->next = next;
    } else {
        fprintf(stderr, "Error: Unable to allocate memory for a new node.\n");
        exit(EXIT_FAILURE);
    }
    return newNode;
}

void deleteSeed(struct Node* seed) {
    // printf("AAA %ld %ld\n", seed->start, seed->end);
    struct Node* S = seeds_base;
    while (S != NULL) {
        // printf("s: %ld, e: %ld\n", S->start, S->end);
        S = S->next;
    }
    if (seed != seeds_base) {
        struct Node* s = seeds_base;
        while (s->next != seed) {
            if (s->next == NULL) {
                // printf("aaa %ld %ld\n", s->start, s->end);
            }
            s = s->next;
        }
        s->next = seed->next;
    } else {
        seeds_base = seed->next;
    }
    free(seed);
}

void newRange(long s, long e, long shift) {
    news_base = createNode(s + shift, e + shift, news_base);
}

void convertRange(struct Node* seed, long shift, long m_S, long m_E) {
    long s_S = seed->start;
    long s_E = seed->end;
    // printf("s: %ld, e: %ld, S: %ld, E: %ld, shift: %ld\n", s_S, s_E, m_S, m_E, shift);
    if ((s_S > m_E) || (s_E < m_S))
        return;
    if (s_S < m_S) {
        if (s_E <= m_E) { // s S e E ==> NS NE, s S
            newRange(m_S, s_E, shift);
            seed->end = m_S;
        } else {         // s S E e ==> NS NE, s S, E e
            newRange(m_S, m_E, shift);
            seed->end = m_S;
            seed->next = createNode(m_E, s_E, seed->next);
        }
    } else {
        if (s_E <= m_E) { // S s e E ==> NS NE
            newRange(s_S, s_E, shift);
            deleteSeed(seed);
        } else {         // S s E e ==> NS NE, E e
            newRange(s_S, m_E, shift);
            seed->start = m_E;
        }
    }
}

int main(int argc, char *argv[]) {
    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    fp = fopen(FILENAME, "r");
    
    getline(&line, &len, fp);
    strtok(line, " ");
    for (int i = 0; i < NUM_SEEDS/2; i++) {
        long start = strtol(strtok(NULL, " \n"), NULL, 10);
        long range = strtol(strtok(NULL, " \n"), NULL, 10);
        seeds_base = createNode(start, start + range, seeds_base);
    }

    getline(&line, &len, fp); // "\n"
    while ((read =  getline(&line, &len, fp)) != -1) { // "a-to-b map:"
        while ((read = getline(&line, &len, fp)) > 2) { // "x y z"
            long dst_st = strtol(strtok(line, " "), NULL, 10);
            long src_st = strtol(strtok(NULL, " "), NULL, 10);
            long range = strtol(strtok(NULL, "\n"), NULL, 10);
            long shift = dst_st - src_st;
            long m_S = src_st;
            long m_E = src_st + range;
            struct Node* seed = seeds_base;
            struct Node* next;
            while (seed != NULL) {
                next = seed->next;
                convertRange(seed, shift, m_S, m_E);
                seed = next;
            }
        }

        // Append news to seeds
        if (seeds_base == NULL) {
            seeds_base = news_base;
        } else {
            struct Node* seed = seeds_base;
            while (seed->next != NULL)
                seed = seed->next;
            seed->next = news_base;
        }
        news_base = NULL;
    }

    long min_loc = seeds_base->start;
    struct Node* seed = seeds_base;
    while (seed != NULL) {
        if (seed->start < min_loc)
            min_loc = seed->start;
        seed = seed->next;
    }
    printf("%ld\n", min_loc);

    fclose(fp);
    free(line);
    while (seeds_base != NULL) {
        struct Node* temp = seeds_base;
        seeds_base = seeds_base->next;
        free(temp);
    }
    exit(EXIT_SUCCESS);
}