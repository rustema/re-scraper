import pandas as pd
import sys

if len(sys.argv) < 2:
    print('please specify date')

date = sys.argv[1]

cities = ['los-altos',
          'santa-clara',
          'palo-alto',
          'mountain-view',
          'sunnyvale',
          'campbell',
          'north-san-jose',
          'west-valley',
          'central-san-jose']
o = None
for x in cities:
    path = x + '/all-%s.csv' % date
    print(path)
    p = pd.read_csv(path)
    if o is None:
        o = p
    else:
        o = o.append(p)

o.to_csv('result-%s.csv' % date, index=False)
