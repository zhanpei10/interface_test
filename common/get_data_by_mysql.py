'''
获得数据库数据， 根据数据库返回的结果进行断言
'''
import pymysql
from common.common_method import *


class MysqlData:
    '''
    初始化数据库对下
    '''

    def __init__(self):
        self.conn = pymysql.connect(**get_mysql_config('SIT_MYSQL'))

    def get_count(self, table_name, filed_name, filed_value):
        '''
        查看数据是否正常插入
        :return:
        '''
        sql = 'select * from {0} where {1}={2}'.format(table_name, filed_name, filed_value)
        print(sql)
        c = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        count = c.execute(sql)
        return count


if __name__ == '__main__':
    print(get_mysql_config('SIT_MYSQL'))
    print(MysqlData().get_count('info_case', 'id', 1251))
