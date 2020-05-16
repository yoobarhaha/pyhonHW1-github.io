diction={".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E",
"..-.":"F","--.":"G","....":"H","..":"I",".---":"J","-.-":"K",".-..":"L",
"--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R",
"...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X",
"-.--":"Y","--..":"Z", "  ": " "}
string=input("모스부호를 입력하세요.")
codleList=string.split(" ")
output=""
print(codleList)
for i in codleList:
    for a in diction.keys():
        if(i==a):
            i=diction.get(a)
            output+=i
            
print(output)