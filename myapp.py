'''
 Visualisasi Data Interaktif Fluktuasi Harga Saham (Level 3)
 
        Tugas Besar Visualisasi Data IF-41-GAB04
              Rizky Dewa Sakti_1301180358
'''

# Data handling
import pandas as pd

# Bokeh libraries
from bokeh.io import output_file
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Tabs, Panel
from bokeh.models import HoverTool

##Import stock_market.csv
df_stock = pd.read_csv("http://bit.ly/VD_FP")

##Mengubah tipe kolom 'Date' menjadi DateTime
df_stock['Date'] = pd.to_datetime(df_stock.Date)

##Rename atribut 'Adj Close' -> 'Adj_Close' supaya data dapat dioutput pada saat pengaturan Hovertool
df_stock = df_stock.rename(columns={"Adj Close" : "Adj_Close"})

##Split Data
df_Hangseng = df_stock[(df_stock['Name'] == 'HANG SENG')]
df_Nasdaq = df_stock[(df_stock['Name'] == 'NASDAQ')]
df_Nikkei = df_stock[(df_stock['Name'] == 'NIKKEI')]

##CollumnDataSource
cds_Hangseng = ColumnDataSource(df_Hangseng)
cds_Nasdaq = ColumnDataSource(df_Nasdaq)
cds_Nikkei = ColumnDataSource(df_Nikkei)

##Level 3
#a. Set Output File Extension
output_file('Saham_Level3.html', title='Saham_Level3')

##b. Konfigurasi fig dan Gambar Garis dari 'Adj_Close' dengan 'Date'
fig_adj_close = figure(x_axis_type='datetime',
                  plot_height=700,
                  x_axis_label='Date',
                  y_axis_label='Adj_Close',
                  title='Adj_Close')
fig_adj_close.plot_width=1300

fig_adj_close.line(x='Date', y='Adj_Close', source=cds_Hangseng, color='Orange', legend='HANGSENG')
fig_adj_close.line(x='Date', y='Adj_Close', source=cds_Nasdaq, color='green', legend='NASDAQ')
fig_adj_close.line(x='Date', y='Adj_Close', source=cds_Nikkei, color='blue', legend='NIKKEI')

##c. Konfigurasi fig dan Gambar Garis dari 'Volume' dengan 'Date'
fig_vol = figure(x_axis_type='datetime',
                  plot_height=700,
                  x_axis_label='Date',
                  y_axis_label='Volume',
                  title='Volume')
fig_vol.plot_width=1300

fig_vol.line(x='Date', y='Volume', source=cds_Hangseng, color='Orange', legend='HANG SENG')
fig_vol.line(x='Date', y='Volume', source=cds_Nasdaq, color='green', legend='NASDAQ')
fig_vol.line(x='Date', y='Volume', source=cds_Nikkei, color='blue', legend='NIKKEI')


##d. Konfigurasi fig dan Gambar Garis dari 'Day Perc Change' dengan 'Date'
fig_day = figure(x_axis_type='datetime',
                  plot_height=700,
                  x_axis_label='Date',
                  y_axis_label='Day_Perc_Change',
                  title='Day Perc Change')
fig_day.plot_width=1300

fig_day.line(x='Date', y='Day_Perc_Change', source=cds_Hangseng, color='Orange', legend='HANG SENG')
fig_day.line(x='Date', y='Day_Perc_Change', source=cds_Nasdaq, color='green', legend='NASDAQ')
fig_day.line(x='Date', y='Day_Perc_Change', source=cds_Nikkei, color='blue', legend='NIKKEI')

##e. Set 'Hide graph at clicked Legend' function
fig_adj_close.legend.click_policy = 'hide'
fig_vol.legend.click_policy = 'hide'
fig_day.legend.click_policy = 'hide'

##f. Set Panel for each ['Adj_Close' ; 'Volume' ; 'Day Perc Change']
panel_adj_close = Panel(child=fig_adj_close, title='Adjusted Close')
panel_vol = Panel(child=fig_vol, title='Volume')
panel_day = Panel(child=fig_day, title='Day Perc Change')
tabs = Tabs(tabs=[panel_adj_close, panel_vol, panel_day])

##g. HoverTool
tooltips = [
            ('Name','@Name'),
            ('Date', '@Date{%F}'),
            ('Adj Close', '@Adj_Close'),
            ('Volume', '@Volume'),
            ('Day_Perc_Change','@Day_Perc_Change'),
           ]

fig_adj_close.add_tools(HoverTool(tooltips=tooltips, formatters={'@Date': 'datetime'}))
fig_vol.add_tools(HoverTool(tooltips=tooltips, formatters={'@Date': 'datetime'}))
fig_day.add_tools(HoverTool(tooltips=tooltips, formatters={'@Date': 'datetime'}))

##h. ShowPlot
show(tabs)
