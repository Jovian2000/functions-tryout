# functions-tryout
## F1.5.01.L1
```python
def hoi():
    print("Hello from function town")

hoi() 
```
## F1.5.01.L2
```python
invoernummer = int(input("Van welk getal wilt u de tafel zien? "))
def getallen(nummer: int):
    for getal in range(1,11):
        print(getal, " x ", nummer, " = ", getal * nummer)
getallen(invoernummer)
```
## F1.5.01.L3
### programma 1
```python
def helloWorld(aantal):
    for word in range(aantal):
        print("Hello world!")
```
### programma 2
```python 
def addition(number1,number2) -> int:    
    return print (number1, " + ", number2, " = ", (number1+number2))
def substraction(number1,number2) -> int:    
    return print (number1, " - ", number2, " = ", (number1-number2))
def multiplication(number1,number2) -> int:    
    return print (number1, " x ", number2, " = ", (number1*number2))
def division(number1,number2) -> int:    
    return print (number1, " : ", number2, " = ", (number1/number2))
def increment(number) -> int:
    return print (number, " + ", 1 , " = ", (number + 1))
def decrement(number) -> int:
    return print (number, " - ", 1 , " = ", (number - 1))
```
### programma 3
```python
def namenEnLeeftijd():    
    while True:
        naam = input("Naam: ")
        if naam == "stop":
            break
        leeftijd = input("Leeftijd: ")
        if leeftijd == "stop":
            break
        print("Hallo", naam, ", je leeftijd is", leeftijd, "jaar")
```
