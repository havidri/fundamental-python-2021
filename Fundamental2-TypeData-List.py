# Type data List/Array

child = ['Two', 'One', 'Three', 'Four']

print(child)
child.append('Six')
print(child)
print('_'*10)

print('Greeting second child')
print(f'Hallo {child[1]}\n')
print('_'*10)

print('Greeting all child')
for c in child:
    print(f'Hai {c}!')

print('_'*10)
print('Greeting all child')
for c in range(0, len(child)):
    print(f'Hai {child[c]}!')