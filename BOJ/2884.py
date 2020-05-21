h, m = input().split()
h, m = int(h), int(m)

mm = m-45

if mm<0 :
    m = 60+mm
    h = (h-1)%24
    print("{} {}".format(h, m))
else : 
    print("{} {}".format(h, mm))