import random

def swap(a , b):
    return b , a

class bubble:
    def bubbleSort(numbers):          
        for i in range(len(numbers) - 1):
            for j in range(len(numbers) - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j] , numbers[j + 1] = numbers[j + 1] , numbers[j]
                    yield numbers[:] , i , j , False
                    
        yield numbers[:] , i , j , True
    
class selection:
    def selectionSort(numbers):
        for i in range(len(numbers) - 1):
            min_index = i
            
            for j in range(i + 1 , len(numbers)):
                if numbers[j] < numbers[min_index]:
                    min_index = j
                    
                yield numbers[:] , i , j , False
                    
            numbers[i] , numbers[min_index] = numbers[min_index] , numbers[i]
            yield numbers[:] , i , j , False
            
        yield numbers[:] , i , j , True

    
class insertion:
    def insertionSort(numbers):
        for i in range(1 , len(numbers)):
            key = numbers[i]
            j = i - 1
            
            while j >= 0 and numbers[j] > key:
                numbers[j + 1] = numbers[j]
                j -= 1
                yield numbers[:] , i , j , False
                
            numbers[j + 1] = key
            yield numbers[:] , i , j , False
            
        yield numbers[:] , i , j , True
        
class quick:
    def quickSort(numbers , left , right):
        if left >= right:
            yield numbers[:] , left , right , False
            return

        index_pivot = (left + right) // 2
        pivot = numbers[index_pivot]
        numbers[index_pivot] , numbers[right] = numbers[right] , numbers[index_pivot]
        i = left - 1
        
        for j in range(left , right):
            if numbers[j] < pivot:
                i += 1
                numbers[i] , numbers[j] = numbers[j] , numbers[i]
                
            yield numbers[:] , left , right , False
            
        numbers[i + 1] , numbers[right] = numbers[right] , numbers[i + 1]
        
        yield numbers[:] , left , right , False
        
        yield from quick.quickSort(numbers , left , i)
        yield from quick.quickSort(numbers , i + 2 , right)
        
class Merge:
    def merge(numbers , left , mid , right):
        temp = []
        i = left
        j = mid + 1
        
        while i <= mid and j <= right:
            if numbers[i] < numbers[j]:
                temp.append(numbers[i])
                i += 1
                yield numbers[:] , i , j , False
            else:
                temp.append(numbers[j])
                j += 1
                yield numbers[:] , i , j , False
                
        while i <= mid:
            temp.append(numbers[i])
            i += 1
            yield numbers[:] , i , j , False
        
        while j <= right:
            temp.append(numbers[j])
            j += 1
            yield numbers[:] , i , j , False
            
        for k in range(len(temp)):
            numbers[left + k] = temp[k]
            yield numbers[:] , i , j , False
            
    def mergeSort(numbers , left , right):
        if left >= right:
            yield numbers[:] , left , right , False
            return
        
        mid = (left + right) // 2
        
        yield from Merge.mergeSort(numbers , left , mid)
        yield from Merge.mergeSort(numbers , mid + 1 , right)
        
        yield from Merge.merge(numbers , left , mid , right)
        
class bogo:
    def isSorted(numbers):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                return False
            
        return True
            
    def bogoSort(numbers):
        while not bogo.isSorted(numbers):
            random.shuffle(numbers)
            yield numbers[:] , 0 , 0 , False
            
class tim:
    def insertionSort(numbers , left , right):
        for i in range(left + 1 , right + 1):
            key = numbers[i]
            j = i - 1

            while j >= left and numbers[j] > key:
                numbers[j + 1] = numbers[j]
                j -= 1
                yield numbers[:] , i , j , False

            numbers[j + 1] = key
            yield numbers[:] , i , j , False

    def merge(numbers , l , m , r):
        left = numbers[l : m + 1]
        right = numbers[m + 1 : r + 1]

        i , j , k = 0 , 0 , l

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                numbers[k] = left[i]
                i += 1
            else:
                numbers[k] = right[j]
                j += 1
                
            k += 1
            yield numbers[:] , i , j , False

        while i < len(left):
            numbers[k] = left[i]
            i += 1
            k += 1
            yield numbers[:] , i , j , False

        while j < len(right):
            numbers[k] = right[j]
            j += 1
            k += 1
            yield numbers[:] , i , j , False


    def timSort(numbers):
        RUN = 32

        for i in range(0 , len(numbers) , RUN):
            yield from tim.insertionSort(numbers , i , min(i + RUN - 1 , len(numbers) - 1))

        size = RUN

        while size < len(numbers):
            for left in range(0 , len(numbers) , 2 * size):
                mid = min(len(numbers) - 1 , left + size - 1)
                right = min((left + 2 * size - 1) , (len(numbers) - 1))

                if mid < right:
                    yield from tim.merge(numbers , left , mid , right)

            size *= 2
            
        yield numbers[:] , i , 0 , True