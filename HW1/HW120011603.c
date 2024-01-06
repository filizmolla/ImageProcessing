#include<stdio.h>
#include<stdlib.h>
#include <ctype.h>
#include <string.h>


typedef struct {
	char pgmType[3];
	int rows, cols;
	int maxVal;
	int ** pixels;
}Image;

Image myImage;
Image *readPGM(const char *filename);

int **allocate_dynamic_matrix(int row, int col){
    int **ret_val;
    int i;
 
    ret_val = (int **)malloc(sizeof(int *) * row);
    if (ret_val == NULL) {
        perror("memory allocation failure");
        exit(EXIT_FAILURE);
    }
 
    for (i = 0; i < row; ++i) {
        ret_val[i] = (int *)malloc(sizeof(int) * col);
        if (ret_val[i] == NULL) {
            perror("memory allocation failure");
            exit(EXIT_FAILURE);
        }
    }
 
    return ret_val;
}
 
void deallocate_dynamic_matrix(int **matrix, int row){
    int i;
 
    for (i = 0; i < row; ++i) {
        free(matrix[i]);
    }
    free(matrix);
}

void ignoreComments(FILE * fp){
	int ch; 
	char line[100];
	
    while ((ch = fgetc(fp)) != EOF && isspace(ch));
 
    if (ch == '#') {
        fgets(line, sizeof(line), fp);
        ignoreComments(fp);
    }
    else
        fseek(fp, -1, SEEK_CUR);
}


Image *readPGM(const char *filename) {
    FILE *file = fopen(filename, "rb");
    if (file == NULL) {
        fprintf(stderr, "\n\nFile '%s' cannot be opened! \n", filename);
        exit(1);
    }

    char magic[3];
    Image *image = (Image *)malloc(sizeof(Image));

    fscanf(file, "%2s" , magic);
    strcpy(image->pgmType, magic);
    ignoreComments(file);
    
    if (fscanf(file, "%d %d %d", &image->cols, &image->rows, &image->maxVal) != 3) {
        fprintf(stderr, "Invalid PGM file format.\n");
        exit(1);
    }   
	
    if (image->maxVal != 255) {
        fprintf(stderr, "This program only supports 8-bit depth PGM files.\n");
        exit(1);
    }

	if(strcmp(magic, "P2") == 0){
		image->pixels = (int **)malloc(image->rows * sizeof(int *));
    	for (int i = 0; i < image->rows; i++) {
        	image->pixels[i] = (int *)malloc(image->cols * sizeof(int));
        	for (int j = 0; j < image->cols; j++) {
            	fscanf(file, "%d", &image->pixels[i][j]);
        	}
    	}
	}else if(strcmp(magic, "P5") == 0){
		image->pixels = allocate_dynamic_matrix(image->rows, image->cols);
		
	    for (int i = 0; i < image->rows; i++) {
	        for (int j = 0; j < image->cols; j++) {
	            unsigned char pixel;
	            if (fread(&pixel, sizeof(unsigned char), 1, file) != 1) {
	            	fprintf(stderr, "Error reading image data at (%d, %d)\n", i, j);
	                free(image);
	                fclose(file);
	                return NULL;
	            }
	            image->pixels[i][j] = (int)pixel;
	            if(pixel > 255){
	            	printf("!\n");
				}	
	        }
	    }
		
	}else{
		printf("Invalid file type!");
	}


    fclose(file);
    return image;
}

Image *negatifAl(Image *girisGoruntu) {
	int maxVal = girisGoruntu->maxVal;
    int rows = girisGoruntu->rows;
    int cols = girisGoruntu->cols;
	
    Image *cikis_goruntu = (Image *)malloc(sizeof(Image));
    cikis_goruntu->rows = rows;
    cikis_goruntu->cols = cols;
	cikis_goruntu->maxVal = maxVal;
    cikis_goruntu->pixels = allocate_dynamic_matrix(rows, cols);

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cikis_goruntu->pixels[i][j] = maxVal - girisGoruntu->pixels[i][j];
        }
    }

    return cikis_goruntu;
}



Image *changeBrightness(Image *girisGoruntu, int X){
	int maxVal = girisGoruntu->maxVal;
    int rows = girisGoruntu->rows;
    int cols = girisGoruntu->cols;
	
    Image *cikis_goruntu = (Image *)malloc(sizeof(Image));
    cikis_goruntu->rows = rows;
    cikis_goruntu->cols = cols;
	cikis_goruntu->maxVal = maxVal;
    cikis_goruntu->pixels = allocate_dynamic_matrix(rows, cols);
	
	int newMax = 255, newMin = 0;
	
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
        	int newPixelValue = girisGoruntu->pixels[i][j] + X;
        	if(newPixelValue > newMax){
        		newMax = newPixelValue;
			}
			if(newPixelValue < newMin){
				newMin = newPixelValue;
			}
            cikis_goruntu->pixels[i][j] = newPixelValue;
        }
    }
    float maxValue = (float) maxVal; 

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cikis_goruntu->pixels[i][j] = ( (maxValue* (cikis_goruntu->pixels[i][j] - newMin)) / (newMax - newMin));
        }
    }
    
    return cikis_goruntu;

}
	

Image * thresholding(Image *girisGoruntu, int T){
	int maxVal = girisGoruntu->maxVal;
    int rows = girisGoruntu->rows;
    int cols = girisGoruntu->cols;
	
    Image *cikis_goruntu = (Image *)malloc(sizeof(Image));
    cikis_goruntu->rows = rows;
    cikis_goruntu->cols = cols;
	cikis_goruntu->maxVal = maxVal;
    cikis_goruntu->pixels = allocate_dynamic_matrix(rows, cols);

    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            cikis_goruntu->pixels[i][j] = (girisGoruntu->pixels[i][j] > T) ? 255 : 0;
        }
    }

    return cikis_goruntu;
}

