# *
# **
# ***
# ****

# # الاسطر
# for i in (1,2,3,4):
#     # محتوى كل سطر
#     for n in range(4,i):
#         print("*",end="")
#     print("\n")

##################################

#    *
#   **
#  ***
# ****

# # الاسطر
# for i in (4,3,2,1):
#     # محتوى كل سطر
#     for n in range(0,i):
#         print("",end=" ")
#     for n in range(0, abs(i-5)):
#         print("*",end="")
#     print("\n")

#################################

#    *
#   ***
#  *****
# *******

# # الاسطر
# for i in (4,3,2,1):
#     # محتوى كل سطر
#     for n in range(0,i):
#         print("",end=" ")
#     for n in range(0, abs(i-5)):
#         print("*",end="")
#     for n in range(0, abs(i-5)-1):
#         print("*",end="")
#     print("\n")

#################################

#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

# واجب قع جهران

print("   *")
print("  ***")
print(" *****")
print("*******")
print(" *****")
print("  ***")
print("   *")