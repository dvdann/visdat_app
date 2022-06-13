#!/usr/bin/env python
# coding: utf-8

# 
# #### Tugas_Besar_Visdat_IF42GAB01.ipynb
# ### Visualisasi Data Interaktif Fluktuasi Harga Saham
# ## Dosen Pengampu : ERWIN BUDI SETIAWAN, S.Si., M.T.
# ### Final Project
# ### Kelas : IF-43-GAB01
# #### Daniel Septyadi (1301180009)
# #### Friska Alfanda 
# #### Reyhan Pratama

# In[1]:


# Data handling
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
import io


# In[2]:


# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel


# In[3]:


url_stock = "https://cdn.discordapp.com/attachments/810415013076402217/855494072591581184/stock_market.csv"
stock = requests.get(url_stock).content
stock = pd.read_csv(io.StringIO(stock.decode('utf-8')))

#stock


# In[4]:


# ubah tipe data 'Date' dari object menjadi datetime

stock['Date'] = pd.to_datetime(stock.Date)

stock = stock.rename(columns={"Adj Close" : "Adj_Close"})
stock.head()

#stock.info()


# In[5]:


# Split data dengan 'Name' = HANG SENG

condition1 = (stock['Name'] == 'HANG SENG')
df_Hangseng = stock[condition1]
df_Hangseng


# In[6]:


# Hanya ambil data dengan 'Name' = NASDAQ

condition2 = (stock['Name'] == 'NASDAQ')
df_Nasdaq = stock[condition2]
df_Nasdaq


# In[7]:


# Hanya ambil data dengan 'Name' = NIKKEI

condition3 = (stock['Name'] == 'NIKKEI')
df_Nikkei = stock[condition3]
df_Nikkei

output_notebook()


# # LEVEL 1 

# In[8]:


# output file html
output_file('Level1.html', title='Level1')

from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource


# In[9]:


# Buat ColumnDataSource
cds_hs = ColumnDataSource(df_Hangseng)
cds_nd = ColumnDataSource(df_Nasdaq)
cds_nk = ColumnDataSource(df_Nikkei)


# In[10]:


# Buat dan konfigurasikan figure dari Adjusted Close dengan Date

fig = figure(plot_height=600,
             plot_width=900,
             x_axis_label='Date',
             y_axis_label='Adjusted Close',
             title='Adjusted Close Hangseng & Nasdaq & Nikkei')


# In[11]:


# Buat visualisasi garis pada grafik

fig.line(x='Date', y='Adj_Close', 
        color='Red', legend_label='HANG SENG',
        source=cds_hs)

fig.line(x='Date', y='Adj_Close', 
        color='Green', legend_label='NASDAQ',
        source=cds_nd)

fig.line(x='Date', y='Adj_Close', 
        color='Blue', legend_label='NIKKEI',
        source=cds_nk)

fig.legend.location = 'top_right' # posisi legenda


# In[12]:


from bokeh.models import HoverTool


# In[13]:


# Hover

# Hover Hang Seng
hvr_hs = fig.circle(x='Date', y='Adj_Close', source=cds_hs,
                 size=15, alpha=0, hover_fill_color='darkred',
                 hover_alpha=0.5)

# Hover Nasdaq 
hvr_nd = fig.circle(x='Date', y='Adj_Close', source=cds_nd,
                 size=15, alpha=0, hover_fill_color='darkgreen',
                 hover_alpha=0.5)
# Hover Nikkei
hvr_nk = fig.circle(x='Date', y='Adj_Close', source=cds_nk,
                 size=15, alpha=0, hover_fill_color='darkblue',
                 hover_alpha=0.5)


# In[14]:


# Format tampilan dari hoover
tooltips = [
            ('Name','@Name'),
            ('Date', '@Date{%F}'),
            ('Adj Close', '@Adj_Close'),
            ('Volume', '@Volume'),
            ('Day_Perc_Change','@Day_Perc_Change'),
           ]


# In[15]:


# Tambahkan HoverTool ke grafik
fig.add_tools(HoverTool(tooltips=tooltips, formatters={'@Date': 'datetime'}, renderers=[hvr_hs, hvr_nd, hvr_nk]))


# In[16]:


# show plot
show(fig)


