/* QuickSort
1. Get the array: arr = {1, 0, -6, 2, 5, 3, 2}
2. arr[6] ===== pivot (опорный элемент)
3. Вызвать шаги 1-2 для подмассива слева от pivot и справа от pivot
*/

int[] arr = { 0, -5, 2, 3,5, 9, -1, 7};
int[] res = QuiakSort(arr, 0, arr.Length - 1);

Console.WriteLine($"Отсортированный массив {string.Join(", ", res)}");

int[] QuiakSort(int[] inputArray, int minIndex, int maxIndex)
{
    if (minIndex >= maxIndex) return inputArray;
    int pivot = GetPivotindex(inputArray, minIndex, maxIndex);
    QuiakSort(inputArray, minIndex, pivot - 1);
    QuiakSort(inputArray, pivot + 1, maxIndex);
    return inputArray;
}

int GetPivotindex(int[] inputArray, int minIndex, int maxIndex)
{
    int pivotIndex = minIndex - 1;
    for (int i = minIndex; i <= maxIndex - 1; i++)
    {
        if (inputArray[i] < inputArray[maxIndex])
        {
            pivotIndex++;
            Swap(inputArray, i, pivotIndex);
        }
    }
    pivotIndex++;
    Swap(inputArray, pivotIndex, maxIndex);
    return pivotIndex;
}

void Swap(int[] inpurarray, int leftValue, int rightValue)
{
    int temp = inpurarray[leftValue];
    inpurarray[leftValue] = inpurarray[rightValue];
    inpurarray[rightValue] = temp;
}