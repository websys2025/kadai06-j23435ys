"""
使用するオープンデータ
名称：気象庁 防災気象情報 API
概要：日本各地の天気予報や防災情報を提供するオープンデータ。
提供元：気象庁（Japan Meteorological Agency）

参照エンドポイント
URL: https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json
機能: 東京都の天気予報（当日、翌日、翌々日）を取得

使い方
- エリアコードを変更することで他地域のデータも取得可能。
-実行することで天気データを取得できる
"""

import requests

def fetch_weather_forecast():
    try:
        response = requests.get("https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json")
        response.raise_for_status()
        data = response.json()

        forecasts = data[0]['timeSeries'][0]['areas'][0]['weathers']
        dates = data[0]['timeSeries'][0]['timeDefines']

        print("【東京都の天気予報】")
        for date, weather in zip(dates, forecasts):
            print(f"{date} の予報: {weather}")
    except requests.RequestException as e:
        print(f"データ取得に失敗しました: {e}")
    except (KeyError, IndexError) as e:
        print(f"データ解析に失敗しました: {e}")

if __name__ == "__main__":
    fetch_weather_forecast()
