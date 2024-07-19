import time

from contextlib import contextmanager

import psycopg2
import psycopg2.extras

setup = '''
CREATE EXTENSION IF NOT EXISTS pgrowlocks;
DROP TABLE IF EXISTS my_table;
CREATE TABLE my_table(id int, v text);
INSERT INTO my_table VALUES (1, 'a'), (2, 'b');
'''

@contextmanager
def get_cursor(application_name):
    with \
            psycopg2.connect(host="127.0.0.1", port="5432", user="postgres", password="password", application_name=application_name) as conn, \
            conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
        yield cur


with get_cursor(application_name='block_or_not_setup') as cur_setup:
    cur_setup.execute(setup)


def get_locks(application_names):
    time.sleep(0.5)
    with get_cursor('block_or_not_get_locks') as cur:
        sql = '''
           SELECT a.application_name, mode, relation::regclass, l.* AS table
           FROM pg_locks l
           INNER JOIN pg_stat_activity a ON a.pid = l.pid
           WHERE application_name LIKE 'block\\_or\\_not\\_%' AND relation::regclass::text NOT LIKE 'pg%'
           ORDER BY application_name, relation::regclass::text, mode
        '''
        cur.execute(sql)
        table_locks = cur.fetchall()

        sql = '''
            SELECT application_name, mode, locked_row
            FROM pgrowlocks('my_table'::text)
            CROSS JOIN UNNEST(pids) AS pids(pid)
            CROSS JOIN UNNEST(modes) AS modes(mode)
            INNER JOIN pg_stat_activity a ON a.pid = pids.pid
            WHERE application_name LIKE 'block\\_or\\_not\\_%';
        '''
        cur.execute(sql)
        row_locks = cur.fetchall()
        return table_locks + row_locks;

with get_cursor(application_name='block_or_not_setup') as cur_setup:
    cur_setup.execute(setup)