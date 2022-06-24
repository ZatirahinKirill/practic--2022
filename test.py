word=input()
output1 = []
for char in word:
    number = ord(char) - 97
    output1.append(number)

output2 = []
count=output1[0]
if (count<5):
    output2.append(26-(5-count))
else:
    output2.append(count-5)
    
for num in output1[1:]:
    while (num <count):
        num=num+26
    output2.append(num-count)
    count=num

new_word =[]    
for num in output2:
    char = chr(num + 97)
    new_word.append(char)
print ("".join(new_word))
