# 백준, 2941번 크로아티아 알파벳

word = input()

alpha = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
            
for c_a in alpha :
    if c_a in word :
        word = word.replace(c_a, "A")

print(len(word))