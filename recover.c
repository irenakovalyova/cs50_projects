#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
 
int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    
    char *input_file_name = argv[1];
    FILE *input_file = fopen(input_file_name, "r");
        
    if (input_file == NULL)
    {
        printf("Cannot open the file\n");
        return 2;
    }
    
    uint8_t buffer[512];
    int file_count = 0;
    char filename[8];
    FILE *image = NULL;
    
    while (fread(&buffer, 512, 1, input_file) == 1)
    {
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            if (!(file_count == 0))
            {
                fclose(image);
            }
            sprintf(filename, "%03i.jpg", file_count);
            image = fopen(filename, "w");
            file_count++;
        }
        if (!(file_count == 0))
        {
            fwrite(&buffer, 512, 1, image);
        }
    }
    fclose(input_file);
    fclose(image);
    return 0;
 
}