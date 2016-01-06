print('\n\n\n\n')


amount = 0

for p in c.all_positions():
    if p.h.startswith('@path migrations'):
        amount += 1
        print(p.h)
        c.selectPosition(p)
        c.deleteOutline()


for p in c.all_positions():
    if p.h.startswith('@path .ropeproject'):
        amount += 1
        print(p.h)
        c.selectPosition(p)
        c.deleteOutline()


if not amount:
    print('There is no deleted path')
