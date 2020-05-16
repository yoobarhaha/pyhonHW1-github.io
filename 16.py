sum=0
count=0
#number=0
while(True):
    inputString=input("데이터를 입력해주세요. 데이터입력 완료시, 끝 이라고 입력해주세요.")
    if (inputString=="끝"):
        break
    else:
         number=int(inputString)
         count+=1
         sum+=number
         print(sum/count)
   

