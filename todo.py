

import sys
from datetime import datetime
dt=datetime.today().strftime('%Y-%m-%d')
try:
    sys.argv[1]
except IndexError:
    st = ""
else:
    st = sys.argv[1]

def helP():
    
    print("""Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics""")
    

    

def add(data):
    with open("todo.txt","a") as f:
        f.writelines(data+"\n")
    print("Added todo: \"{}\"".format(data))
    

def deL(number):
    l=[]
    with open("todo.txt",'r') as f:
        for x in f:
            l.append(x)
    if number>len(l) or number<=0:
        print("Error: todo #{} does not exist. Nothing deleted.".format(number))
    else:
        with open("todo.txt", "w") as f:
            for line in l:
                if l[int(number)-1]!=line:
                    f.write(line)
        print("Deleted todo #{}".format(number))    

def ls():
    l=[]
    try:
        with open("todo.txt",'r') as f:
            for x in f:
                l.append(x)
            for e in range(len(l)-1,-1,-1):
                print("["+str(e+1)+"] "+l[e])
                # print("[{}] {}".format(e+1,l[e]))
    except:
        print("There are no pending todos!")

def done(number):
    l=[]
    with open("todo.txt",'r') as f:
        for x in f:
            l.append(x)
    if number>len(l) or number<=0:
        print("Error: todo #{} does not exist.".format(number))
    else:
        with open("todo.txt", "w") as f:
            for line in l:
                if l[int(number)-1]!=line:
                    f.write(line)
        with open("done.txt","a") as f:
            f.write("x "+dt+" "+l[number-1]) 
            print("Marked todo #{} as done.".format(number))
    
    


def report():
    l=[]
    m=[]
    with open("todo.txt",'r') as f:
        for x in f:
            l.append(x)
    with open("done.txt",'r') as f:
        for x in f:
            m.append(x)
    print(dt+" Pending : {} Completed : {}".format(len(l),len(m)))

if(st=="help" or st==""):
    helP()
if(st=="add"):
    try:
        add(sys.argv[2])
    except IndexError:
        print("Error: Missing todo string. Nothing added!")

if(st=="ls"):
    
    ls()
    

if(st=="del"):
    try:
        deL(int(sys.argv[2]))
    except IndexError:
        print("Error: Missing NUMBER for deleting todo.")
    else:
        print("Error: todo #{} does not exist. Nothing deleted.".format(sys.argv[2]))

if(st=="done"):
    try:
        done(int(sys.argv[2]))
    except IndexError:
        print("Error: Missing NUMBER for marking todo as done.")
    else:
        print("Error: todo #{} does not exist. Nothing Mark.".format(sys.argv[2]))
if(st=="report"):
    report()




