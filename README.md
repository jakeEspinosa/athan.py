<h1>Athan Speaker</h1>

<h2><a href="https://jakeespinosa.github.io/athan-frontend/">Generate your API call string here!</a></h2>

<h2>Description</h2>
<p>
  Turn any bluetooth speaker into an <a href="https://studioarabiya.com/blog/muslim-world/what-does-athan-mean-in-islam">athan</a> speaker and enjoy the blessings of having the call to prayer played in your home! This project consists of 2 Python scripts, a React front-end to generate the API call string with ease, a <a href="https://soundcloud.com/bilalahmadofcl/most-beautiful-azan-adhan-no-copyright-free-islamic-background">copyright-free athan .mp3 file</a>, and a silent .mp3 file to keep the speaker turned on. Running this on a Raspberry Pi connected to a bluetooth speaker will provide the best experience.
</p>

<h3>How it Works</h3>
<b>1.)</b> The athan.py script (script for sake of brevity) gets the current date and time and adds it to the API call string.<br />
<b>2.)</b> The script calls the Al Adan API, gets the current prayer times for the day, and logs that it did so.<br />
<b>3.)</b> The script then sets a refresh time for a little under 24 hours after Fajr (the morning prayer).<br />
<b>4.)</b> The script compares the prayer times to the current time. If the prayer time and current time match, it plays the athan and logs that it played it.<br />
<b>5.)</b> Once the refresh time comes, the script refreshes the prayer times.<br />
<b>6.)</b> The script then repeats steps 4 and 5.

<h2>How to Use</h2>
<b>1.)</b> Install all dependencies from below using pip.<br />
<b>2.)</b> Clone the repo to your local machine.<br />
<b>3.)</b> <a href="https://jakeespinosa.github.io/athan-frontend/">Generate your API call string.</a><br />
<b>4.)</b> Paste the API call string into the athan.py file (there is a comment designating where).<br />
<b>5.)</b> Run the athan.py script.<br />
<b>6.)</b> If your speaker auto powers off, then run the stayAlive.py script in the stayAlive directory. If not, feel free to delete it.<br />
<b>7.)</b> Check the log.txt file created in the cloned repo and make sure it worked. It should say "Refreshed prayer times at...".

<h2>Languages/Technologies Used</h2>

 - <b>Python (script)</b>: fetch and play athan at prayer times
 - <b>TypeScript and React.js (optional front-end)</b>: user interface to generate API call string
 - <b>Al Adan Prayer Times API (third-party backend)</b>: fetch and update prayer times
 - <b>GitHub Pages</b>: static web host

<h2>Dependencies</h2>

- requests
- playsound
- iso8601
- pydub (if using stayAlive script)
