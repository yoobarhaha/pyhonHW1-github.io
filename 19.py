inputString=input("문자를 입력해주세요.")
a=list(inputString)
output=[]
count=0
num=0
output.append(a[1])
for i in a:
    if (output[num]==i):
        count+=1
    else:
        output.append(count)
        output.append(i)
        count=1
        num+=2
output.append(count)
string=""
for i in output:
    string+=str(i)
print(string)


