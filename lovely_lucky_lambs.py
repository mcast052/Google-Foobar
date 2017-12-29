def stingy(total_lambs): # Fibonacci sequence
    num = 1
    tot = total_lambs - 1
    pay = [1] # At least 1 henchmen on team, rule 1 
    
    while tot > 0: 
        if num == 1 and not( tot - 1 < 0 ): 
            pay.append(1)
            tot = tot - 1
        else: 
            payAmnt = pay[num-1] + pay[num-2]
            if tot - payAmnt < 0: 
                break 
            pay.append(payAmnt) 
            tot = tot - payAmnt
        num = num + 1
        
    print tot
    return num

def generous(total_lambs): # Powers of 2
    num = 1
    tot = total_lambs - 1
    pay = [1] 
    
    while tot > 0: 
        payAmnt = pow(2, num)
        if tot - payAmnt < 0: 
            break
        pay.append(payAmnt) 
        tot = tot - payAmnt
        num = num + 1
    
    return num

def answer(total_lambs):
    # your code here
    diff = stingy(total_lambs) - generous(total_lambs)
    return diff
    
print answer(2)
    