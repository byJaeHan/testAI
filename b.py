from datetime import datetime, timedelta
import random

import plotly.graph_objects as go
import plotly.express as px

import pandas as pd
import numpy as np

np.random.seed(1)

N = 100

df = pd.DataFrame(dict(x=np.random.randn(N),
                       y=np.random.randn(N)))


now = datetime(2021, 1, 1, 0, 0, 0)
times = []
for _ in range(N):
    times.append(now)
    now += timedelta(minutes=1)

df['choice'] = [random.choice(['a', 'b', 'c', 'd']) for _ in range(N)]
df['date'] = times

# Create figure
fig = go.Figure()

fig.add_trace(
    go.Scattergl(x=df.date, y=df.x,
                 mode='markers+lines',
                 # marker=dict(
                 #     line=dict(
                 #         width=1,
                 #         color='DarkSlateGrey'
                 #     )
                 # ),
                 # line=dict(
                 #     width=1
                 # )
    )
)

buttons = []

# button with one option for each dataframe
for selected in df.choice.unique():
    a = df.loc[df.choice == selected, 'x']
    b = df.loc[df.choice == selected, 'date']
    buttons.append(dict(method='restyle',
                        label=selected,
                        visible=True,
                        args=[{'x': [df.loc[df.choice == selected, 'date']],
                               'y': [df.loc[df.choice == selected, 'x']]}],
                        )
                  )

# Add dropdown
fig.update_layout(
    showlegend=False,
    updatemenus=[
        dict(
            buttons=buttons,
            direction="down",
            showactive=True,
        ),
    ]
)



# Set title
fig.update_layout(
    title_text="Time series with range slider and selectors"
)

fig.update_layout(
    xaxis=dict(
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

# initial_range = [
#     '2021-01-01', '2021-01-02'
# ]
#
# fig['layout']['xaxis'].update(range=initial_range)
fig.show()
# fig.write_html("file.html")