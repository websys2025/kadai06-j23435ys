"""
【使用するオープンデータ】
名称：e-Stat- 出入国管理統計
概要：法務省が提供する、日本への出入国者数に関する統計データ。

【エンドポイント情報】
URL: http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
機能:統計IDで指定されたデータから、地域や分類を指定してデータを取得

【使い方】
- データを取得してJSON形式で解析
"""
import requests
#出入国管理統計
#出入国管理統計 / 出入（帰）国者数
APP_ID = "41a8ec7dc0cbd4d5ab03a8b1c7eb0f3723b6449d"
API_URL  = "http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId":"0000020201",
    "cdArea":"12101,12102,12103,12104,12105,12106",
    "cdCat01": "A1101",
    "metaGetFlg":"Y",
    "cntGetFlg":"N",
    "explanationGetFlg":"Y",
    "annotationGetFlg":"Y",
    "sectionHeaderFlg":"1",
    "replaceSpChars":"0",
    "lang": "J"  # 日本語を指定
}



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)