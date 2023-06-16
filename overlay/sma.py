def SMA(src: pd.Series, bars:int):
  return src.rolling(window=bars).mean()
