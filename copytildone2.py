while True:
    line = input('> ')
    if line.startswith('#'):
        continue
    if line == 'done':
        break
    print(line)
print('Done!')
