# i have upload my code hear and you can copy and run it to check if it is ok. if there is anything i should fix please lmk!!!



# imoprtant impoertant libraries
import pandas as pd
# read the csv file
df = pd.read_csv("tornados.csv")
# Filter and group the data by year to analyze trends over time
df['date'] = pd.to_datetime(df['date'])  # Convert the 'date' column to a datetime object
df['yr'] = df['date'].dt.year  # Extract the year from the 'date' column
# Group by year and calculate property loss and fatalities
property_loss_by_year = df.groupby('yr')['loss'].sum()
fatalities_by_year = df.groupby('yr')['fat'].sum()
# Calculate mean and median for property loss and fatalities for each year
property_loss_mean = df.groupby('yr')['loss'].mean()
property_loss_median = df.groupby('yr')['loss'].median()
fatalities_mean = df.groupby('yr')['fat'].mean()
fatalities_median = df.groupby('yr')['fat'].median()
# tornado path length
path_length_mean = df.groupby('yr')['len'].mean()
path_length_median = df.groupby('yr')['len'].median()
# tornado severity
tornado_severity_mean = df.groupby('yr')['mag'].mean()
tornado_severity_median = df.groupby('yr')['mag'].median()
print("\nMean Property Loss by Year:")
print(property_loss_mean)
print("\nMedian Property Loss by Year:")
print(property_loss_median)
print("\nMean Fatalities by Year:")
print(fatalities_mean)
print("\nMedian Fatalities by Year:")
print(fatalities_median)
print("\nAverage Tornado Path Length by Year:")
print(path_length_mean)
print("\nMedian Tornado Path Length by Year:")
print(path_length_median)
print("\nTrend in Tornado Severity Over Time:")
print(tornado_severity_mean.pct_change())
print("\nAverage Tornado Severity by Year:")
print(tornado_severity_mean)
print("\nMedian Tornado Severity by Year:")
print(tornado_severity_median)
#graph to represent loss, fatalities, path length, and tornado severity
plt.figure(figsize=(16, 16))
plt.subplot(4, 1, 1)
plt.plot(property_loss_by_year.index, property_loss_by_year, label='Property Loss')
plt.title('Property Loss due to Tornadoes Over Time')
plt.xlabel('Year')
plt.ylabel('Property Loss')
plt.legend()
plt.subplot(4, 1, 2)
plt.plot(fatalities_by_year.index, fatalities_by_year, label='Fatalities', color='orange')
plt.title('Fatalities due to Tornadoes Over Time')
plt.xlabel('Year')
plt.ylabel('Fatalities')
plt.legend()
plt.subplot(4, 1, 3)
plt.plot(path_length_mean.index, path_length_mean, label='Average Path Length', color='green')
plt.plot(path_length_median.index, path_length_median, label='Median Path Length', color='blue')
plt.title('Tornado Path Length Over Time')
plt.xlabel('Year')
plt.ylabel('Path Length')
plt.legend()
plt.subplot(4, 1, 4)
plt.plot(tornado_severity_mean.index, tornado_severity_mean, label='Average Severity', color='red')
plt.plot(tornado_severity_median.index, tornado_severity_median, label='Median Severity', color='purple')
plt.title('Tornado Severity Over Time')
plt.xlabel('Year')
plt.ylabel('Tornado Severity')
plt.legend()
plt.tight_layout()  
plt.show()

