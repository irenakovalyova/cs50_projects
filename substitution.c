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
    if (strlen(argv[1]) != 26)
    {
        printf("Key must contain 26 characters.\n");
        return 2;
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