# # Level 2&3

# In[17]:


# output file html
output_file('Level2&3.html', title='Level2&3')


# In[18]:


from bokeh.models.widgets import Tabs, Panel


# In[19]:


# Buat dan konfigurasikan figure dari Adjusted Close dengan Date
fig_adj = figure(x_axis_type='datetime',
                  plot_height=500,
                  x_axis_label='Date',
                  y_axis_label='Adj_Close',
                  title='Adj Close')


# In[20]:


# Buat dan konfigurasikan figure dari Volume dengan Date
fig_vol = figure(x_axis_type='datetime',
                  plot_height=500,
                  x_axis_label='Date',
                  y_axis_label='Volume',
                  title='Volume')


# In[21]:


# Buat dan konfigurasikan figure dari Day_Perc_Change dengan Date
fig_dpc = figure(x_axis_type='datetime',
                  plot_height=500,
                  x_axis_label='Date',
                  y_axis_label='Day_Perc_Change',
                  title='Day Perc Change')


# In[22]:


# Buat Garis Grafik Adjust Close
fig_adj.line(x='Date',
           y='Adj_Close',
           source=cds_hs,
           color='red',
           legend_label='HANG SENG')
fig_adj.line(x='Date',
           y='Adj_Close',
           source=cds_nd,
           color='green',
           legend_label='NASDAQ')
fig_adj.line(x='Date',
           y='Adj_Close',
           source=cds_nk,
           color='blue',
           legend_label='NIKKEI')


# In[23]:


# Buat Garis Grafik Volume
fig_vol.line(x='Date',
           y='Volume',
           source=cds_hs,
           color='red',
           legend_label='HANG SENG')
fig_vol.line(x='Date',
           y='Volume',
           source=cds_nd,
           color='green',
           legend_label='NASDAQ')
fig_vol.line(x='Date',
           y='Volume',
           source=cds_nk,
           color='blue',
           legend_label='NIKKEI')


# In[24]:


# Buat Garis Grafik Day Perc Change
fig_dpc.line(x='Date',
           y='Day_Perc_Change',
           source=cds_hs,
           color='red',
           legend_label='HANG SENG')
fig_dpc.line(x='Date',
           y='Day_Perc_Change',
           source=cds_nd,
           color='green',
           legend_label='NASDAQ')
fig_dpc.line(x='Date',
           y='Day_Perc_Change',
           source=cds_nk,
           color='blue',
           legend_label='NIKKEI')


# In[25]:


# fungsi hide jika klik leegnda
fig_adj.legend.click_policy = 'hide'
fig_vol.legend.click_policy = 'hide'
fig_dpc.legend.click_policy = 'hide'


# In[26]:


# samakan ukuran plot
fig_adj.plot_width = fig_vol.plot_width = fig_dpc.plot_width = 900


# In[27]:


# Buat 3 panel, 1 untuk masing-masing conference
panel_adj = Panel(child=fig_adj, title='Adjusted Close')
panel_vol = Panel(child=fig_vol, title='Volume')
panel_dpc = Panel(child=fig_dpc, title='Day Perc Change')


# In[28]:


# Masukkan panel ke dalam tabs
tabs = Tabs(tabs=[panel_adj, panel_vol, panel_dpc])


# In[29]:


# format tooltips untuk hover
tooltips = [
            ('Name','@Name'),
            ('Date', '@Date{%F}'),
            ('Adj Close', '@Adj_Close'),
            ('Volume', '@Volume'),
            ('Day_Perc_Change','@Day_Perc_Change'),
           ]


# In[30]:


# add HoverTool ke Grafik 
fig_adj.add_tools(HoverTool(tooltips=tooltips, formatters={'@Date': 'datetime'}))
fig_vol.add_tools(HoverTool(tooltips=tooltips, formatters={'@Date': 'datetime'}))
fig_dpc.add_tools(HoverTool(tooltips=tooltips, formatters={'@Date': 'datetime'}))


# In[31]:


# tampilkan show
show(tabs)


# In[33]:


# bokeh serve --show myapp.py


# For more on all things interaction in Bokeh, [**Adding Interactions**](https://docs.bokeh.org/en/latest/docs/user_guide/interaction.html) in the Bokeh User Guide is a great place to start.

