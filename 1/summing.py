def sum_numbers(numbers=None):
    sumOfNumbers = 0
    if numbers == None:
        for number in range(0,101):
            sumOfNumbers = sumOfNumbers + number
            print(sumOfNumbers) 

    else:
        for number in numbers: 
            sumOfNumbers += number

    return(sumOfNumbers)  



