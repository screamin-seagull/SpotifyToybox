from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px
import SpotifyToybox as st
from datetime import datetime

app = Flask(__name__)

test_file = "combined.json"
testbox = st.SpotifyToybox(test_file)


@app.route("/", methods=["GET", "POST"])
def data_vis():
    artists, times = [], []
    if request.method == 'GET':
        test_times = testbox.top_artists_time(False, 10)
        for time in test_times:
            print(time, test_times[time])
            artists.append(time)
            times.append(test_times[time]/60000)
        print(artists, times)
    elif request.method == 'POST':
        toy_file = request.form.get('filename')
        toybox = st.SpotifyToybox(toy_file)
        toybox_times = toybox.top_artists_time(False, 10)
        for time in toybox_times:
            print(time, toybox_times[time])
            artists.append(time)
            times.append(toybox_times[time]/60000)
        print(artists, times)
    df = pd.DataFrame({
        'Artist': artists,
        'Time': times
    })
    fig = px.bar(df, x='Artist', y='Time', color='Artist', width=len(artists) * 100, height=600)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("datavis.html", graphJSON=graphJSON)


if __name__ == "__main__":
    app.run()
