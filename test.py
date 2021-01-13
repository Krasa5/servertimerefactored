# import urllib.request

# url = "http://www.mieliestronk.com/corncob_lowercase.txt"
# file = urllib.request.urlopen(url)

# for line in file:
#     decoded_line = line.decode("utf-8")
#     print(decoded_line)

list1 = ["a", "b", "c", "d", "e", "f", "o", "g"]
word = "Google"
number = 0

matching = [s for s in list1 if s in word]
print(matching)
print(len(matching))
