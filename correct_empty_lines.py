g.es('\n\n\n\n')
g.es('Now:\n')


for p in c.all_positions():
    try:
        # Corrects empty lines around @language python\n@tabwidth -4
        if p.h.startswith('@clean') and p.h.endswith('py'):
            try:
                if '@language python\n@tabwidth -4' in p.b:
                    splited = p.b.partition('@language python\n@tabwidth -4')
                    p.b = ''.join((splited[0].rstrip(), '\n', splited[1], '\n', splited[2].lstrip()))
                    g.es(p.h)

            except Exception:
                g.es_exception()

        # Corrects empty lines between main blocks
        else:
            parent = p.parent()
            if parent.h.startswith('@clean'):
                siblings = [pos.gnx for pos in p.self_and_siblings()]
                # Corrects empty lines between main blocks
                if p.gnx != siblings[-1] or not parent.b.rstrip().endswith('@others'):
                    p.b = '{}\n\n\n'.format(p.b.rstrip())
                # Corrects empty lines at end of file
                else:
                    p.b = '{}\n'.format(p.b.rstrip())
            # Corrects empty lines between methods
            elif parent.h.startswith('class'):
                siblings = [pos.gnx for pos in p.self_and_siblings()]
                # Corrects empty lines between main blocks
                if p.gnx != siblings[-1] or not parent.b.rstrip().endswith('@others'):
                    p.b = '{}\n\n'.format(p.b.rstrip())
                # Corrects empty lines at end of file
                else:
                    p.b = '{}\n'.format(p.b.rstrip())

    except Exception:
        g.es_exception()
