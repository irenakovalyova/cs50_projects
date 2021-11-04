#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

int alphacount (string line);
int wordcount(string line);
int sentcount(string line);

int main(void)
{

  string text = get_string ("Text: ");
  int letters = alphacount(text);
  int words = wordcount(text);
  int sentences = sentcount(text);

  float l = (letters * 100) / (float) words;
  float s = (sentences * 100) / words;
  double index = (0.0588 * (double) l) - (0.296 * s) - 15.8;
  
  if (index > 16)
    {
      printf("Grade: 16+\n");
    }
  else if (index < 1)
    {
      printf("Before Grade 1\n");
    }
  else
    {
      printf("Grade: %d\n", (int) index);
    }
}

int alphacount (string line)
{
  int l = 0;
  for (int i = 0; line[i] != '\0'; i++)
  {
    if (isalpha(line[i]))
    {
      l++;
    }
  }
  return l;
}

int wordcount(string line)
{
  int w = 1;
  for (int i = 0; line[i] != '\0'; i++)
  {
    if (isspace(line[i]))
    {
      w++;
    }
  }
  return w;
}

int sentcount(string line)
{
  int s = 0;
  for (int i = 0; line[i] != '\0'; i++)
  {
    if (line[i] == '!' || line[i] == '.' || line[i] == '?')
    {
      s++;
    }
  }
  return s;
}