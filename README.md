 <!DOCTYPE html>
<html>
<head>
<title>README.MD</title>
</head>
<body>

<h1>Spelling Challange Game</h1>
<br>
<img src="assets/images/website-mockup-image.jpg" alt="An-image-of-game-across-multiple-screens">
<br>
<p>Welcome to Spelling Challange! Spelling Challenge was built for children between 8 – 11 to test their long vocabulary skills. This game was constructed using only python. Spelling Challenge allows kids to guess a letter of a random word. Each word is ten letters long. Because this is a game based around learning to spell, a player gets to have 7 wrong guesses during a single game. If they guess the word before running out of chances, they win! If not, they can restart the game and try again. It’s all about the effort!</p>

<a href="https://spelling-challange.herokuapp.com/">Link to live Spelling Challange Game</a> 

<h2><u>Features</u></h2>
<br>
<b>Welcome</b>
<br>
<img src="assets/images/welcome-feature.jpg" alt="An-image-of-the-welcome-feature">
<br>
<p>The welcome feature welcomes the player to the game, asked for their name and greets the user by their name.</p>
<br>
<b>Enter Age</b>
<br>
<img src="assets/images/age-feature.jpg" alt="An-image-of-the-age-feature">
<br>
<p>The age feature asks the player their age, if they are between 8-11, the game proceeds. If they are not between 8-11, the terminal prints the game's age recommendation.</p>
<br>
<b>Correct/Incorrect</b>
<br>
<img src="assets/images/validation-feature.jpg" alt="An-image-of-the-guess-validator-feature">
<br>
<p>The Correct/Incorrect tells the player if their guess was correct or incorrect. If correct, their guess is added to a list in the terminal</p>
<br>





<h2><u>Design</u></h2>

<img src="assets/images/flow-chart-1.jpg" alt="An-image-of-the-spelling-challange-flowchart">

<img src="assets/images/flow-chart-2.jpg" alt="A-second-image-of-the-spelling-challange-flowchart">


<h2><u>Technologies</u></h2>
<h2><u>Testing</u></h2>

<img src="assets/images/code-validated-image.jpg" alt="An-image-of-the-CI-Python-Linter">

<h2><u>Bugs</u></h2>
<img src="assets/images/list-bug.jpg" alt="An-image-of-list-bug">
<br>
<br>
<b>Issue:</b>
<br>
<p>In order for the ‘Spelling Challenge’ to successfully work, the player’s guesses must be added and then compared to the answer (SecretWord). This code was not working as testing proved that a bug was stopping the player’s score from being compared to the answer. </p>
<br>
<b>Resolution:</b>
<br>
<p>The solution came along with the realisation that the current code was comparing a string to a list. Once the len() method was implemented on both the ‘correct’ list and the ‘secretWord’ string, the two could be successfully compared.</p>
<br>
<img src="assets/images/multi-line-bug.jpg" alt="An-image-of-bug-causing-multiple-prints">
<br>
<br>
<b>Issue:</b>
<br>
<p>I discovered a bug in my code that resulted in print statements being printed multiple times in the terminal. This bug was attached to the code in the while loop that checks if the player’s guesses matches the answer. </p>
<br>
<b>Resolution:</b>
<br>
<p>I resolved this bug by researching online. I eventually found some information of Stack Overflow on the nature of while loops.The bug was caused by the loop repeating because it didn’t have a break. I inserted two breaks into the while loop and the issue was resolved.</p>
<br>
<img src="assets/images/restart-bug.jpg" alt="An-image-of-bug-causing-multiple-prints">
<br>
<br>
<b>Issue:</b>
<br>
<p>I previously had code in place at the bottom of my 'while fail_Count >:0' code to restart the game (play_Again) when the player click ‘y’ for yes. The issue was that I didn’t work. The player could click on ‘y’ but it wouldn’t restart the game. Instead, the guesses from the player’s last game would carry over, leaving them with very little (if any) guesses to try and solve the game. </p>
<br>
<p>Original code:</p>
<img src="assets/images/original-play-again-f.jpg" alt="An-image-of-bug-causing-restart-fail">
<br>
<br>
<b>Resolution:</b>
<br>
<p>I went to tutor support for help investigating the issue. The tutor pointed out that part of the issue was that the ‘correct’ and ‘incorrect’ lists were not emptying when the game the game ended, because of this, the guesses from the last game were still counted. I added ‘correct = []’ and ‘incorrect = [ ]’ to the end of the restart function to reset the lists. That solved part of the issue. In the end, I opted to add a main() function to all the game code so it would restart when ‘y’ was selected by the player. </p>
<br>
<br>
<h2><u>Unresolved Bugs</u></h2>
<img src="assets/images/unresolved-bug.jpg" alt="An-image-of-unresolved-bug">
<br>
<br>
<b>Issue:</b>
<br>
<p>The guesses that the player has submitted prints on the same line as the restart question. I have attempted to resolve this bug by putting a line of print(‘-------------------‘) underneath the print statement that fills in the letters that have been guessed but it has been unsuccessful.</p>
<br>
<h2><u>Credits</u></h2>
<a href="/about/about_team.htm">team</a>
<h2><u>Deployment</u></h2>
<h2><u>Acknowledgments</u><h2>


<p>This is a paragraph.</p>

</body>
</html> 


