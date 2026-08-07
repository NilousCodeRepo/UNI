#include <stdio.h>

int main()
{
    int array[] = {10,9,3,2,1};
    
    for(int index = 1; index <= sizeof(array)/sizeof(array[0]);  ++index)
    {
        int key = array[index];
        int prev_index = index - 1;

        while( prev_index >= 0 && array[prev_index] > key)
        {
            array[prev_index + 1] = array[prev_index];
            
            prev_index = prev_index - 1;

        }
        array[prev_index + 1] = key;//questa è la seconda parte dell'aggiornamento, dopo che 9 e 10 si scambiano, devo fare in modo di non lasciare la cella del 10 vuota, quindi ci metto il 9
    }

    for(int i = 0; i <= sizeof(array)/sizeof(array[0]); i++) printf("[%d]", array[i]);

    printf("\n");
    
	return 0;
}

