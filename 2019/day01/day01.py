import sys

import module

spacecraft_modules = []
for uid, line in enumerate(sys.stdin.readlines()):
    spacecraft_modules.append(module.Module(uid, int(line)))

print(spacecraft_modules)

print('Processed {} modules'.format(len(spacecraft_modules)))

print('Sum of fuel requirements, part 1: {}'
      .format(sum(x.fuel[0] for x in spacecraft_modules)))
print('Sum of fuel requirements, part 2: {}'
      .format(sum(x.fuel[1] for x in spacecraft_modules)))
