import requests
import pandas as pd

instrument_id_list = ['17', '18', '19', '22']
time_mode_list = ['OneMinute', 'FiveMinutes', 'TenMinutes', 'FifteenMinutes', 'ThirtyMinutes', 'OneHour', 'FourHours', 'OneDay', 'OneWeek']
etoro = requests.get('https://candle.etoro.com/candles/desc.json/'+time_mode_list[0]+'/1000/' + instrument_id_list[0]) #natgas
# etoro = requests.get('https://candle.etoro.com/candles/desc.json/OneDay/1000/17') #oil
# etoro = requests.get('https://candle.etoro.com/candles/desc.json/OneDay/1000/18') #gold
# etoro = requests.get('https://candle.etoro.com/candles/desc.json/OneDay/1000/19') #silver
content = etoro.json()
# print(content['Candles'][0]['Candles'])
df = pd.DataFrame(content['Candles'][0]['Candles'])
try:
    df_old = pd.read_csv('./etoro_data/' + instrument_id_list[0] + '_' + time_mode_list[0] + '.csv')
    # df_old['FromDate'][0]
except:
    print('there is no data of {}, {}'.format(instrument_id_list[0], time_mode_list[0]))
    df.to_csv('./etoro_data/' + instrument_id_list[0] + '_' + time_mode_list[0] + '.csv')
print(df['FromDate'][0])
