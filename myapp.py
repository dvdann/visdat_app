#!/usr/bin/env python
# coding: utf-8

# In[26]:


# Data handling
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Bokeh libraries
from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource


# In[27]:


df = pd.read_csv(./stock_market.csv")
print('Data downloaded and read into a dataframe!')
df.head()


# In[28]:


# Create a ColumnDataSource
df = ColumnDataSource(df)


# In[29]:


# Create views for each saham
Nikkei = CDSView(source=df,
                       filters=[GroupFilter(column_name='Name', group='NIKKEI')])
Hang_Seng = CDSView(source=df,
                       filters=[GroupFilter(column_name='Name', group='HANG SENG')])
Nasdaq = CDSView(source=df,
                       filters=[GroupFilter(column_name='Name', group='NASDAQ')])


# In[30]:


# Create and configure the figure
sm_fig1 = figure(plot_height=600, plot_width=1000, title='Adj Close', x_axis_label='index', y_axis_label='Adj Close')
sm_fig2 = figure(plot_height=600, plot_width=1000, title='Day_Perc_Change', x_axis_label='index', y_axis_label='Adj Close')
sm_fig3 = figure(plot_height=600, plot_width=1000, title='Volume', x_axis_label='index', y_axis_label='Adj Close')

sm_fig1.circle('index', 'Adj Close', source=df, view=Nikkei, color='#00FFFF', legend='Nikkei', muted_alpha=0.1)
sm_fig1.square('index', 'Adj Close',source=df, view=Hang_Seng, color='#7FFF00', legend='Hang_Seng', muted_alpha=0.1)
sm_fig1.triangle('index', 'Adj Close', source=df, view=Nasdaq, color='#CE1141', legend='Nasdaq',muted_alpha=0.1)

sm_fig2.circle('index', 'Volume', source=df, view=Nikkei,  color='#00FFFF', legend='Nikkei', muted_alpha=0.1)
sm_fig2.square('index', 'Volume', source=df, view=Hang_Seng, color='#7FFF00', legend='Hang_Seng', muted_alpha=0.1)
sm_fig2.triangle('index', 'Volume', source=df, view=Nasdaq, color='#CE1141', legend='Nasdaq',muted_alpha=0.1)

sm_fig3.circle('index', 'Day_Perc_Change', source=df, view=Nikkei, color='#00FFFF', legend='Nikkei', muted_alpha=0.1)
sm_fig3.square('index', 'Day_Perc_Change', source=df, view=Hang_Seng, color='#7FFF00', legend='Hang_Seng', muted_alpha=0.1)
sm_fig3.triangle('index', 'Day_Perc_Change', source=df, view=Nasdaq, color='#CE1141', legend='Nasdaq',muted_alpha=0.1)


# In[31]:


# Increase the plot widths
sm_fig1.plot_width = sm_fig2.plot_width = sm_fig3.plot_width = 1000

# Create three panels, one for each conference
tab1 = Panel(child = sm_fig1, title = 'Adj Close')
tab2 = Panel(child = sm_fig2, title = 'Volume')
tab3 = Panel(child = sm_fig3, title = 'Day Perc Change')

# Assign the panels to Tabs
Table = Tabs(tabs = [tab1,tab2,tab3])
output_file('Table.html')


# In[32]:


AdjClose  = True #@param {type:"boolean"}
Volume = True #@param {type:"boolean"}
Day_Per_Change = True #@param {type:"boolean"}


# In[33]:


# Format the tooltip
tooltips = [
            ('Name','@Name'),
            ('Adj Close', '@{Adj Close}{0,0.000}'),
            ('Volume', '@Volume'),
            ('Day_Perc_Change','@Day_Perc_Change{0,0.000}'),
           ]

# Add the HoverTool to the figure
sm_fig1.add_tools(HoverTool(tooltips=tooltips))
sm_fig2.add_tools(HoverTool(tooltips=tooltips))
sm_fig3.add_tools(HoverTool(tooltips=tooltips))


# In[34]:


sm_fig1.legend.click_policy = 'mute'
sm_fig2.legend.click_policy = 'mute'
sm_fig3.legend.click_policy = 'mute'
show(Table)


# In[ ]:




