#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
 
int main(int argc, char *argv[])
{
    
    // Checking the input for the valid number of parameters
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    
    // Opening the specified file
    char *input_file_name = argv[1];
    FILE *input_file = fopen(input_file_name, "r");
    
    // If the file doesn't exist   
    if (input_file == NULL)
    {
        printf("Cannot open the file\n");
        return 2;
    }
    
    // Initializing:
    uint8_t buffer[512]; //the buffer for recovered images
    int file_count = 0; // a variable for counting files recovered
    char filename[8]; // an array for the name
    FILE *image = NULL; // the output file
    
    while (fread(&buffer, 512, 1, input_file) == 1)
    {
        // Checking first four bytes to determine the start of a JPEG
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // If this is not the first file, closing the previous one
            if (!(file_count == 0))
            {
                fclose(image);
            }
            
            // Initializing the new JPEG file
            sprintf(filename, "%03i.jpg", file_count);
            image = fopen(filename, "w");
            file_count++;
        }
        
        // Writing form buffer into the output file
        if (!(file_count == 0))
        {
            fwrite(&buffer, 512, 1, image);
        }
    }
    
    // Closing all files
    fclose(input_file);
    fclose(image);
    return 0;
 
}