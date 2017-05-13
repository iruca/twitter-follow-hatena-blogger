#!/usr/bin/python
#-*- coding:utf-8 -*-

"""
「はてなブログに投稿しました」というテキストでツイート検索を行い、
出てきたツイートを行ったユーザを1人フォローする。
"""
import sys
import yaml
import search_hatenablogger_util
import twitter_follow_util

from requests_oauthlib import OAuth1Session

# 設定ファイルからtokenを読み込み
with open("token.yaml", "r") as f:
    tokens = yaml.load( f.read() )
    CK = tokens["consumer_key"]
    CS = tokens["consumer_secret"]
    AT = tokens["access_token"]
    AS = tokens["access_token_secret"]

twitter_client = OAuth1Session(CK, CS, AT, AS)

# はてなブロガーのuser ID(数値)リストを15人分取得
try:
    blogger_user_ids = search_hatenablogger_util.search_hatena_bloggers(twitter_client)
except:
    print "failed to get bloggers' userIDs"
    exit()

# そのうち1人をフォロー
user_id = blogger_user_ids[0]
is_successed = twitter_follow_util.follow( twitter_client, user_id )

if is_successed:
    print "successfully followed "+ str(user_id)
else:
    print "failed to follow "+ str(user_id)
