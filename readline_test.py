# f=open("C:/doit/새파일3.txt", 'r')
# line = f.readline()
# print(line)
# f.close()

#readline_all.py
f=open("C:/doit/새파일3.txt",'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()