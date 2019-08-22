def sum_numbers(numbers=None):
    sumOfNumbers = 0
    if numbers == None:
        for number in range(100):
            sumOfNumbers += number

    else:
        for number in numbers: 
            sumOfNumbers += number
    return(sumOfNumbers)

    
