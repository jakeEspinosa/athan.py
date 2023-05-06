<h1>Athan Speaker</h1>

<h2><a href="https://jakeespinosa.github.io/athan-frontend/">Generate your API call string here!</a></h2>

<h2>Description</h2>
<p>
  Turn any bluetooth speaker into an <a href="https://studioarabiya.com/blog/muslim-world/what-does-athan-mean-in-islam">athan</a> speaker and enjoy the blessings of having the call to prayer played in your home! This project consists of 2 Python scripts, a React front-end to generate the API call string with ease, a <a href="https://soundcloud.com/bilalahmadofcl/most-beautiful-azan-adhan-no-copyright-free-islamic-background">copyright-free athan .mp3 file</a>, and a silent .mp3 file to keep the speaker turned on.
</p>

<h3>How it Works</h3>
<b>1.)</b> The athan.py script (script for sake of brevity) gets the current date and time and adds it to the API call string.<br />
<b>2.)</b> The script calls the Al Adan API, gets the current prayer times for the day, and logs that it did so.<br />
<b>3.)</b> The script then sets a refresh time for a little under 24 hours after Fajr (the morning prayer).<br />
<b>4.)</b> The script compares the prayer times to the current time. If the prayer time and current time match, it plays the athan and logs that it played it.<br />
<b>5.)</b> Once the refresh time comes, the script refreshes the prayer times.
<b>6.)</b> The script then repeats steps 5 and 6.

<h2>How to Use</h2>

<h2>Languages/Technologies Used</h2>

 - <b>Python (script)</b>: fetch prayer times and play athan at prayer times
 - <b>React.js (optional front-end)</b>: user interface to generate API call string
 - <b>Al Adan Prayer Times API (third-party backend)</b>: fetch and update prayer times
 - <b>GitHub Pages</b>: static web host
