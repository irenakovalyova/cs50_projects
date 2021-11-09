#include "helpers.h"
#include <math.h> 

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int blue = image[i][j].rgbtBlue;
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            
            int average = round(((float) blue + (float) red + (float) green)/3);
            image[i][j].rgbtBlue = image[i][j].rgbtRed = image[i][j].rgbtGreen = average;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int blue = image[i][j].rgbtBlue;
            int red = image[i][j].rgbtRed;
            int green = image[i][j].rgbtGreen;
            
            double sepiaRed = round(0.393 * ((double) red) + 0.769 * ((double) green) + 0.189 * ((double) blue));
            if (sepiaRed > 255)
            {
                image[i][j].rgbtRed = 255;
            }
            else
            {
                image[i][j].rgbtRed = round(sepiaRed);
            }
            
            double sepiaGreen = round(0.349 * ((double) red) + 0.686 * ((double) green) + 0.168 * ((double) blue));
            if (sepiaRed > 255)
            {
                image[i][j].rgbtGreen = 255;
            }
            else
            {
                image[i][j].rgbtGreen = round(sepiaGreen);
            }
            double sepiaBlue = round(0.272 * ((double) red) + 0.534 * ((double) green) + 0.131 * ((double) blue));
            if (sepiaRed > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtBlue = round(sepiaBlue);
            }
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int middle = width/2;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < middle; j++)
        {
            RGBTRIPLE buf = image[i][j];
            image[i][j] = image[i][width - (j + 1)];
            image[i][width - (j + 1)] = buf;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
