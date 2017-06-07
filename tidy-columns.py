#!/usr/bin/env python

from __future__ import print_function

import sys
import argparse
import locale

locale.setlocale(locale.LC_ALL, '')

parser = argparse.ArgumentParser(
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description='Align columns of data read from standard input.')

parser.add_argument(
    '--addCommas', default=False, action='store_true',
    help='If True, insert commas into numeric (integer) column values.')

parser.add_argument(
    '--defaultAlignment', default='L', choices=('L', 'R'),
    help='The default column alignment, either L or R.')

parser.add_argument(
    '--alignment', help='Per-column alignment, either L or R for each column.')

parser.add_argument(
    '--separator', default=' ', help='The string to print between columns.')

args = parser.parse_args()

maxWidths = []
values = []
addCommas = args.addCommas

for line in sys.stdin:
    fields = line.split()
    nFields = len(fields)

    if nFields > len(maxWidths):
        maxWidths.extend([0] * (nFields - len(maxWidths)))

    for i, field in enumerate(fields):
        if addCommas:
            try:
                # Insert locale-specific commas into integers.
                fields[i] = field = locale.format('%d', int(field),
                                                  grouping=True)
            except ValueError:
                pass

        if len(field) > maxWidths[i]:
            maxWidths[i] = len(field)

    values.append(fields)

nCols = len(maxWidths)

alignment = [args.defaultAlignment.replace('L', '-').replace('R', '')] * nCols

if args.alignment:
    for i, thisAlignment in enumerate(args.alignment[:nCols].upper()):
        alignment[i] = thisAlignment.replace('L', '-').replace('R', '')

format_ = args.separator.join(
    ['%%%s%ds' % (align, width) for (align, width) in
     zip(alignment, maxWidths)])

for fields in values:
    if len(fields) < nCols:
        fields.extend([''] * (nCols - len(fields)))
    print(format_ % tuple(fields))
