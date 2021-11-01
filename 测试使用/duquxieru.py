#
# #
# import os
# file =open("D:\insert_id - 副本.txt","r")
# lines = []
# for i in file:
#     lines.append(i)
#     i.replace("\n", ",")
# file.close()
# new = []
# p = 0
# for line in lines:
#     if p == 10:
#         new.append(line)
#     else:
#         new.append(line)
#     p = p+1
# print(lines)
# print(new)

# fiil_write_obj = open("D:\insert_id - 副本.txt","w")
# count = 0
# for var in new:
#     if count <10:
#         var.replace("\n",",")
#         fiil_write_obj.writelines(var)
#     else:
#         fiil_write_obj.writelines(var)
#         fiil_write_obj.writelines("\n")
#         count =0
#     count += 1
#
# fiil_write_obj.close()

import find
# 删除 null
lines = [l for l in open("D:\insert_id - 副本.txt","r") if l.find("null",0,8) !=0]
fd = open("D:\insert_id - 副本.txt","w")
fd.writelines(lines)
fd.close()


# 排列成10个数据一行
path = "D:\insert_id - 副本.txt"
with open(path) as f1:
    cnames = f1.readlines()
    for i in range(0,len(cnames)):
        cnames[i] = cnames[i].replace("\n", ",")
        if i %10 == 0 and i!= 0:
            cnames[i] = cnames[i].strip() + "\n"
with open(path,"w") as f2:
    f2.writelines(cnames)
