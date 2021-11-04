#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

int alphacount(string txt);
int wordcount(string txt);
int sentcount(string txt);

// Determines the reading level of the text provided by the user
int main(void)
{
    string text = get_string("Text: ");
    int letters = alphacount(text);
    int words = wordcount(text);
    int sentences = sentcount(text);

    float l = (letters * 100) / (float) words;
    float s = (sentences * 100) / (float) words;
    double index = (0.0588 * (double) l) - (0.296 * s) - 15.8;

    if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %d\n", (int) round(index));
    }
}

// Counts letters
int alphacount(string txt)
{
    int l = 0;
    for (int i = 0; txt[i] != '\0'; i++)
    {
        if (isalpha(txt[i]))
        {
            l++;
        }
    }
    return l;
}

// Counts words
int wordcount(string txt)
{
    int w = 1;
    for (int i = 0; txt[i] != '\0'; i++)
    {
        if (isspace(txt[i]))
        {
            w++;
        }
    }
    return w;
}

// Counts sentences
int sentcount(string txt)
{
    int s = 0;
    for (int i = 0; txt[i] != '\0'; i++)
    {
        if (txt[i] == '!' || txt[i] == '.' || txt[i] == '?')
        {
            s++;
        }
    }
    return s;
}