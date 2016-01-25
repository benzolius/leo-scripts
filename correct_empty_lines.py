print('\n\n\n\n')
print('Now:\n')


for p in c.all_positions():
    try:
        # Corrects empty lines around @language python\n@tabwidth -4
        if p.h.startswith('@clean') and p.h.endswith('py'):
            # Corrects empty lines after @first
            if p.h == '@clean manage.py':
                splited = p.b.partition('"""\nMain starter script for Django\n"""')
                p.b = ''.join((splited[0].rstrip(), '\n', splited[1], splited[2]))

            try:
                if '@language python\n@tabwidth -4' in p.b:
                    splited = p.b.partition('@language python\n@tabwidth -4')
                    p.b = ''.join((splited[0].rstrip(), '\n', splited[1], '\n', splited[2].lstrip()))
                    print(p.h)

            except Exception as exc:
                print('---------------------------- Exception: -------------------- {}'.format(exc))

        # Corrects empty lines between main blocks
        else:
            parent = p.parent().h
            if parent.startswith('@clean'):
                siblings = [pos.gnx for pos in p.self_and_siblings()]
                # Corrects empty lines between main blocks
                if p.gnx != siblings[-1]:
                    p.b = '{}\n\n\n'.format(p.b.rstrip())
                # Corrects empty lines at end of file
                else:
                    p.b = '{}\n'.format(p.b.rstrip())
            # Corrects empty lines between methods
            elif parent.startswith('class'):
                siblings = [pos.gnx for pos in p.self_and_siblings()]
                # Corrects empty lines between main blocks
                if p.gnx != siblings[-1]:
                    p.b = '{}\n\n'.format(p.b.rstrip())
                # Corrects empty lines at end of file
                else:
                    p.b = '{}\n'.format(p.b.rstrip())

    except Exception as exc:
        print('---------------------------- Exception: -------------------- {}'.format(exc))