import os
"""
The goal of this would be to read from 1 file 
break it up into multiple files.
"""




curr_path = os.getcwd()
print(f"Current directory is - {curr_path}")


target = curr_path+"/target/input.txt"
print(f"Target is: {target}")


my_file = open(target,"r")


#Write algo
count = 1
current_text = my_file.readline()
current_f_name = f"file_{count}"
target_output = curr_path+"/targetOne/"

while len(current_text)>2:
    #write portion
    target_file = open(target_output+current_f_name+".txt","w")
    target_file.write(current_text)
    target_file.close()
    #obtain name and text for output file and iterate
    count += 1
    current_text = my_file.readline()
    current_f_name = f"file_{count}"
    





my_file.close()

print('*'*10+"break"+"*"*10+"\n")
print("completed one to many")