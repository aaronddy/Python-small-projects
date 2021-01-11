# lambda로 간단하게 함수 만들기

y = lambda x : 3*x                  # y = 3x 방정식 생성
print(y(24))                        # 72

add = lambda a,b : (a*b) + 16       # y = (a*b) + 16
print(add(2, 9))                    # 34



littlePrince = '''
여섯 살 적에 나는 '체험한 이야기'라는 제목의, 원시림에 관한 책에서 기막힌 그림 하나를 본 적이 있다.
맹수를 집어삼키고 있는 보아뱀 그림이었다. 위의 그림은 그것을 옮겨 그린 것이다. 그 책에는 이렇게 씌어 있었다.
'보아뱀은 먹이를 씹지도 않고 통째로 집어삼킨다. 그리고는 꼼짝도 하지 못하고 여섯 달 동안 잠을 자면서 그것을 소화시킨다.'
'''

print(littlePrince[:10])            # 여섯 살 적에 나

short = lambda x : x[1:44]
print(short(littlePrince))          # 여섯 살 적에 나는 '체험한 이야기'라는 제목의, 원시림에 관한 책에서 기막힌





# lambda로 환율계산기 만들기
# 1원의 환율이 0.00086라고 가정

exchange = lambda x : x * 0.00086
print(exchange(10000))              # 10,000 = $ 8.6
print(exchange(340000))             # 340,000 = $ 292.4

