from flask import Flask, render_template
import pandas as pd
import json
import plotly
import plotly.express as px
import SpotifyToybox as st
from datetime import datetime

app = Flask(__name__)

test_file = "combined.json"
testbox = st.SpotifyToybox(test_file)


@app.route("/")
def data_vis():
    artists, times = [], []
    test_times = testbox.top_artists_time(False, 10)
    for time in test_times:
        print(time, test_times[time])
        artists.append(time)
        times.append(test_times[time]/6000)
    print(artists, times)

    df = pd.DataFrame({
        'Artist': artists,
        'Time': times
    })

    fig = px.bar(df, x='Artist', y='Time', color='Artist', width=len(artists)*100, height=600)

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template("datavis.html", graphJSON=graphJSON)


if __name__ == "__main__":
    app.run()
