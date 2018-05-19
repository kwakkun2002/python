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
#print("{:f}".format(52.123))#실수
#print("{:15f}".format(52.123))
#print("{:+15f}".format(52.123))
#print("{:+015f}".format(52.213))
#print("{:15.3f}".format(52.123))#소수점에서 반올림
#print("{:15.2f}".format(52.123))
#print("{:+15.1f}".format(52.523))
#print("{:+15.0f}".format(52.523))
#print("{:g}".format(52.0))

#다른 문자열 관련함수들
#str="Hello World"
#str_up=str.upper()
#str_low=str.lower()
#print(str_up)
#print(str_low)

#str_a="Hello world"
#str_a.upper()
#print(str_a)

#공백제거함수
#input="""
#  안녕하세요
#문자열 함수를 알아봅시다
#"""
#print(input.strip())

#find
#a="안녕안녕하세요".find("안녕")
#b="안녕안녕하세요".rfind("안녕")
#print(a)
#print(b)

#in
#print("안녕"in"안녕하세요")

##if문
#num=input("정수입력")
#num=int(num)

#if num>0:
#    print("양수입니다.")
#if num<0:
#    print("음수입니다")
#if num==0:
#    print("0입니다")

#import datetime

#now=datetime.datetime.now()

#if now.hour < 12:
#    print("현재시간은 {}시로 오전입니다.".format(now.hour))
#if now.hour >= 12:
#    print("현재시간은 {}시로 오후입니다.".format(now.hour-12))

#if 3<=now.month<=5:
#    print("현재시간은 {}월로 봄입니다.".format(now.month))
#if 6<=now.month<=8:
#    print("현재시간은 {}월로 여름입니다.".format(now.month))
#if 9<=now.month<=11:
#    print("현재시간은 {}월로 가을입니다.".format(now.month))
#if now.month==12 or 1<=now.month<=2:
#    print("현재시간은 {}월로 겨울입니다.".format(now.month))
#print()


#number=int(input("정수 입력 "))

#if number%2==0:
#    print("{}는 짝수 입니다.".format(number))
#else:
#     print("{}는 홀수 입니다.".format(number))

#score=float(input("학점입력"))

#if 4.5<=score:
#    print("신")
#elif 4.2<=score:
#    print("교수님의 사랑")
#elif 3.5<=score:
#    print("현체재의 수호자")
#elif 2.8<=score:
#    print("일반인")
#elif 2.3<=score:
#    print("일탈을 꿈꾸는 소시민")
#elif 1.75<=score:
#    print("오락문화의 선구자")
#elif 1.0<=score:
#    print("불가촉천민")
#elif 0.5<=score:
#    print("자벌레")
#elif 0<=score:
#    print("플랑크톤")
#else:
#    print("시대를 앞서 가는 혁명의 씨앗")


#리스트
#arr=[273,32,102,"문자열",True]
#print(arr)

#list_a=[1,2,3]
#list_b=[4,5,6]

#print(list_a)
#print(list_b)
#print(list_a+list_b)
#print(list_a*3)
#print(len(list_a))

#list_a=[1,2,3]
#print(list_a)

#list_a.append(4)
#list_a.append(5)

#list_a.insert(4,10)
#print(list_a)

#list_a=[1,2,3]
#list_a.extend([4,5,6])
#print(list_a)

#리스트함수
#list_a=[0,1,2,3,4]
#del list_a[1]
#print(list_a)
#list_a.pop(2)
#print(list_a)
#list_a=[1,2,1,2]
#list_a.remove(2)
#print(list_a)

#list_a=[0,1,2,3,4,5,5,5]
#list_a.clear()
#print(list_a)

#list_a=[1,2,3,4,5]
#print(1 in list_a);
#print(2 in list_a);
#print(3 in list_a);
#print(4 in list_a);
#print(5 in list_a);
#print(6 in list_a);

#arr=[1,2,3,4,5]
#for a in "안녕하세요":
#    print(a)

#a={
#    "name":"7D 건조망고",
#    "type":"당절임",
#    "ingredient":["망고","설탕","메타중아황산나트륨"],
#    "origin":"필리핀"
#    }
#print(a)
#a["name"]="8d 건조망고"
#a["name2"]="건조망고"
#print(a)

#a={
#    "name":"7D 건조망고",
#    "type":"당절임",
#    "ingredient":["망고","설탕","메타중아황산나트륨"],
#    "origin":"필리핀"
#    }

#value=a.get("존재하지 않는 키")
#print("값",value)

#di={
#    0:"alpha",
#    1:"beta",
#    3:"delta"
#    }

#for key in di:
#    print(di[key])

#print(range(5),list(range(5)))
#print(range(10),list(range(10)))
#print()

#print(range(0,5),list(range(0,5)))
#print(range(5,10),list(range(5,10)))
#print()

#print(range(0,10,2),list(range(0,10,2)))
#print(range(0,10,3),list(range(0,10,3)))
#print()

#for i in range(10):
#    print(str(i)+"번째 반복입니다.");

#for i in range(5):
#    print(str(i)+"반복변수")
#print()

#for i in range(5,10):
#    print(str(i)+"반복변수")
#print()

#for i in range(0,10,3):
#    print(str(i)+"반복변수")
#print()

#arr=[100,200,300,400,500]

#for i in range(len(arr)):
#    print("index{}:value{}".format(i,arr[i]))

#for i in reversed(range(10)):
#    print("{}번째 반복".format(i))

