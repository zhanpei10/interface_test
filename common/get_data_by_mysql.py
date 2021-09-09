'''
获得数据库数据， 根据数据库返回的结果进行断言
'''
import pymysql
from common.common_method import *
from common.get_config import *


class MysqlData:
    '''
    初始化数据库对下
    '''

    def __init__(self):
        # 82环境
        self.conn = pymysql.connect(**get_mysql_config('SIT_MYSQL'))
        # 临港环境
        # self.conn = pymysql.connect(**get_mysql_config('LG_MYSQL'))

    def get_count(self, table_name, filed_name, filed_value):
        '''

        :param table_name:  表名称
        :param filed_name: 字段名称
        :param filed_value: 字段值
        :return:
        '''
        sql = 'select * from {0} where {1}={2}'.format(table_name, filed_name, filed_value)
        print(sql)
        c = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        count = c.execute(sql)
        return count

    def get_params(self, get_sql, number):
        '''
        查询数据库当中的数据进行传参
        :param number:  指定要读取几行
        :param get_sql: 获取数据使用的sql
        :return:
        '''
        # 获得一个游标对象
        c = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        c.execute(get_sql)
        return c.fetchmany(number)


if __name__ == '__main__':
    print(get_mysql_config('SIT_MYSQL'))
    get_data_sql = 'SELECT gp.process_id, gp.grid_id, gr.serial, gpe.event_type ' \
                   'FROM info_r_grid_process gp ' \
                   'JOIN info_r_grid_process_event_type gpe ' \
                   'ON gp.process_id = gpe.process_id ' \
                   'JOIN info_grid gr ' \
                   'ON gr.id = gp.grid_id  where event_type = 100000373'
    print(MysqlData().get_params(get_data_sql, 1))
