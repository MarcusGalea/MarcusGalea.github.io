from bokeh.models import Select, ColumnDataSource, ColorBar, LinearColorMapper, CustomJS
from bokeh.plotting import figure, save, output_file
from bokeh.layouts import column
from bokeh.palettes import Viridis256
from src.loading_functions import *
#get cwd
cwd = os.getcwd()
#get data folder
data_folder = os.path.join(cwd, 'data')

df = load_or_download_lego_data(data_folder)
df = preprocess_data(df)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
grouped = df.groupby(['Year', 'Month', 'subtheme']).size().reset_index(name='Count')
# Define your threshold
threshold = 7  # Replace X with the desired value
 
# Filter the DataFrame
filtered = grouped[grouped['Count'] > threshold]
#convert dates to strings in filtered
filtered['Year'] = filtered['Year'].astype(str)
filtered['Month']= filtered['Month'].astype(str)
options = filtered['Year'].unique()

# Specify the output file
output_file("plot2.html")

# Create a Select object for the years
years = sorted(filtered['Year'].unique())
select = Select(title="Year", value=str(years[0]), options=[str(year) for year in years])

# Create a figure
subthemes = sorted(filtered['subtheme'].unique())
months = [str(i) for i in range(1, 13)]
p = figure(x_range=months, y_range=list(reversed(subthemes)), toolbar_location=None, tools="")

# Create a color mapper
mapper = LinearColorMapper(palette=Viridis256, low=filtered.Count.min(), high=filtered.Count.max())

# Create a rectangle glyph and add it to the figure
source = ColumnDataSource(data=filtered[filtered['Year'] == years[0]])
p.rect(x="Month", y="subtheme", width=1, height=1, source=source,
       fill_color={'field': 'Count', 'transform': mapper}, line_color=None)

# Create a color bar
color_bar = ColorBar(color_mapper=mapper, location=(0, 0), orientation='horizontal')
p.add_layout(color_bar, 'below')

# Create a callback function to update the data source
callback = CustomJS(args=dict(source=source, select=select, df=filtered), code="""
    var year = select.value;
    var data = df.filter(d => d['Year'] == year);
    source.data = data;
""")

select.js_on_change('value', callback)

# Add the Select object and the figure to a layout and save it
layout = column(select, p)
save(layout)