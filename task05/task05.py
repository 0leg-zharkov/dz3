def summ():
    ex = False
    fResult = 0
    while ex == False:
        lNumbers = input().split()
        result = 0
        for i in range(len(lNumbers)):
            if lNumbers[i] =='q':
                ex = True
                break
            else:
                result = result + int(lNumbers[i])
        fResult = fResult + result
        print(f"�����: {fResult}")
    print(f'�����: {fResult}')
summ()

 