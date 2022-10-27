# Question no 2

my_str = input("Enter the word to be arranged:\n")

strs = [word.lower() for word in my_str]

l = len(strs)
for i in range(0,l):
    for j in range(0,l):
        if strs[i] < strs[j]:
            strs[i],strs[j] = strs[j],strs[i]

result = ""

for i in range(0,l):
    result+=strs[i]

print(result)