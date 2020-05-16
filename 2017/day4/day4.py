import sys

data = ''
for line in sys.stdin:
    data += line

data = data[:-1]

print(len(data.split('\n')))

invalid_line = 0
for line in data.split('\n'):
    words = line.split()

    for i in range(len(words)):
        word = words[i]
        print(list(word))
        word = list(word)
        word.sort()
        print(''.join(word))
        words[i] = ''.join(word)

    count = 0
    for word1 in words:
        for word2 in words:
            if word1 == word2:
                count += 1

    if count != len(line.split()):
        invalid_line += 1

    print('words: %d matches: %d' % (len(line.split()), count))

print(len(data.split('\n')) - invalid_line)
