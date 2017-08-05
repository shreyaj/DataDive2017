import pandas as pd

df = pd.read_csv("NEW - TRANSACTION DATA.csv")
grouped = df.groupby(['DonorID']).size().reset_index().rename(columns={0:'count'})
grouped = grouped.set_index('DonorID')
amount = df.groupby(['DonorID'])[['Amount']].sum()
grouped['Amount'] = amount

oneTime = grouped.where(grouped['count'] == 1)
recurring = grouped.where(grouped['count'] > 1)

oneTimeMedianDonAmount = oneTime['Amount'].median()
print("OT AMOUNT MED")
print(oneTimeMedianDonAmount)

recurringMedianDonAmount = recurring['Amount'].median()
print("REC AMOUNT MED")
print(recurringMedianDonAmount)

oneTimeMeanDonAmount = oneTime['Amount'].mean()
print("OT AMOUNT MEAN")
print(oneTimeMeanDonAmount)

recurringMeanDonAmount = recurring['Amount'].mean()
print("REC AMOUNT MEAN")
print(recurringMeanDonAmount)

# GET POPULAR AND NON-POPULAR DAYS
oneTimeAll = oneTime.reset_index().merge(df, on = 'DonorID')
OTDayOfWeekCount = oneTimeAll.groupby(['dayofweek']).size().reset_index().rename(columns={0:'count'})
OTPopDayOfWeek = OTDayOfWeekCount.loc[OTDayOfWeekCount['count'].idxmax()]
print("POP DAY OT")
print(OTPopDayOfWeek)

recurringAll = recurring.reset_index().merge(df, on = 'DonorID')
recDayOfWeekCount = recurringAll.groupby(['dayofweek']).size().reset_index().rename(columns={0:'count'})
recPopDayOfWeek = recDayOfWeekCount.loc[recDayOfWeekCount['count'].idxmax()]
print("POP DAY REC")
print(recPopDayOfWeek)

# Location & Days Correlation to be added

