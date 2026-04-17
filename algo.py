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