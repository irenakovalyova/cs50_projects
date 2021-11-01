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
    for (int z = 1; z <= spaces; z++)
    {
      printf("  ");
    }

    for (int j = 1; j <= width; j++)
    {
      printf("#");
    }

    printf(" ");

    for (int h = 1; h <= width; h++)
    {
      printf("#");
    }

    printf("\n");
    width++;
    spaces--;
  }
}