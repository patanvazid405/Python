#strings

str1="hello ";
str2="vazid bhai !";
final_len=str1+str2;

#str length
print(len(str1));
print(len(final_len));
#
# if (hlo>=18):
#     print("you can vote");
# else:
#     print("you cant vote ");

#indexing

name="vazid patan";
print(name[3])#i
print(name[0 :8]);#slice
print(name[:10]);
print(name[2:]);

#string functions

my_Job="hello I'm code from mgr university";

print(my_Job.capitalize());#captalize
print(my_Job);
print(my_Job.endswith("ty"));#true
print(my_Job.find("y"));#finds inex of string
print(my_Job.replace("code","vazid"));
print(my_Job.count("o"));

#practise
#wap to input user'name& print its length

user=input("enter your name bro ! :  ");

print("length of your name is : ",len(user));

 #wap to print @ in this string

msg="@hello babai how @re you nice t@ see You";
print( msg.count("@"));


# #condtional statements

# #eligliblity for vote 

age=21;

if(age>=18):
    print("you  can vote bro !");
elif(age>=60):
    print("you are old but you can vote Thata");
else:
    print("you can't vote child");

#mark of student

marks=int(input("enter your marks: "));

if(marks>=90):
    print("you got 'A' grade bro!");

elif(marks<90) and (marks>=80):
     print("you got 'B' grade bro!");
else:
     print("you failed bro!");

print("this is your marks",marks);

#practise
#wap wether your number is even or odd

number=int(input("enter your number here : "))

if(number%2==0):
    print("this is an even number");
else:
    print("this is an odd number");

a=int(input("enter your first number here : "));
b=int(input("enter your second number here : "));
c=int(input("enter your third number here : "));
d=int(input("enter your fourth number here : "));

if(a>=b and a>=c):
    print("first number is big",a);
elif(b>=c and b>=c):
      print("second number is big",b);
elif (d>=c):
      print("third number is big",c);


     






















