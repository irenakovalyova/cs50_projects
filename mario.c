#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height = 0;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    int width = 1;
    int spaces = height - width;

    for (int i = 0; i < height; i++)
    {
        for (int z = 1; z <= spaces; z++) // Adding white spaces before dashes
        {
                printf(" ");
        }

        for (int j = 1; j <= width; j++) // Adding first set of dashes
        {
                printf("#");
        }
        
        for (int s = 0; s < 2; s++) // Adding white spaces between the two sets of dashes
        {
                printf(" ");
        }
        
        for (int h = 1; h <= width; h++) // Adding the second set of dashes
        {
                printf("#");
        }

        printf("\n"); // To the new line
        width++;
        spaces--;
    }
}