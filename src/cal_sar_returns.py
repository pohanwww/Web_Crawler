import pandas as pd
import matplotlib.pyplot as plt
import talib

data = pd.read_csv("etoro_data/17_currentFiveMinutes.csv")
data = data.iloc[::-1].reset_index(drop=True)

# Drop the NaN values
# data = data.dropna()


# Calculate parabolic sar
data['SAR'] = talib.SAR(data.High, data.Low, acceleration=0.02, maximum=0.2)

data[['Close', 'SAR']].plot(figsize=(10,5))
plt.grid()
# print(data)
# plt.show()
data.to_csv("sar.csv")
data['signal'] = 0
data.loc[(data.Open > data.SAR), 'signal'] = 1
data.loc[(data.Open < data.SAR), 'signal'] = -1

start_value = 0
end_value = 0
holding = [False, 0]
money = 100
total_gain = []
total_loss = []
for index in data.index.values.tolist():
    if holding[0] == False:
        if data['signal'].iloc[index] != 0:
            holding = [True, data['signal'].iloc[index]]
            start_value = data.Open.iloc[index] + 0.05 if holding[1] == 1 else data.Open.iloc[index]
    elif holding[0] == True:
        if holding[1] != data['signal'].iloc[index]:
            end_value = data.Open.iloc[index] if holding[1] == 1 else data.Open.iloc[index] + 0.05
            persentage = abs(1 - end_value / start_value)
            if (end_value > start_value and holding[1] == 1) or (end_value < start_value and holding[1] == -1):
                total_gain.append(money * persentage)
            else:
                total_loss.append(-(money * persentage))
            
            holding[1] = data['signal'].iloc[index]
            start_value = data.Open.iloc[index] + 0.05 if holding[1] == 1 else data.Open.iloc[index]
print('gain:', sum(total_gain))
print('count:', len(total_gain))
print(sum(total_gain)/len(total_gain))

print('gain:', sum(total_loss))
print('count:', len(total_loss))
print(sum(total_loss)/len(total_loss))

print("result:", sum(total_gain) + sum(total_loss))
            # if end_value >

# # Calculate daily returns
# daily_returns = data.Close.pct_change()
# # Calculate strategy returns
# data['strategy_returns'] = daily_returns *data['signal'].shift(1)
data['signal'].to_csv("sar_test.csv")
# # print(strategy_returns)
# # Calculate cumulative returns
# (data['strategy_returns']+1).cumprod().plot(figsize=(10,5))
# # Plot the strategy returns
# plt.xlabel('Date')
# plt.ylabel('Strategy Returns (%)')
# plt.grid()
# plt.show()