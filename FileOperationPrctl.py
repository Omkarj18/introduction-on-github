###Q.how to open & close file in python?

filevar=open("E:/omkar credence notes/readme.txt")
filecont=filevar.read()
print('read content of file:',filecont)
filevar.close()


###=================================================================================

# Q.Write a open file program by using try except finally?
# path="E:\\omkar credence notes\\readme1111.txt"
# try:
#     filepath=open(path)
#     content=filepath.read()
#     print('read file:',content)

# except FileNotFoundError as e:
#     print(f"File not found : {filePath}", e)
# except Exception as e:
#     print("Something went wrong...", e)

# finally:
#     try:
#         filepath.close()        # Closing file
#     except:
#         print("File never been opened")