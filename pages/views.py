from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    menu = ['닭갈비', '탕수육', '초밥', '스파게티돈까스']
    pick = random.choice(menu)
    return render(request,'hello.html', {'pick':pick})

def name(request):
    my_name = '김슬기'
    return render(request, 'name.html', {'my_name':my_name})

def introduce(request):
    my_info = ['김슬기', '100']
    name = '김슬기'
    age = 100
    context = {
        'name' : name,
        'age' : age,
    }
    return render(request, 'introduce.html', context)

def classroom(request):
    # 1. 리스트에 반 학생 5명 작성
    # 2. 해당 리스트에서 무작위 한명 선택
    # 3. 그 학생 이름 출력하는 페이지 작성
    student = ['이준성', '유명인', '박누리', '신승환', '강인선']
    pick = random.choice(student)
    context = {
        'pick' : pick
    }
    return render(request, 'classroom.html',context)

def yourname(request, name):
    # name = name
    context = {
        'name' : name
    }
    return render(request, 'yourname.html', context)

def yourinfo(request, name, age):
    # Q1. 이름과 나이 받아보기
    # 1. url 경로에 이름과 나이(반드시 int)입력
    # 1-1. urls.py에 경로 설정 시
    # <> 꺽쇠 형태로 구분하여 표현
    # 2. 입력 받은 내용을 페이지에 출력
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'yourinfo.html',
    context)

def times(request, num1, num2):
    num3 = num1 * num2
    context = {
        'num1' : num1,
        'num2' : num2,
        'num3' : num3,
    }
    return render(request, 'times.html',context)

def pigeon(request, big, small):
    result = []
    if big < small :
        big, small = small, big
    for num in range(1, small+1):
        result.append(big*num)
    context = {
        'result': result
    }
    return render(request, 'pigeon.html', context)

def dtl(request):
    my_list = ['짜장면', '차돌짬뽕', '탕수육', '콩국수']
    empty_list = []
    my_string = "Life is short, You need Python"
    today = datetime.now()
    context = {
        'my_list' : my_list,
        'empty_list' : empty_list,
        'my_string' : my_string,
        'today' : today
    }
    return render(request, 'dtl.html', context)

def forif(request):
    a = request.GET.get('a')
    my_list = [100, 50, 30, 20, 10]
    my_string = '간단한 문자열'
    data_a = '첫번째 데이터'
    data_b = '두번째 데이터'
    data_a, data_b = data_b, data_a
    context = {
        'my_list' : my_list,
        'my_string' : my_string,
        'data_a' : data_a,
        'data_b' : data_b
    }
    return render(request, 'forif.html', context)

def presentation(request):
    students = ['강인선','곽혜란','김민정','김서연','김성현','김현수','김현정','문준우','박누리','백승재','성민재','신승환','심재민','오성식','유명인','유환우','윤소윤','이영주','이정윤','이준성']
    random.shuffle(students)
    context = {
        'students' : students
    }
    return render(request, 'presentaion.html', context)