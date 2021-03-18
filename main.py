import re
def main():

    print("Enter filename: ")
    filename  = str(input())
    print("Enter operation: ")
    operation = str(input())

    
    numbers = read_file(filename)
    res_negative, res_positive = arithmetic_operation(numbers,operation)
    
    save_results(res_negative,'negative_results.txt')
    save_results(res_positive,'positive_results.txt')
    
    
def read_file(filename):
    
    list_numb = []
    with open(filename, 'r') as reader:
        for line in reader:
            for number in line.split():
                try:
                    list_numb.append(float(number))
                except ValueError:
                    pass
    return list_numb           
                        
                        
            #print([int(s) for s in re.findall(r'\b\d+\b', line)])
    
def arithmetic_operation(numbers,operation):
    
    res_negative = []
    res_positive = []
    
    for x in range(0,len(numbers),2):
    
            if(operation == '*'):
                res = numbers[x] * numbers[x+1]
                if(res<0):
                    res_negative.append(str(res))
                else:
                    res_positive.append(str(res))
            if(operation == '/'):
                res = numbers[x] / numbers[x+1]
                if(res<0):
                    res_negative.append(str(res))
                else:
                    res_positive.append(str(res))   
            if(operation == '+'):
                res = numbers[x] + numbers[x+1]
                if(res<0):
                    res_negative.append(str(res))
                else:
                    res_positive.append(str(res))  
            if(operation == '-'):
                res = numbers[x] - numbers[x+1]
                if(res<0):
                    res_negative.append(str(res))
                else:
                    res_positive.append(str(res))       
                
    return res_negative, res_positive
             
              
def save_results(results, filename):
    
    with open(filename,'w') as writer:
        for res in results:
            writer.write(res+'\n')
            


main()
