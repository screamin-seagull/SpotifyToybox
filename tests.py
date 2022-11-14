import SpotifyToybox as st
from datetime import datetime

test_file = "JSON Files/endsong_0.json"

testbox = st.SpotifyToybox(test_file)
print(testbox.stream_time(), testbox.stream_time(True),
      testbox.stream_time(False, True), testbox.stream_time(True, True))

start = datetime.strptime("01/01/2021", '%m/%d/%Y').date()
end = datetime.strptime("12/31/2021", '%m/%d/%Y').date()
test_times = testbox.artist_times(True, True, True, start, end)
for time in test_times:
    print(time, test_times[time])

test_streams = testbox.artist_streams(True, True)
for streams in test_streams:
    print(streams, test_streams[streams])

top5_streams = testbox.top_artists_streams()
for i in top5_streams:
    print(i, top5_streams[i])
top5 = testbox.top_artists_time(True)
for i in top5:
    print(i, top5[i])
