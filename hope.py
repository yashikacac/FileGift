import webbrowser, os, time, sys
os.system('cls')
f1= open("abc.txt","w+")
f2= open("file.txt","w+")
f1.write("Hello")
f2.write("Hope you are enjoying your day!\r\n")
#f2.write("A small gift that i have tried.")
f1.close()
f2.close()
filenames = ["abc.txt", "file.txt"]
frames = []

for name in filenames:
    with open(name,"r",encoding="utf8") as f:
        frames.append(f.readlines())

for frame in frames:
    print("".join(frame))
    time.sleep(3)
    os.system('cls')

lines = ["LoremIpsum, LoremIpsum.",
         "LoremIpsum", "LoremIpsum",
         "LoremIpsum", "LoremIpsum,","LoremIpsum.",
         "LoremIpsum"]

for line in lines:    
    for c in line:
        print(c.upper(), end='')
        sys.stdout.flush()
        time.sleep(0.1)
    print('')  
