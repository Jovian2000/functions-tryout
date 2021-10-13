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
