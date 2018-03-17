#출력
#print("hello world")
#print(1,"hello")
#print('1',"hello")

#뒤에서 세기
#print("안녕하세요"[-1])
#print("안녕하세요"[-2])
#print("안녕하세요"[-3])
#print("안녕하세요"[-4])
#print("안녕하세요"[-5])

#문자범위선택연산자
#print("#문자범위선택연산자")
#print("안녕하세요"[0:5])
#print("안녕하세요"[1:5])
#print("안녕하세요"[2:5])

#문자열의 길이 변환
#print(len("안녕세상아"));

#타입을 알자
#print(type("안녕하세요"))
#print(type(len("안녕하세요")))
#print(12)
#print(12.2)
#print(type(12))
#print(type(12.2))
#print(0)
#print(0.0)
#print(type(0))
#print(type(0.0))

#연산자
#print(5+7)
#print(5-7)
#print(5*7)
#print(5/7)
#print(3%2)
#print(5//7)
#print(2**1)
#print(2**2)
#print(2**3)

#괄호 (우선순위제공)
#print(1+1*2)
#print((1+1)*2)

#머리아픈 암산(우선순위)
#print(2+2-2*2/2*2)
#print(2-2+2/2*2+2)

#그렇다면 문자열에서도 우선순위는?
#print("안녕"+"하세요"*3)

#문자열과 숫자를 더하면 타입에러가 난다.
#string="문자열"
#number=123
#string+number

#변수
#pi=3.14159265
#print(pi)

#복합대입연산자
#a=0
#a+=3
#print(a)

#a=0
#a-=3
#print(a)

#a=2
#a*=3
#print(a)

#a=3
#a/=3
#print(a)

#a=1
#a**=3
#print(a)

#문자복합대입연산자
#a="hello"
#a+='world'
#print(a)

#a="hello"
#a*=3
#print(a)

#입력
#string=input("입력>")
#print(string)
#print("자료형:",type(string))

#오류!
#string=input()
#print(string+100)

#캐스트연산자
#a=float(input("첫번째숫자"))
#b=float(input("두번째숫자"))
#print(a+b)
#print(a-b)
#print(a*b)
#print(a/b)

#format()
#out="{},{},{},{}".format(53345,12,True,"VAL")
#print(type(out),out)
#"{} {}".format(1,2,3,4)#ERROR!!
#"{} {} {}".format(1,2)
#print("{:5d}".format(53))
#print("{:5d}".format(-53))
#print("{:05d}".format(43))
#print("{:05d}".format(-43))
#print("{:+d}".format(-43))
#print("{:+d}".format(43))
#print("{: d}".format(43))
#print("{: d}".format(-43)
#print("{:+5d}".format(52))#그냥 숫자앞에 붙인다.
#print("{:+5d}".format(-52))
#print("{:=+5d}".format(52))#등호는 기호를 앞으로 민다.
#print("{:=+5d}".format(-52))
#print("{:+05d}".format(52))
#print("{:+05d}".format(-52))
print("{:f}".format(52.123))#실수
print("{:15f}".format(52.123))
print("{:+15f}".format(52.123))
print("{:+015f}".format(52.213))

print("{:15.3f}".format(52.123))
print("{:15.2f}".format(52.123))
print("{:+15.1f}".format(52.523))
print("{:+15.0f}".format(52.523))































