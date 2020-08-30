#PF-Assgn-36
def create_largest_number(number_list):
    list1=[]
    for i in number_list:
        n=i%10
        list1.append(n)
        n=i//10
        list1.append(n)
    list1.sort(reverse=True)
    res=""
    for i in list1:
        res+=str(i)
    return int(res)

number_list=[21,19,61]
#You can also create the list dynamically
largest_number=create_largest_number(number_list)
print(largest_number)
