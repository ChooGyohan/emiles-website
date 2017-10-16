
import sys
sys.path.append("D:/cnrygks/Sogang University/2017_4학기 ()/일반교양_기초응용소프트웨어프로그래밍/Emilles_Website_Project/Input")
sys.path.append("D:/cnrygks/Sogang University/2017_4학기 ()/일반교양_기초응용소프트웨어프로그래밍/Emilles_Website_Project/Output")
sys.path.append("D:/cnrygks/Sogang University/2017_4학기 ()/일반교양_기초응용소프트웨어프로그래밍/Emilles_Website_Project/Process")

import Input
import Output
import Process

print(sys.path)
print(dir(Input))
print(dir(Output))
Username : input("아이디를 입력하시오 : ")
Username = Input()
Username = Output()
Username = Process()
Username.login()
