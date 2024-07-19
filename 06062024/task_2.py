from concurrent.futures import ThreadPoolExecutor

import psycopg2
import psycopg2.extras

from generic_setup import get_cursor, get_locks

sql_1 = '''
BEGIN;
UPDATE my_table
SET v='a' WHERE id=1;
'''

sql_2 = '''
BEGIN;
UPDATE my_table SET v='b' WHERE id=1;  
'''


with \
        ThreadPoolExecutor(max_workers=2) as executor, \
        get_cursor(application_name='block_or_not_1') as cur_1, \
        get_cursor(application_name='block_or_not_2') as cur_2:

    locks_future = executor.submit(get_locks, ('block_or_not_1', 'block_or_not_2'))
    cur_1.execute('SET statement_timeout = 5000;')
    cur_2.execute('SET statement_timeout = 5000;')


    print('Running...\n')
    try:
        print('Connection 1:', sql_1)
        cur_1.execute(sql_1)


        print('Connection 2:', sql_2)
        cur_2.execute(sql_2)

    except psycopg2.errors.QueryCanceled:
        print("\033[91m\033[1mBLOCK")
    else:
        print("\033[92m\033[1mNO BLOCK - Move onto the next task :)")
