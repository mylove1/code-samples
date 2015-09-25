# -*- coding: utf-8 -*-

import csv

csvfile_path = 'estate_corpus_20150409.csv'


def test_csvfile():
    with open(csvfile_path, 'rb') as csvfile:
        reader = csv.reader(csvfile)

        table_head = reader.next()
        print('table_head: ', table_head)

        table_row = reader.next()

        print('table_row: ', table_row)


if __name__ == '__main__':
    #export_all_content()
    test_csvfile()
