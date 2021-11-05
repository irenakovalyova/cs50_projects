#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>

string encryptor(string cyphr, string text);

int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    else if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 1;
    }
    for (int i = 0; i < (strlen(argv[1])); i++)
    {
        if (!isalpha(argv[1][i]))
        {
            printf("Invalid key: only alphabetic symbols are allowed\n");
            return 1;
        }
        
        for (int j = 0; j != i; j++)
        {
            if (argv[1][i] == argv[1][j] || argv[1][i] == tolower(argv[1][j]) || argv[1][i] == toupper(argv[1][j]))
            {
                printf("Invalid key: duplicated symbols are not allo0wed\n");
                return 1;
            }
        }
    }
    
    string plaintext = get_string("plaintext: ");
    printf("ciphertext: %s\n", encryptor(argv[1], plaintext));
}

string encryptor(string cyphr, string text)
{
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (islower(text[i]))
        {
            text[i] = tolower(cyphr[text[i] - 97]);
        }
        if (isupper(text[i]))
        {
            text[i] = toupper(cyphr[text[i] - 65]);
        }
    }
    return text;
}