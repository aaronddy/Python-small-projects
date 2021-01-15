'03_1_사업성 분석하기'

import numpy as np
import numpy_financial as npf

'1. 자본의 현재 가치 구하기'
'''
discount = .05
cashflow = 100
print('할인율:', discount, '현금흐름:', cashflow)

'현재 가치(pv)를 구하는 함수'
def present_value(n):
  return (cashflow / ((1+discount) ** n))

print('1년 차:', present_value(1))
print('2년 차:', present_value(2))

'20년 동안 발생할 현재 가치'
for i in range(20):
  print(i, "년차:", present_value(i))
'''


'2. 놀이공원 사업의 사업성 분석하기'

'초기값 설정'
loss = [-750, -250]
profit = [100] * 18
# print(profit)

cf = loss + profit
print(type(cf), cf)                    # list

cashflow = np.array(cf)
print(cashflow.dtype, cashflow)        # int32 array



'순현재가치(NPV)와 내부수익률(IRR) 구하기'

npv = npf.npv(0.045, cashflow)
print("NPV:", npv)

irr = npf.irr(cashflow)
print("IRR", irr)

print("순현재가치는 약", round(npv,2), "이고 내부수익률은", round(irr,2), "% 정도가 예상된다.")