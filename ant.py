import os,time
for i in range(100):
    if i%2==0:
        print(" "*i+"\  /")
        print(" "*i+"OOOO")
        print(" "*i+"/  \\")
        time.sleep(1)
        os.system("clear")
    else:
        print(" "*i+" \  /")
        print(" "*i+"OOOO")
        print(" "*i+" /  \\")
        time.sleep(1)
        os.system("clear")