# 부가세 출력 프로그램 

'''
우리나라 부가가치세의 세율은 현재 10%
소비자 가격 = 물건 가격 + 부가세

소비자 가격 = 물건 가격 * 1.1
물건 가격 = 소비자 가격 * (1/1.1)
부가세 = 물건 가격 * 0.1 = 소비자 가격 * (1/11)
'''

# 물건 가격 5,000 & 부가세 10%
customer_price = 5000 * 1.1
print('소비자 가격:', int(customer_price))


'8,000원짜리 점심에는 부가세가 얼마나 포함되어 있을까?'
tax = 8000 * (1/11)
product_price = 8000 / 1.1
print('부가세(원):', round(tax), ', 물건 가격(원):', round(product_price))


'''
a = float(input('숫자를 하나 입력해 보세요: '))
print(type(a), a)
'''


# 서비스 가격 출력 프로그램 완성하기

service_price = [23, 40, 67]       

for price in service_price:
  price = price * 1.1
  print(price)


def print_service_price():
  price = float(input('서비스 가격을 입력하세요: '))
  valueAdded = input('부가세를 포함합니까? ( y / n ): ')

  price = round(price)

  if valueAdded is not ('y' or 'n'):
    valueAdded = input('y 또는 n으로 입력해 주세요: ')

    if valueAdded == 'y':
      price = price * 1.1

    elif valueAdded == 'n':
      price = price

  else:
    if valueAdded == 'y':
      price = price * 1.1

    elif valueAdded == 'n':
      price = price

  return round(price,1)    

print(print_service_price(), '만 원입니다.')




'''
코드를 좀 더 간결하게 짜고 싶은데 어떻게 해야 할지는 더 고민해야겠다.
try ~ catch, if ~ break 문을 사용하려 했는데 loop 일 경우에만 가능해서 작동이 되지 않는다.

어떤 문제를 해결하는 코드를 짜는 것도 좋지만 그 외의 경우를 어떻게 처리할 수 있을지도 항상 고려하는 연습을 해야겠다.
'''