from binarytreesort import binarytreesort
from bubblesort import bubblesort
from bucketsort import bucketsort
from combsort import combsort
from gnomesort import gnomesort
from heapsort import heapsort
from inplacemergesort import inplacemergesort
from insertionsort import insertionsort
from introsort import introsort
from librarysort import librarysort
from mergesort import mergesort
from oddevensort import oddevensort
from patiencesort import patiencesort
from pigeonholesort import pigeonholesort
from quicksort import quicksort
from selectionsort import selectionsort
from shakersort import shakersort
from shellsort import shellsort
from smoothsort import smoothsort
from strandsort import strandsort
import time
import global_value as g
import pandas as pd

def do_it(sort: list[int], f):
    start = time.time()
    num = f(sort)
    end = time.time()
    return (start, num, end)

if __name__ == '__main__':
    text = input('which data: ')
    if (text == '234'):
        df = pd.read_csv('234.csv', usecols=['2022 Population'])
        df = df.fillna(0)
        sort = df['2022 Population'].to_list()
    elif (text == '918'):
        df = pd.read_csv('918.csv', usecols=['World Sales (in $)'])
        df = df.fillna(0)
        sort = df['World Sales (in $)'].to_list()
    elif (text == '5012'):
        df = pd.read_csv('5012.csv', usecols=['workers'])
        df = df.fillna(0)
        sort = df['workers'].to_list()
    start, num, end = do_it(sort.copy(), bubblesort)
    print('bubblesort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), oddevensort)
    print('oddevensort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), shakersort)
    print('shakersort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), combsort)
    print('combsort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), gnomesort)
    print('gnomesort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), selectionsort)
    print('selectionsort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), insertionsort)
    print('insertionsort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), shellsort)
    print('shellsort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), binarytreesort)
    print('binarytreesort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), librarysort)
    print('librarysort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), mergesort)
    print('mergesort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), inplacemergesort)
    print('inplacemergesort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), heapsort)
    print('heapsort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), smoothsort)
    print('smoothsort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), quicksort)
    print('quicksort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), introsort)
    print('introsort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), patiencesort)
    print('patiencesort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), strandsort)
    print('strandsort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), pigeonholesort)
    print('pigeonholesort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')
    g.swap = 0
    g.cmp = 0
    start, num, end = do_it(sort.copy(), bucketsort)
    print('bucketsort & {:.2e} & '.format(end - start), end='')
    print(f'{g.swap} & {g.cmp}')