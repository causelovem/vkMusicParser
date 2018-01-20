import pyperclip as clip
import codecs

# f = open("pars", "r")
f = codecs.open("pars", "r", "utf_8_sig")

featList = ["ft", "ft.", "feat", "feat."]
file = []
music = {}
for line in f:
    group = f.readline()
    group = group.split('\n')[0].lower()
    # group = group.split('\r\n')[0].lower()

    for feat in featList:
        gr = group.split(feat)
        if (len(gr[0]) != len(group)):
            group = gr[0][:-1]
            break

    group = group.replace('\r', '')
    music[group] = []
    file.append(group)
    file.append(f.readline().split('\n')[0].replace('\r', ''))
    f.readline()

f.close()

for i in range(0, len(file), 2):
    music[file[i]].append(file[i + 1])

# res = open("clast", "w")
res = codecs.open("clast", "w", "utf_8_sig")

for elem in music:
    res.write(elem + " " + str(len(music[elem])) + "\r\n")
    for i in range(len(music[elem])):
        res.write(elem + " - " + music[elem][i] + "\r\n")
    res.write("\n\n")

res.close()

for elem in music:
    print(elem + " " + str(len(music[elem])) + "\r\n")
    command = input()

    if command == "next":
        print("!NEXT!\r\n\r\n")
        continue

    for i in range(len(music[elem])):
        song = elem + " - " + music[elem][i]
        print(str(i + 1) + " " + song)
        clip.copy(song)
        command = input()
        if command == "next":
            break

    print("!NEXT!\r\n\r\n")

print("DONE!")
