from __future__ import print_function
import inspect
import sys

program_listing = {}
program_communication = {}

def process_program_listing(top_id, current_id):
    # print('Called with %d' % current_id)
    # Get the current_id communicates listing.
    listing = program_listing[current_id]
    # print('Program id %d talks to %s' % (current_id, listing))

    if top_id not in program_communication.keys():
        program_communication[top_id] = set()

    for pid in listing:
        if pid == current_id or pid == top_id or pid in program_communication[top_id]:
            continue
        # print('Adding %d to talks-to list' % pid)
        program_communication[top_id].add(pid)
        # print('Following %d...' % pid)
        process_program_listing(top_id, pid)


def main():

    data = ''
    for line in sys.stdin:
        data += line

    data = data[:-1]

    for line in data.split('\n'):
        program_id = int(line.split(' <-> ')[0])
        communicates = [int(x) for x in line.split(' <-> ')[1].split(', ')]
        program_listing[program_id] = communicates

    print(program_listing)

    # For a test key, build a list of things that Program ID can talk to.
    for p in program_listing.keys():
        skip = False
        for v in program_communication.values():
            if p in v:
                skip = True
                break
        if skip:
            continue
        program_id = p
        process_program_listing(program_id, program_id)

    print('program_communication %s' % program_communication)
    # Size of the group is how many programs program_id talks to plus itself.
    for p in program_communication:
        print('Program ID %d: %d' % (p, len(program_communication[p]) + 1))
    # print(len(program_communication[program_id]) + 1)
    print('Total number of groups: %d' % len(program_communication.keys()))

if __name__ == '__main__':
    main()
