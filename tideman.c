#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
}
pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    int zero = 0;
    for (int i = 0; i < MAX; i++)
    {
        if (strcmp(name, candidates[i]) == zero)
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int i = 0; i < MAX; i++)
    {
        for (int j = 0; j < MAX; j++)
        {
            if (i != j)
            {
                for (int q = MAX; q > 1; q--)
                {
                    if (strcmp(candidates[ranks[q - 1]], candidates[i]) == 0 && strcmp(candidates[ranks[q]], candidates[j]) != 0)
                    {
                        preferences[i][j]++;
                    }
                }
            }
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    for (pair_count = 0; pair_count < (MAX * (MAX - 1) / 2); pair_count++)
    {
        for (int i = 0; i < MAX; i++)
        {
            for (int j = 0; j < MAX; j++)
            {
                if ((preferences[i][j] - preferences[j][i]) > 0)
                {
                    pairs[pair_count].winner = i;
                    pairs[pair_count].loser = j;
                }
            }
        }
    }
    return;
}
    
// Sort pairs
void sort_pairs(void)
{
    int stregnth[MAX * (MAX - 1) / 2];
    for (pair_count = 0; pair_count < (MAX * (MAX - 1) / 2); pair_count++)
    {
        for (int i = 0; i < MAX; i++)
        {
            for (int j = 0; j < MAX; j++)
            {
                if (pairs[pair_count].winner == i && pairs[pair_count].loser == j)
                {
                    stregnth[pair_count] = preferences[i][j];
                }
            }
        }
        if (stregnth[pair_count] > stregnth[pair_count + 1])
        {
            pair temp = pairs[pair_count];
            pairs[pair_count] = pairs[pair_count + 1];
            pairs[pair_count + 1] = temp;
        }
    }
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
    for (pair_count = 0; pair_count < (MAX * (MAX - 1) / 2); pair_count++)
    {
        for (int i = 0; i < MAX; i++)
        {
            for (int j = 0; j < MAX; j++)
            {
                if (pairs[pair_count].winner == i && pairs[pair_count].loser == j)
                {
                    locked[i][j] = true;
                }
            }
        }
    }
    return;
}

// Print the winner of the election
void print_winner(void)
{
    int wins = 0;
    for (int i = 0; i < MAX; i++)
        {
            for (int j = 0; j < MAX; j++)
            {
                if (i != j && locked[i][j] == true)
                {
                    wins++;
                }
            }
            if (wins == (MAX - 2))
            {
                printf("%s\n", candidates[i]);
            }
        }
    
    return;
}

