import sys

data = ''
for line in sys.stdin:
    data += line

# Remove the trailing newline
data = data[:-1]

sum = 0
current_digit = 0
next_digit = 0
# Part 1 step size
step_size = 1
# Part 2 step size
# step_size = len(data) / 2

print(len(data))
print(step_size)
for i in range(len(data)):
    current_digit = data[i]
    next_digit = data[(i+step_size) % len(data)]

    if current_digit == next_digit:
        sum += int(current_digit)

print(sum)
