#!/usr/bin/python
#-*- coding:utf-8 -*-

from requests_oauthlib import OAuth1Session
import traceback

"""
TwitterのユーザをフォローするためのUtil
"""
def follow( oauth_client, user_id ):
    """
    特定のユーザをTwitterでフォローする.
    Args:
    oauth_client: Oauth認証されたクライアント
            (requests_oauthlibのOAuth1Sessionオブジェクト)
    user_id:    フォローする対象twitterユーザのuserId (数値)
    Returns:
        フォロー成功すればTrue, すでにフォローしていたなどの理由でフォローできなかったときはFalseを返却する。
    Raises:
        IOError:
            TwitterAPIの実行に失敗したとき。
            すでにフォローしているユーザを指定されたときはErrorはraiseされないが、存在しないuserIDを指定されたときはErrorとなる。
    """
    target_url = "https://api.twitter.com/1.1/friendships/create.json"

    # follow対象ユーザIDと相手に通知を送るかどうかのフラグ(True固定)
    params = {"user_id":user_id, "follow": True}

    try:
        # Follow API実行
        response = oauth_client.post(target_url, params = params)

        if response.status_code == 200:
            #フォロー成功
            return True
        else:
            #フォロー失敗
            return False
    except:
        raise IOError("Unexpected error occurred while consuming twitter's Follow API. user_id="+ str(user_id)+", stacktrace="+ traceback.format_exc() )


# このスクリプトを実行したら
if __name__ == "__main__":

    import sys
    import yaml
 
    # 設定ファイルからtokenを読み込み   
    with open("token.yaml", "r") as f:
        tokens = yaml.load( f.read() )
        CK = tokens["consumer_key"]
        CS = tokens["consumer_secret"]
        AT = tokens["access_token"]
        AS = tokens["access_token_secret"]

    twitter_client = OAuth1Session(CK, CS, AT, AS)
    user_id = 2527670030

    print follow( twitter_client, user_id )
    
    
    
    
