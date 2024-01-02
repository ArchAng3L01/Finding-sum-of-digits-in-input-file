#function for return sum of digits in current string
def find_sum_of_digits(a):
    #sum of digits in string
    sm = 0
    
    #check all symbols in string
    for i in range(len(a)):
        #check for right ASCII code (we need 
        # [48, 57] for [0, 9] respectively)
        if(ord(a[i]) >= 48 and ord(a[i]) <= 57):
            sm += (ord(a[i]) - 48)
            
    #return our sum of digits
    return sm

def main():
    #create an object - open file with name 'input.txt'
    #which can recognize russian alphabet 
    #there's also a mode = 'r' only for read information from file
    input = open('input.txt', encoding='utf-8', mode = 'r')

    #create a list with all strings from input file
    s = list(input.readlines())

    #variable for sum all digits from input file
    sum_of_digits = 0

    #let's find sum of digits in input file
    for i in s:
        #to the sum_of_digits will add new sum of digits from string i
        sum_of_digits += find_sum_of_digits(i)
        
    #close input file
    input.close()

    #create an object - open file with name 'output.txt'
    #which can recognize russian alphabet 
    #there's also a mode = 'w' only for writing information to the file
    output = open('output.txt', encoding = 'utf-8', mode = 'w')

    #create vatiable with output information with sum of digits from input file
    info = "Sum of digits from file with name: " + input.name + " is equals " + str(sum_of_digits)

    #write to the output file our info
    output.write(info)

    #close output file
    output.close()

    #clearing a list
    s.clear()

if __name__ == '__main__':
    main()
