
# 1. Write a Python program to read an entire text file.

# with open(file ="myinfo.txt",mode= "r") as f:
   # data= f.read()
   
# print(data)

# 2. Write a Python program to read first n lines of a file.

# n = int(input("Enter number of lines to read: "))

# with open (file= "myinfo.txt",mode= "r") as f:
    # for i in range(n):
        # line = f.readline()
        # if not line:  
            # break
        # print(line.strip())
        
# 4. Write a Python program to read last n lines of a file.     

# n = int(input("Enter number of lines to read from end: "))

# with open(file = "myinfo.txt", mode = "r") as file:
    # lines = file.readlines()

# for last n line
# for i in lines[-n:]:
    # print(i.strip())
    
# 5. Write a Python program to read a file line by line and store it into a list.

# l_list = []
# with open(file = "myinfo.txt", mode= "r") as f:
    # for i in f:
        # l_list.append(i.strip())
        
        # print(l_list)
        
 # 6. Write a Python program to read a file line by line store it into a variable.     
# var = " "
# with open("myinfo.txt", "r") as f:
    # for i in f:
        # var += i
        
        # print(var)
# with open (file = "myinfo.txt" ,mode= "r") as f:
    # var = f.read()
    
    # print(var)
    
    

# 8. Write a python program to find the longest words and store into new file.
# with open(file ="myinfo.txt", mode = "r") as f:
    # words = f.read().split()

# longest = max(words, key=len)

# print(longest)


# 9. Write a Python program to count the number of lines in a text file and store into new file.
# with open("myinfo.txt", "r") as f:
    # data = f.read()
    # count = len(data.splitlines())

# print("Total lines:", count)
# print(data)




#2nd assignment

# 1. Write a Python program to copy the contents of a file to another file . 

# with open(file ="myinfo.txt", mode= "r") as f1:
    # data = f1.read()

# with open(file= "myinfo1.txt",mode= "w") as f2:
    # f2.write(data)
    
# print(data)

 
# 2. Write a Python program to remove newline characters from a file. 
# with open("myinfo.txt", "r") as f:
    # data = f.read().replace("\n", "")

# with open("myinfo1.txt", "w") as f:
    # f.write(data)

# print(data)

# 3. Write a Python program to extract characters from various text files and puts them into a list. 
# char_list = []
# with open("myinfo.txt", "r") as f1, open("myinfo1.txt", "r") as f2:
    # char_list = list(f1.read() + f2.read())

# print(char_list)

# 4. Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt. 

# for i in range(65, 91):  
    # ch = chr(i)

    # with open(ch + ".txt", "w") as f:
        # f.write("This is file " + ch)
 
# 5. Write a Python program to create a file where all letters of English alphabet are listed by 
# specified number of letters on each line. 


n = int(input("Enter letters per line: "))

alphabets = "abcdefghijklmnopqrstuvwxyz"

with open("myinfo.txt", "w") as f:
    count = 0
    
    for ch in alphabets:
        f.write(ch)
        count += 1
        
        if count == n:
            f.write("\n")
            count = 0