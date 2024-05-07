# sqlalchemy-challenge
Utilized Xpert learning for histogram legend: plt.legend(["tobs"], loc="upper right") 
~Reread the instruction to see I didn't actually need that line of code~
looked up a way(stack overflow) to read some results better by making a dictionary to present findings in one line. Though I wasnt eble to cleanly do it with the last ones.

Had some help from Tutor Justin with the <start>/<end> of the project, He helped explain what the "<>" did.
He also gave me a suggestion(if I wanted to learn more) on how to use html/css in flask, which I use to make it a little nicer. I already was using links(I prefer new tabs)

I added a default date range for start/end so the page doesn't default in "null" and the input format would be simple to understand and change.

Was going to use return jsonify(f"Min:{results[0]}, Max:{results[1]}, Avg:{results[2]}") to have it look cleaner, but it didn't look the same as other jsonify results.
