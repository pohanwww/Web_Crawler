import requests
import pandas as pd
import time

instrument_id_list = ['17', '18', '19', '22']
# instrument_id_list = ['19'] 
# time_mode_list = ['TenMinutes']
time_mode_list = ['OneMinute', 'FiveMinutes', 'TenMinutes', 'FifteenMinutes', 'ThirtyMinutes', 'OneHour', 'FourHours', 'OneDay', 'OneWeek']
# etoro = requests.get('https://candle.etoro.com/candles/desc.json/'+time_mode_list[0]+'/1000/' + instrument_id_list[0]) #natgas
# etoro = requests.get('https://candle.etoro.com/candles/desc.json/OneDay/1000/17') #oil
# etoro = requests.get('https://candle.etoro.com/candles/desc.json/OneDay/1000/18') #gold
# etoro = requests.get('https://candle.etoro.com/candles/desc.json/OneDay/1000/19') #silver

for instrument_id in instrument_id_list:
    for time_mode in time_mode_list:
        try:
            etoro = requests.get('https://candle.etoro.com/candles/desc.json/'+time_mode+'/1000/' + instrument_id) #natgas
            time.sleep(0.5)
            content = etoro.json()
            df_new = pd.DataFrame(content['Candles'][0]['Candles'])
            try:
                df_old = pd.read_csv('./etoro_data/' + instrument_id + '_' + time_mode + '.csv')
                try:
                    # print(df_new[df_new['FromDate'] == df_old['FromDate'][0]])
                    index_ = df_new[df_new['FromDate'] == df_old['FromDate'][0]].index[0]
                    df_old_drop = df_old.drop(index=0, axis=0)
                    index_ = index_ + 1
                    # print(df_new.drop(df_old.index[index_:]).count())
                    df_new_drop = df_new.drop(index=[index_,], axis=0)
                    new = pd.concat([df_new_drop,df_old_drop],axis=0, ignore_index = True)
                    new.to_csv('./etoro_data/' + instrument_id + '_' + time_mode + '.csv', index=False)
                except:
                    print('process error')
            except:
                print('There is no data of {}, {}'.format(instrument_id, time_mode))
                # df_new.to_csv('./etoro_data/' + instrument_id + '_' + time_mode + '.csv', index=False)
        except:
            print('api error')
