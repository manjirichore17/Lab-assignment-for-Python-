bal = 0

def show(): print("Balance:", bal)

def dep(x):
    global bal
    bal += x

def wd(x):
    global bal
    if x <= bal:
        bal -= x
    else:
        print("Low balance")

while True:
    print("\n1.Show 2.Deposit 3.Withdraw 4.Exit")
    ch = int(input("Choice: "))
    
    if ch == 4:
        break
    
    if ch == 1:
        show()
    elif ch == 2:
        dep(int(input("Amount: ")))
    elif ch == 3:
        wd(int(input("Amount: ")))