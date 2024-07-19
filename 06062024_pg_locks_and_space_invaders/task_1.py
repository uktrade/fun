import time
from concurrent.futures import ThreadPoolExecutor

import psycopg2
import psycopg2.extras

from generic_setup import get_cursor, get_locks

sql_1 = '''
BEGIN;
UPDATE my_table
SET v='x' WHERE id=1;
'''

sql_2 = '''
BEGIN;
UPDATE my_table SET v='x' WHERE id=2;  
UPDATE my_table SET v='x' WHERE id=1;
'''

sql_1_b = '''
UPDATE my_table SET v='x' WHERE id=2;  
'''


with \
        ThreadPoolExecutor(max_workers=2) as executor, \
        get_cursor(application_name='block_or_not_1') as cur_1, \
        get_cursor(application_name='block_or_not_2') as cur_2:

    locks_future = executor.submit(get_locks, ('block_or_not_1', 'block_or_not_2'))
    cur_1.execute('SET statement_timeout = 5000;')
    cur_2.execute('SET statement_timeout = 5000;')


# Somewhere here a solution needs to be implemented...
    print('Running...\n')
    try:
        print('Connection 1:', sql_1)
        cur_1.execute(sql_1)

        if sql_1_b:
            print('Connection 1:', sql_1_b)
            def after_delay():
                time.sleep(0.25)
                cur_1.execute(sql_1_b)
            executor.submit(after_delay)

        print('Connection 2:', sql_2)
        cur_2.execute(sql_2)

    except psycopg2.errors.DeadlockDetected:
        print("\033[91m\033[1mDEADLOCK")
    else:
        print("\033[92m\033[1mNO BLOCK - Move onto the next task :)")
