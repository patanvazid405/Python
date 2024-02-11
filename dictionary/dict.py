student={
    "name": "vazid",
    "age":21,
    "clg":"mgr university",
    "cgpa": 8.5,
    "gender":True,
}


student["cgpa"]=9.0
student["location"]="Nellore"
print(student)

#creating null ditocnary

null_dict={}
null_dict["job"]="devloper";
print(null_dict)

#nested Dictonary
st={
    "name": "vazid",
    "age":21,
    "clg":"mgr university",
    "subjects":{
          "dbms":56,
          "dsa":89,
          "os":85,
    },
    "cgpa": 8.5,
    "gender":True,
}
print(st["subjects"] ["os"])

#methods
print(st.keys())
print(st.values())
print(list(st.items()))
print(st.get("cgpa"))
st.update({"new_dict" :"dictionary"})
print(st)

#sets
collection=set()

collection.add(1)#adds item
collection.add(2)
collection.remove(1)
#collection.clear()#clers
print(len(collection))

set1={1,2,3,4,6}
set2={2,3,5,6}

sot=set1.union(set2);
print(sot)
intersec=set1.intersection(set2)
print(intersec)

#practise

things={

}

things["table"]="A peice of furniture"
things["cat"]="a small animal"
print(things)
#2
clas={"python","java","C++","javaScript","java","python","C++","C"}
print(len(clas));

mark={}


x=int(input("Enter YOur EEe Maks:" ))
mark.update({"your mark":x})
print(mark)




