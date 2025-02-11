# replicate_paper_results_forcasting_using_LSTM_models
Replicate research paper results for forecasting S&amp;P 500 index using LSTM models

## Reference

- **Research paper**: https://arxiv.org/abs/2501.17366 ; https://arxiv.org/pdf/2501.17366
- **Data Sources**
  + **S&P 500 index**: https://www.wsj.com/market-data/quotes/index/SPX/historical-prices
  + **U.S. Treasury Yields**: https://www.kaggle.com/datasets/guillemservera/us-treasury-yields-daily
  + **Volatility Index**: https://www.kaggle.com/datasets/guillemservera/vix-cboe-volatility-index-daily-updated

[1]: https://arxiv.org/pdf/2501.17366
[2]: https://www.wsj.com/market-data/quotes/index/SPX/historical-prices

## Data Sources &amp; Features

The [dataset][2] used in the study is the daily values for the S&amp;P 500 (SPX) over the period of October 2013 to September 2014.
The historical SPX data include:

- 50 and 200-day Moving Averages (MOV AVG 50/200D)
- 14-day Relative Strength Index (RSI 14D)
- Open and Closing Prices (PX OPEN/CLOSE)
- High and Low Prices (PX HIGH/LOW)
- Daily Price High-Low Difference (PX HIGH LOW DIFFERENCE)
- Daily Volume (PX VOLUME)
- 30-day Volatility (VOLATILITY 30D)
- Beta (BETA ADJ OVERRIDABLE)
  
Along with the historical SPX data, the following additional metrics are considered:

- **SPX Ratios:**
  + Price-to-Earnings Ratio (PE RATIO)
  + Price-to-Book Ratio (PX TO BOOK RATIO)
  + Price-to-Sales Ratio (PX TO SALES RATIO)
  + Earnings Yield (EARN YLD)
  
- **Market Metrics:**
  + Volatility Index (VIX)
  + 10-Year Treasury Yield (USGG10YR)
  + NAPM Manufacturing PMI (NAPMPMI)
  + Consumer Confidence Index (CONCCONF)

The original data source used in the [reasearch paper][1] was gotten from [bloomberg](https://www.bloomberg.com/). 
