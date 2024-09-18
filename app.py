
from cal_fun import do_addition, do_subtraction,do_division
from multiply import do_multiplication
# from area import ar
def main():
    print("Welcome to the calculator app")
    print("""\nSelect the function from the given option
          1. Addition
          2. Subtraction
          3.Multiplication
          4.Division
          
         
          """)

    user_input=input("Enter the number ")

    a = int(input('value of A '))
    b = int(input('value of B '))

    if user_input =='1':
        result = do_addition(a,b)
    elif user_input=='2':
        result = do_subtraction(a,b)
    elif user_input=='3':
        result = do_multiplication(a,b)
    elif user_input=='4':
        result = do_division(a,b)
 
    
    print("Result",result)

if __name__=="__main__":
    main()