// Implements a dictionary's functionality

#include <stdbool.h>
#include "dictionary.h"
#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Number of words
unsigned int n = 0;

// Hash value
unsigned int hash_value;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    hash_value = hash(word);
    node *table_position = table[hash_value];
    while (table_position != NULL)
    {
        if (strcasecmp(word, table_position->word) == 0)
        {
            return true;
        }
        table_position = table_position->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    unsigned long hash = 5381;
    int c;
    while ((c = toupper(*word++)))
    {
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
    }
    return hash % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *dictionary_file = fopen(dictionary, "r");
    if (dictionary_file == NULL)
    {
        return false;
    }
    else
    {
        char word[LENGTH + 1];
        while (fscanf(dictionary_file, "%s", word) != EOF)
        {
            node *new_node = malloc(sizeof(node));
            if (new_node == NULL)
            {
                return false;
            }
            strcpy(new_node->word, word);
            hash_value = hash(word);
            new_node->next = table[hash_value];
            table[hash_value] = new_node;
            n++;
        }
    }
    fclose(dictionary_file);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (n > 0)
    {
        return n;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // Iterate through buckets
    for (int i = 0; i < N; i++)
    {
        // Set cursor to this each bucket location  
        node *cursor = table[i];
// If cursor is not NULL, free  
        while (cursor)
        {
            // Create temp 
            node *tmp = cursor;
            // Move cursor to next node
            cursor = cursor->next;
            // Free up temp
            free(tmp);
        }
// If cursor is NULL
        if (i == N - 1 && cursor == NULL)
        {
            return true;
        }
    }
    return false;
    return false;
}
