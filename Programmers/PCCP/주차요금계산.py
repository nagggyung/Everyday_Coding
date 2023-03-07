# 내 풀이
'''
math.ceil(): 실수를 입력하면 올림하여 정수를 반환한다.

'''


import math
import collections

def solution(fees, records):
    answer = []
    base_time, base_fee, unit_time, unit_fee = fees
    fee = collections.defaultdict(int)
    
    for i in range(len(records)):
        time, num, state = records[i].split()
        if state == 'IN':
            checkout_time = '23:59'
            for j in range(i+1, len(records)):
                t, n, s = records[j].split()
                if s == 'OUT' and num == n:
                    checkout_time = t
                    break
        
            # 누적 주차시간 
            inhour, inmins = list(map(int, time.split(':')))
            outhour, outmins = list(map(int, checkout_time.split(':')))
            fee[num] += ((outhour*60 + outmins) - (inhour*60 + inmins))
    
    # 주차요금 계산
    for k, v in fee.items():
        if v <= base_time:
            fee[k] = base_fee
        else:
            fee[k] = base_fee + math.ceil((v-base_time)/unit_time)*unit_fee
        
    total_fee = dict(sorted(fee.items()))
    return list(total_fee.values())
    
        

        
        
                
# 풀이2 : 강의듣고나서 다시 풀어보기

import math
import collections

def solution(fees, records):
    answer = []
    base_time, base_fee, unit_time, unit_fee = fees
    inTime = [0]*10000
    isIn = [0]*10000
    sumT = [0]*10000
    
    for record in records:
        time, num, state = record.split()
        num = int(num)
        if state == 'IN':
            inhour, inmins = list(map(int,time.split(':')))
            inTime[num] = inhour * 60 + inmins
            isIn[num] = 1
        if state == 'OUT':
            outhour, outmins = list(map(int,time.split(':')))
            sumT[num] += ((outhour * 60 + outmins) - (inTime[num]))
            isIn[num] = 0
    
    for i in range(len(isIn)):
        if isIn[i]:
            sumT[i] += ((23*60 + 59) -inTime[i]) 
    for j in range(len(sumT)):
        if sumT[j] > 0:
            if sumT[j] <= base_time:
                answer.append(base_fee)
            else:
                answer.append(base_fee+math.ceil((sumT[j]-base_time)/unit_time)*unit_fee)
    return answer
    