#i=0
#while i<10:
#    print("{}번째 반복입니다.".format(i))
#    i+=1

#list_a=[1,2,1,2]
#val=2

#while val in list_a:
#    list_a.remove(val)

#print(list_a)


#import time

#out=0
#target_tick=time.time()+5
#while time.time()<target_tick:
#    out+=1
#print(out)

#while True:
#    print("{}번째 반복문입니다.".format(i))
#    i+=1
#    input_s=input("종료?y or Y")
#    if input_s in ['y','Y']:
#        print("반복을 중단합니다.")
#        break

#numbers=[5,15,6,20,7,25]

#for num in numbers:
#    if num<10:
#        continue
#    print(num,end=" ")

#string="hello programming"

#out=string.upper()
#print(out)
#out=string.lower()
#print(out)
#out=string.split(" ")
#print(out)

#list_a=[1,2,3,4]

#list_a.append(1)
#print(list_a)
#list_a.remove(2)
#print(list_a)
#list_a.pop()
#print(list_a)

#test=(
#    "a"
#    "b"
#    "c"
#    )
#print(test)
#print(type(test))

#print("::".join(['1','2','3','4','5']))

#number=int(input("정수입력"))

#if number%2==0:
#    print("\n".join(["입력한 문자열을 {}입니다".format(number),"{}는 짝수입니다.".format(number)]))
#else:
#    print("\n".join(["입력한 문자열을 {}입니다".format(number),"{}는 홀수입니다.".format(number)]))

#a="문자열"
#b={"a":"b",
#   "c":"d"}
#c=range(10)
#d=True

#print("list:{}={}".format(a,list(a)))
#print("list:{}={}".format(b,list(b)))
#print("list:{}={}".format(c,list(c)))
#print("list:{}={}".format(d,list(d)))

#learn def

#def callname(name):
#    print("hello {}".format(name))

#callname("maria")



#def gagup(n):
#    return n*n

#print(gagup(3))



#def tri(a,b):
#    return int(a*b/2)

#print(tri(3,4))

#def oddeven(a):
#    if a%2==0:
#        print("even")
#    else:
#        print("odd")

#oddeven(10)

#def primecom(a):
#    for i in range(2,a):
#        if a%i==0:
#            return 1;

#innum=int(input())
#if primecom(innum)==1:
#    print("com")
#else:
#    print("pri")

#a=input()
#b=input().split()
#c=input()

#print(b.index(c)+1)

#def sum(a):
#    count=0
#    for i in range(1,a+1):
#        count+=i

#    return int(count)

#print(sum(10))


#def fac(a):
#    count=1
#    for i in range(2,a+1):
#        count*=i

#    return int(count)

#print(fac(5))

#def dividenum(a):
#    count=1
#    for i in dividenum(2,a+1):
#        count*=i

#    return int(count)

#print(dividenum(5))

#import time

#input("엔터를 누르고 20초를 셉니다.")
#start=time.time()

#input("20초에 다시 엔터를 누릅니다")
#end=time.time()
#et=end-start

#print("실제시간:",et,"초")
#print("차이",abs(et-20),"초")

#import time
#import random

#n=random.randint(1,100)

#innum=int(input("1~100사이의 숫자를 맞추어보세요!  "))

#while True:
#    if innum==n:
#        print("맞추었습니다!\n")
#        break
#    elif innum>n:
#        innum=int(input("너무 큽니다! 다시 입력해주세요  "))
#    else:
#        innum=int(input("너무 작습니다! 다시 입력해주세요  "))

#import turtle as t
#import time
#import random

#def draw():
#    degree=360
#    for x in range(100):
#        t.bgcolor("red")
#        t.color("blue")
#        t.pencolor("black")
#        t.shape("turtle")
#        t.forward(degree/6)
#        t.left(degree/6)
#        degree-=30

#draw()

#def drawcir(n):
#    t.circle(n)

#for i in range(0,10000,20):
#    drawcir(i)

#t.speed(10)

#def draw(n): 
#    t.bgcolor("red")
#    t.color("blue")
#    t.pencolor("black")
#    t.shape("turtle")
#    t.up()
#    t.right(90)
#    t.forward(10)
#    t.left(90)
#    t.down()
#    t.circle(n)

#for i in range(0,10000,10):
#    draw(i)



#def draw(): 
#    while True:
#        t.setheading(random.randint(1,360))
#        t.forward(10)


#print("test hello world")

#튜플
#a=(10,20,30)
#print(a,type(a))


#list_a=[1,2,3,4,5]

#list_b=list(map(lambda x:x*x,list_a))
#print(list_b)
#list_b=list(filter(lambda x:x<3,list_a))
#print(list_b)


#map(<함수명>,<리스트>)
#filter(<함수명>,<리스트>)

#input_a=input("")

#if input_a.isdigit():
#    num=int(input_a)
#    print("원의 반지름:",num)
#    print("원의 둘레:",2*3.14*num)
#else:
#    print("다시 입력해주세요")


#try:
#    <예외가 발생할수 있는 코드>
#except:
#    <예외 발생시 대처 코드>
#else:
#    <예외가 발생하지 않았을때의 코드>
#finally:
#    <무조건 실행할 코드>


input_a=input()

try:
    num=int(input_a)
except:
    print("다시 입력해주세요")
else:
    print("원의 반지름:",num)
    print("원의 둘레:",2*3.14*num)
finally:
    print("입력값은:",num)




















        


        
























   




































