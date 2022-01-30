e2f = {'dog' : 'chien', 'cat' : 'chat', 'walrus' : 'morse'}
e2f['walrus']
f2e = {}
for english, french in e2f.items():
    f2e[french] = english
set(e2f.keys())
