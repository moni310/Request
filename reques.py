import requests
import json
api = requests.get("http://saral.navgurukul.org/api/courses")
s=json.loads(api.text)
with open("user.json","w") as f:
    m=json.dump(s,f,indent=4)
store=s["availableCourses"]
# print(store)
id=[]
name=[]
i=0
while i<len(store):
    print(i+1,store[i]["name"],end=" ")
    print(store[i]["id"])
    id.append(store[i]["id"])
    name.append(store[i]["name"])
    i=i+1

print( )

user=int(input("enter the number whichone data do you want="))
user1=id[user]
user2=name[user]
print(user2,end=" ")
print(user1)
u=id[user]
api1= requests.get("http://saral.navgurukul.org/api/courses/"+u+"/exercises")
data1=json.loads(api1.text)
# print(data1)
with open("userdata.json","w") as file1:
    f=json.dump(data1,file1,indent=4)
store1=data1["data"]
# print(store1)
print( )

l=0
while l<len(store1):
    print(l+1,store1[l]["name"])
    p=store1[l]["childExercises"]
    if p==[]:
        print("  ","[]")
    else:
        h=0
        while h<len(p):
            print("   ",h+1,p[h]["name"])
            h=h+1
    l=l+1
print( )

user2=int(input("enter the parent id--"))

print()
print(store1[user2]["name"])

if store1[user2]["childExercises"]==[]:
    print("  ",store1[user2]["slug"])


    api2=requests.get("http://saral.navgurukul.org/api/courses/"+str(user2)+"/exercise/getBySlug?slug="+store1[user2]["slug"])
    data3=json.loads(api2.text)
    # print(data3)
    print()
    # print(data3["content"])
    with open("thirdapi.json","w") as f2:
        f4=json.dump(data3,f2,indent=4)
    print( )
else:
    print( ) 
    h=0
    while h<len(store1[user2]["childExercises"]):
        print(h+1,store1[user2]["childExercises"][h]["name"])
        h=h+1
    user3=int(input("entr the child id----"))
    ap=requests.get("http://saral.navgurukul.org/api/courses/"+str(user3)+"/exercise/getBySlug?slug=requests__using-json")
    k=ap.text
    for h1 in k:
        print(h1,end="")


var1=int(input("show your slug---"))
var2=requests.get("http://saral.navgurukul.org/api/courses/"+str(user2)+"/exercise/getBySlug?slug="+store1[user2-1]["slug"])
d=var2.json()
print(d["content"])
ques=input("enter the option next,previous-----")
x=var2
print("**************")
if ques=="next":
    req=requests.get("http://saral.navgurukul.org/api/courses/"+str(user2)+"/exercise/getBySlug?slug="+store1[user2-1]["slug"])
    r1=req.json()
    print("content",r1["content"])
    # print(x)
elif ques=="previous":
    l=0
    while l<len(store1):
        print(l+1,store1[l]["name"])
        p=store1[l]["childExercises"]
        if p==[]:
            print("  ","[]")
        else:
            h=0
            while h<len(p):
                print("   ",h+1,p[h]["name"])
                h=h+1
        l=l+1
else:
    pass