#include <cs50.h>
#include <stdio.h>

int main(void)
{
   int start_size;
  do
  {
      start_size = get_int("Start population size: ");
  }
  while (start_size < 9);

    int end_size;
  do
  {
      end_size = get_int("End population size: ");
  }
  while (end_size < start_size);

  int n_years = 0;

  for (n_years = 0; start_size < end_size; n_years++)
  {
      start_size = start_size + (start_size / 3) - (start_size / 4);
  }
    printf("Start size: %i\n", start_size);
    printf("End size: %i\n", end_size);
    printf("Years: %i\n", n_years);
}