def swap(a , b):
    return b , a

class bubble:
    def bubbleSort(numbers , i , j):          
        if i >= len(numbers) - 1:
            return numbers , i , j , True
        
        if j >= len(numbers) - i - 1:
            return numbers , i + 1 , 0 , False
        
        if numbers[j] > numbers[j + 1]:
            numbers[j] , numbers[j + 1] = swap(numbers[j] , numbers[j + 1])
            
        return numbers , i , j + 1 , False
    
class selection:
    def selectionSort(numbers , i , j , min_index):
        if i >= len(numbers) - 1:
            return numbers , i , j , True , 0
        
        if j >= len(numbers):
            if min_index != i:
                numbers[i] , numbers[min_index] = swap(numbers[i] , numbers[min_index])
            
            return numbers , i + 1 , i + 2 , False , i + 1
        
        if numbers[j] < numbers[min_index]:
            min_index = j
            
        return numbers , i , j + 1 , False , min_index
    
class insertion:
    def insertionSort(numbers , i , j , key):
        if i >= len(numbers):
            return numbers , i , j , True , key
        
        if j >= 0 and numbers[j] > key:
            numbers[j + 1] = numbers[j]
            return numbers , i , j - 1 , False , key
        else:
            numbers[j + 1] = key
        
        try:    
            return numbers , i + 1 , i , False , numbers[i + 1]
        except:
            return numbers , i , j , True , key
        
class quick:
    def quickSort(numbers , left , right):
        if left >= right:
            yield numbers[:] , left , right , False
            return

        pivot = numbers[right]
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