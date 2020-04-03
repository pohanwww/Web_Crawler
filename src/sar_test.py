import pandas as pd
import matplotlib.pyplot as plt
import talib

data = pd.read_csv("etoro_data/17_FiveMinutes.csv")
# print(data)
# Drop the NaN values
# data = data.dropna()


# Calculate parabolic sar
data['SAR'] = talib.SAR(data.High, data.Low, acceleration=0.02, maximum=0.2)

# data[['Close', 'SAR']][:500].plot(figsize=(10,5))
# plt.grid()
# plt.show()


# Calculate Tenkan-sen
high_9 = data.High.rolling(9).max()
low_9 = data.Low.rolling(9).min()
data['tenkan_sen_line'] = (high_9 + low_9) /2
# Calculate Kijun-sen
high_26 = data.High.rolling(26).max()
low_26 = data.Low.rolling(26).min()
data['kijun_sen_line'] = (high_26 + low_26) / 2
# Calculate Senkou Span A
data['senkou_spna_A'] = ((data.tenkan_sen_line + data.kijun_sen_line) / 2).shift(26)
# Calculate Senkou Span B
high_52 = data.High.rolling(52).max()
low_52 = data.High.rolling(52).min()
data['senkou_spna_B'] = ((high_52 + low_52) / 2).shift(26)
# Calculate Chikou Span B
data['chikou_span'] = data.Close.shift(-26)

# Plot closing price and parabolic SAR
komu_cloud = data[['Close','SAR']][:1000].plot(figsize=(12, 7))
# Plot Komu cloud
komu_cloud.fill_between(data.index[:1000], data.senkou_spna_A[:1000], data.senkou_spna_B[:1000],
 where=data.senkou_spna_A[:1000] >= data.senkou_spna_B[:1000], color='lightgreen')
komu_cloud.fill_between(data.index[:1000], data.senkou_spna_A[:1000], data.senkou_spna_B[:1000],
 where=data.senkou_spna_A[:1000] < data.senkou_spna_B[:1000], color='lightcoral')
plt.grid()
plt.legend()
plt.show()

data['signal'] = 0
data.loc[(data.Close > data.senkou_spna_A) & (data.Close >
 data.senkou_spna_B) & (data.Close > data.SAR), 'signal'] = 1

data.loc[(data.Close < data.senkou_spna_A) & (data.Close <
 data.senkou_spna_B) & (data.Close < data.SAR), 'signal'] = -1

print(data['signal'].value_counts())


# Calculate daily returns
daily_returns = data.Close.pct_change()
# Calculate strategy returns
data['strategy_returns'] = daily_returns *data['signal'].shift(1)
data[['signal', 'strategy_returns']].to_csv("sar.csv")
# print(strategy_returns)
# Calculate cumulative returns
(data['strategy_returns']+1).cumprod().plot(figsize=(10,5))
# Plot the strategy returns
plt.xlabel('Date')
plt.ylabel('Strategy Returns (%)')
plt.grid()
plt.show()