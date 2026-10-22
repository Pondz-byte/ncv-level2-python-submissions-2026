mark = int(input("Enter the mark: "))
print("Mark entered:", mark)

if mark >= 0 and mark <= 100:
    
    if mark >=80:
        print("Outstanding")
        
    elif mark >= 70 and mark <= 79:
        print("Highly Competent")
    
    elif mark >= 50 and mark <= 69:
        print("Competent")
        
    elif mark >= 40 and mark <= 49:
        print("Not yet competent")
    
    else: 
        print("Not yet competent")
    
        
else: 
    print("Invalid")
    

    
    

    
    
