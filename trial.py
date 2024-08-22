# import sqlite3
#
# conn = sqlite3.connect('music_2/music_2.sqlite')
# cursor = conn.cursor()
# cursor.execute('SELECT * FROM music_2')
# results = cursor.fetchall()
# for row in results:
#     print(row)
# conn.close()
import torch
from matplotlib import pyplot as plt
import os
import pandas as pd
# 获取 Windows 系统的桌面路径
desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')
# print(desktop_path)
path = desktop_path + '/full_CSpider/CSpider/'
# for li in os.listdir(path):
#     print(li)

# char_emb.txt
# database
# dev.json
# dev_gold.sql
# README.txt
# tables.json
# test_data
# test_database
# train.json
# train_gold.sql

import json

# 打开 JSON 文件
# with open(path + 'test_data/test.json', 'r', encoding='utf-8') as file:
#     # 读取文件内容
#     data = file.read()
with open(path + 'tables.json', 'r', encoding='utf-8') as file:
    # 读取文件内容
    data = file.read()

# 解析 JSON 数据
json_data = json.loads(data)


# 处理解析后的 JSON 数据
def sum_1():
    pass


i = 0
for item in json_data:
    print(item)
    i += 1
    if i > 10:
        break

# 打印例子-------test.json
# {'db_id': 'e_commerce',
#  'query': 'SELECT count(*) FROM Shipment_Items',
#  'query_toks': ['SELECT', 'count', '(', '*', ')', 'FROM', 'Shipment_Items'],
#  'query_toks_no_value': ['select', 'count', '(', '*', ')', 'from', 'shipment_items'],
#  'question': '装运了多少货物？',
#  'question_toks': ['装', '运', '了', '多', '少', '货', '物', '？'],
#  'sql': {'orderBy': [],
#          'from': {'table_units': [['table_unit', 7]], 'conds': []},
#          'union': None,
#          'except': None,
#          'groupBy': [],
#          'limit': None,
#          'intersect': None,
#          'where': [],
#          'having': [],
#          'select': [False, [[3, [0, [0, 0, False], None]]]]}
#  }
#
# {'db_id': 'soccer_3',
#  'query': 'SELECT count(*) FROM club',
#  'query_toks': ['SELECT', 'count', '(', '*', ')', 'FROM', 'club'],
#  'query_toks_no_value': ['select', 'count', '(', '*', ')', 'from', 'club'],
#  'question': '有多少个俱乐部？',
#  'question_toks': ['有', '多', '少', '个', '俱', '乐', '部', '？'],
#  'sql': {'orderBy': [],
#          'from': {'table_units': [['table_unit', 0]], 'conds': []},
#          'union': None,
#          'except': None,
#          'groupBy': [],
#          'limit': None,
#          'intersect': None,
#          'where': [],
#          'having': [],
#          'select': [False, [[3, [0, [0, 0, False], None]]]]}
#  }

# 打印例子-----tables_test.json
# {'column_names': [[-1, '*'], [0, 'city id'], [0, 'country'], [0, 'city'], [0, 'max team number'], [1, 'agent id'], [1, 'name'], [1, 'years of experiencing'], [2, 'customer id'], [2, 'player'], [2, 'country'], [2, 'age'], [3, 'city id'], [3, 'agent id'], [3, 'year'], [3, 'number team'], [4, 'city id'], [4, 'customer id'], [4, 'customer rating']],
#  'column_names_original': [[-1, '*'], [0, 'City_ID'], [0, 'Country'], [0, 'City'], [0, 'Max_team_number'], [1, 'Agent_ID'], [1, 'Name'], [1, 'Years_of_experiencing'], [2, 'Customer_ID'], [2, 'Player'], [2, 'Country'], [2, 'Age'], [3, 'City_ID'], [3, 'Agent_ID'], [3, 'Year'], [3, 'Number_team'], [4, 'City_ID'], [4, 'Customer_ID'], [4, 'Customer_rating']],
#  'column_types': ['text', 'number', 'text', 'text', 'number', 'number', 'text', 'number', 'number', 'text', 'text', 'number', 'number', 'text', 'text', 'number', 'number', 'number', 'number'],
#  'db_id': 'travel_agent',
#  'foreign_keys': [[13, 5], [12, 1], [17, 8], [16, 1]],
#  'primary_keys': [1, 5, 8, 12, 16],
#  'table_names': ['city', 'agent', 'customer', 'city agent', 'city customer'],
#  'table_names_original': ['city', 'agent', 'customer', 'city_agent', 'city_customer']}
