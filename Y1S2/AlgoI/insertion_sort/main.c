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
        array[prev_index + 1] = key;
    }
    
	return 0;
}

