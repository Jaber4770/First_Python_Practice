# ---------------------
# frequency checking
text = "banana"
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
        
print(freq)


for k,v in freq.items():
    print(k,v)
    

#---------------------
#loop with set:
for x in {3, 1, 2}:
    print(x)
