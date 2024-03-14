# f=open("demo.docx","r")
# data= f.read()
# print(data)
# f.close()

hello=open("hello.ppt","w") 
close=hello.write("hello babai")
print(close)

hello=open("hello.ppt","+w")
read=hello.read()
write=hello.write("bagunnva abbai")
print(write)
hello.close() 

write=open("word.ppt","+w")
loud=write.read()
hlo=write.write("hello babai")
print(hlo)

venky =  open("sai.docx", "w+")
venky.write("hello frnds")
venky.close()



