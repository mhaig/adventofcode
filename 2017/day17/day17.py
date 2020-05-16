import sys

def get_input():
    """Get input from stdin and return as a string."""
    # TODO move into something common so I can pull this out of all these
    # scripts.
    data = ''
    for line in sys.stdin:
        data += line

    data = data[:-1]

    return data

def main():

    step_size = int(get_input())
    print(step_size)

    circular_buffer = [0]
    current_position = 0

    for i in xrange(1, 2018):
        current_position += step_size
        current_position = current_position % len(circular_buffer)
        circular_buffer.insert(current_position + 1, i)
        current_position = current_position + 1

    index = circular_buffer.index(2017)
    print(circular_buffer[index + 1])

if __name__ == '__main__':
    main()