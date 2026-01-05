'''
Docstring for assignment1
Q1. Define a variable of all the labours and print the name of each labour.
Condition:-
    Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh
    labour variable should be something like this 1st_labour, 2nd_labour and so on.'''

Labour_1 = "Mahesh"
Labour_2 = "Mithilesh"
Labour_3 = "Ramesh"
Labour_4 = "Sumesh"

print(f":Labour names are {Labour_1},{Labour_2},{Labour_3},{Labour_4}")

'''Q2. Define a variable of all the labours daily wage and print the name and wage of each labour.
Condition:-
    Labour names are:- Mahesh, Mithilesh,Ramesh, Sumesh and wages are 500,400,400,300 respectively
    labour variable should be something like this 1st_labour_name,1st_labour_wage, 2nd_labour_name,
    2nd_labour_wage and so on.
    You are bound to use string formatting'''

Labour_1_name = "Mahesh"
Labour_2_name = "Mithilesh"
Labour_3_name = "Ramesh"
Labour_4_name = "Sumesh"

Labour_1_wage = 500
Labour_2_wage = 400
Labour_3_wage = 400
Labour_4_wage = 300

print(f"Labour names are {Labour_1_name} and the wages of the labour {Labour_1_wage} \n {Labour_2_name} and the wage of the labour is {Labour_2_wage} \n {Labour_3_name} and the wage of the labour is {Labour_3_wage} \n {Labour_4_name} and the wage of the labour is{Labour_4_wage} respectively")

'''Q3. I want to print this paragraph and its line number from which this paragraph is printing
    """ Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that
    we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the 
    help of 'Python programming'. We have total land is of \100 ft * 100ft /, to colmplete the house 
    we have total 6 labours with 'different skill set like "\\ building wall or building roof \\".
            I have to print this paragraph as it is given here."""

    Condition:- 
    You can't use triple quote.
    Triple quote at starting is also a part of paragraph.'''


print(
    '""" Programming aasan hai. We are going to learn this in depth. While learning we have to make sure that\n'
    '    we are implemeting all the logics by ourself. The aim here is to build our "4 BHK" house with the \n'
    "    help of 'Python programming'. We have total land is of \\100 ft * 100ft /, to colmplete the house \n"
    "    we have total 6 labours with 'different skill set like \"\\\\ building wall or building roof \\\\\".'\n"
    '            I have to print this paragraph as it is given here."""'
)


'''Q4. When do we get NameError?'''

print(f"Ans: when we typed variable name incorrectly/undefined")


'''Q5. Python is a high level language. What does that mean by high level?'''

print(f"Ans: High level language means it is human understandable format unlike binarycode/machine language ")


'''Q6. What is compiled and Inetrpreted language, list a few?'''

print(f"compled means the whole code is executed at once and is fast(C++) . but, where as inetrpreted language means the code executes line by line (python)")
      
'''Q7. Get all varibales address from RAM and you find if something is similar?'''

print(id(labour_1st),id(labour_2nd),id(labour_3rd),id(labour_4th),id(labour_1st_wage),id(labour_2nd_wage),id(labour_3rd_wage),id(labour_4th_wage))

print(f"observation: where wage is same RAM address ")