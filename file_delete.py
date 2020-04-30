#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json

TOKEN = '' # 取得したトークン https://api.slack.com/custom-integrations/legacy-tokens
TARGET_USER = u'' # 実行者

user_list_url = 'https://slack.com/api/users.list'
files_list_url = 'https://slack.com/api/files.list'
files_delete_url = 'https://axlbit.slack.com/api/files.delete'

users_list_param = {"token": TOKEN}
res = requests.get(user_list_url, users_list_param)
users = json.loads(res.text)['members']
user_id = 0
for u in users:
    if u['name'] == TARGET_USER:
        user_id = u['id']

if user_id != 0:
    file_list_param = {'token': TOKEN, 'user': user_id}
    res = requests.get(files_list_url, file_list_param)
    files = res.json()['files']
    for f in files:
        files_delete_param = {"token": TOKEN, "file": f['id']}
        requests.post(files_delete_url, files_delete_param)

else:
    print('no user: {}'.format(TARGET_USER))

print('DONE!!!!!!!!!!!!!!!!!')