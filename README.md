 <!DOCTYPE html>
<html>
<head>
<title>README.MD</title>
</head>
<body>

<h1>Spelling Challange Game</h1>

<img src="assets/images/website-mockup-image.jpg" alt="An-image-of-game-across-multiple-screens">
<p></p>

<h2><u>Features</u></h2>
<h3>Existing Features</h3>
<h2><u>Design</u></h2>

<img src="assets/images/flow-chart-1.jpg" alt="An-image-of-the-spelling-challange-flowchart">

<img src="assets/images/flow-chart-2.jpg" alt="A-second-image-of-the-spelling-challange-flowchart">


<h2><u>Technologies</u></h2>
<h2><u>Testing</u></h2>

<img src="assets/images/code-validated-image.jpg" alt="An-image-of-the-CI-Python-Linter">

<h2><u>Bugs</u></h2>
<h3>This section will document the bugs found in the 'Spelling Challange' code and how they were resolved<h3>
<img src="assets/images/list-bug.jpg" alt="An-image-of-bug-causing-multiple-prints">
<br>
<br>
<b>Issue:</b>
<p>In order for the ‘Spelling Challenge’ to successfully work, the player’s guesses must be added and then compared to the answer (SecretWord). This code was not working as testing proved that a bug was stopping the player’s score from being compared to the answer. </p>
<br>
<b>Resolution:</b>
<p>The solution came along with the realisation that the current code was comparing a string to a list. Once the len() method was implemented on both the ‘correct’ list and the ‘secretWord’ string, the two could be successfully compared.</p>
<br>
<img src="assets/images/multi-line-bug.jpg" alt="An-image-of-bug-causing-multiple-prints">
<br>
<br>
<b>Issue:</b>
<p>I discovered a bug in my code that resulted in print statements being printed multiple times in the terminal. This bug was attached to the code in the while loop that checks if the player’s guesses matches the answer. </p>
<br>
<b>Resolution:</b>
<p>I resolved this bug by researching online. I eventually found some information of Stack Overflow on the nature of while loops.The bug was caused by the loop repeating because it didn’t have a break. I inserted two breaks into the while loop and the issue was resolved.</p>
<br>
<img src="assets/images/restart-bug.jpg" alt="An-image-of-bug-causing-multiple-prints">
<br>
<br>
<b>Issue:</b>
<p>I previously had code in place at the bottom of my 'while fail_Count >:0' code to restart the game (play_Again) when the player click ‘y’ for yes. The issue was that I didn’t work. The player could click on ‘y’ but it wouldn’t restart the game. Instead, the guesses from the player’s last game would carry over, leaving them with very little (if any) guesses to try and solve the game. </p>
<br>
<p>Original code:</p>
<img src="assets/images/original-play-again-f.jpg" alt="An-image-of-bug-causing-restart-fail">
<br>
<br>
<b>Resolution:</b>
<p>I went to tutor support for help investigating the issue. The tutor pointed out that part of the issue was that the ‘correct’ and ‘incorrect’ lists were not emptying when the game the game ended, because of this, the guesses from the last game were still counted. I added ‘correct = []’ and ‘incorrect = [ ]’ to the end of the restart function to reset the lists. That solved part of the issue. In the end, I opted to add a main() function to all the game code so it would restart when ‘y’ was selected by the player. </p>




<h2><u>Credits</u></h2>
<h2><u>Deployment</u></h2>
<h2><u>Acknowledgments</u><h2>


<p>This is a paragraph.</p>

</body>
</html> 