Image * applyMask(Image *girisGoruntu, float mask[3][3]){
	int maxVal = girisGoruntu->maxVal;
    int rows = girisGoruntu->rows;
    int cols = girisGoruntu->cols;
	
    Image *cikis_goruntu = (Image *)malloc(sizeof(Image));
    cikis_goruntu->rows = rows;
    cikis_goruntu->cols = cols;
	cikis_goruntu->maxVal = maxVal;
    cikis_goruntu->pixels = allocate_dynamic_matrix(rows, cols);
    
    
    int newMax = 255, newMin = 0;
    
	for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
        	
            int toplam = 0;
            for (int m = -1; m <= 1; m++) {
                for (int n = -1; n <= 1; n++) {
                    int x = i + m;
                    int y = j + n;
                    if (x < 0 || x >= rows || y < 0 || y >= cols) {
                        toplam += 0;
                    } else {
                        toplam += girisGoruntu->pixels[x][y] * (mask[m + 1][n + 1]);
                    }
                }
            }
            //toplam = toplam / 16;
            cikis_goruntu->pixels[i][j] = toplam;
            
            if(toplam > newMax){
        		newMax = toplam;
            }
            if(toplam < newMin){
				newMin = toplam;
				}
        }
    }
    printf("\n MAX:%d, MIN:%d", newMax, newMin);
    float maxValue = (float) maxVal; 
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            //cikis_goruntu->pixels[i][j] = cikis_goruntu->pixels[i][j] /2;
            cikis_goruntu->pixels[i][j] = ( (maxValue* (cikis_goruntu->pixels[i][j] - newMin)) / (newMax - newMin));

         }
    }
   
    return cikis_goruntu;
}


void writePGM(const char *filename, Image *image) {
    FILE *file = fopen(filename, "w");
    if (file == NULL) {
        fprintf(stderr, "File can't be opened: %s\n", filename);
        exit(1);
    }

    fprintf(file, "P2\n%d %d\n255\n", image->cols, image->rows);
    for (int i = 0; i < image->rows; i++) {
        for (int j = 0; j < image->cols; j++) {
            fprintf(file, "%d ", image->pixels[i][j]);
        }
        fprintf(file, "\n");
    }

    fclose(file);
}


int main(int argc, char *argv[]) {

  
	char inputFileLocation[250];
	char outputFileLocation[250];
	
	char inputFilename[150];
    char outputFilename[150];
    printf("Images:\n\tcoins.ascii.pgm\n\tfruit.pgm\n\tlena.pgm\n\tsaturn.ascii.pgm\n");
	
	printf("Enter the name of the image: ");
    scanf("%s", inputFilename);
    
    snprintf(outputFilename, sizeof(outputFilename), "output.pgm"); 

	//printf("Enter the name of the output image:");
	//scanf("%s", outputFilename);
	
 	//printf("\nImage Name:%s", inputFilename);
	//printf("\nImage Output Name:%s", outputFilename);
	
    snprintf(inputFileLocation, sizeof(inputFileLocation), "./images/%s", inputFilename);
    snprintf(outputFileLocation, sizeof(outputFileLocation), "./output/%s", outputFilename); 
    //printf("\nImage Location:%s\n", inputFileLocation);
    
    
   printf("Operations:\n\t1. Negative image\n\t2.Change brightness\n\t3.Apply threshold\n\t4.Apply mask 1 convolution\n\t5. Apply mask 2 convolution\n");
   
	int islem = 1;
	printf("\nSelect the operation:");
	scanf("%d", &islem);
	
	Image *giris_goruntu = readPGM(inputFileLocation);
    Image *cikis_goruntu = NULL;



    switch (islem) {
        case 1:
             cikis_goruntu = negatifAl(giris_goruntu);
            break;
        case 2:
        	printf("\n2.Changing Brightness:\n");
            int X;
            printf("Enter brightness value: ");
            scanf("%d", &X);
            cikis_goruntu = changeBrightness(giris_goruntu, X);
            break;
        case 3:
           	printf("\n3.Applying Threshold:\n");
            int T;
            printf("Enter threshold value: ");
            scanf("%d", &T);
            cikis_goruntu = thresholding(giris_goruntu, T);
            break;
        case 4:
           	printf("\n4.Mask 1\n");
        	float mask1[3][3] = { {1, 2, 1}, {2, 4, 2}, {1, 2, 1} };
        	for (int i = 0; i < 3; i++) {
				for (int j = 0; j < 3; j++) {
					mask1[i][j] =  mask1[i][j] / 16;
				}
				printf("\n");
			}
            //cikis_goruntu = applyMask(giris_goruntu, mask1);
            break;
            
        case 5: 
        	printf("\n5.Mask 2 ");
        	float mask2[3][3] = { {-1, -1, -1}, {-1, 9, -1}, {-1, -1, -1} };
        	
        	cikis_goruntu = applyMask(giris_goruntu, mask2);
        	break;
        default:
            printf("Geçersiz işlem kodu.\n");
            break;
    }

    if (cikis_goruntu != NULL) {
        writePGM(outputFileLocation, cikis_goruntu);
        deallocate_dynamic_matrix(cikis_goruntu->pixels, cikis_goruntu->rows);
        free(cikis_goruntu);
    }
    
	deallocate_dynamic_matrix(giris_goruntu->pixels, giris_goruntu->rows);
    free(giris_goruntu);


	
	
	return 0;
}
