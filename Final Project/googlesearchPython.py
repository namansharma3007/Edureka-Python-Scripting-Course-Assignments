from googlesearch import search

query = input("Enter the topic you wish to search: ")

for i in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(i)