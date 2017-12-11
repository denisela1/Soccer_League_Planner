Build a Soccer League 

Build a tool to help a soccer coach divide 18 players into three well-balanced teams. You'll apply your knowledge of important Python data structures like lists and dictionaries to get it done.

You have volunteered to be the Coordinator for your town’s youth soccer league. As part of your job you need to divide the 18 children who have signed up for the league into three even teams - Dragons, Sharks and Raptors. In years past, the teams have been unevenly matched, so this year you are doing your best to fix that. For each child, you will have the following information: Name, height (in inches), whether or not they have played soccer before, and their guardians’ names. You'll take a list of these children, divide them into teams and output a text file listing the three teams and the players on them. There are three main tasks you'll need to complete to get this done:

In your Python program, read the data from the supplied CSV file. Store that data in an appropriate data type so that it can be used in the next task.

Create logic that can iterate through all 18 players and assign them to teams such that each team has the same number of players. The number of experienced players on each team should also be the same.

Finally, the program should output a text file named -- teams.txt -- that contains the league roster listing the team name, and each player on the team including the player's information: name, whether they've played soccer before and their guardians' names.

Create a script named league_builder.py.
Make sure the script doesn't execute when imported; put all of your logic and function calls inside of an if __name__ == "__main__": block.

Create variables and programming logic to divide the 18 players into three teams: Sharks, Dragons and Raptors. Make sure the teams have the same number of players on them, and that the experience players are divided equally across the three teams.

Create a text file named teams.txt that includes the name of a team, followed by the players on that team. List all three teams and their players.

In the list of teams, include the team name on one line, followed by a separate line for each player. Include the player's name, whether the player has experience playing soccer, and the player's guardian names. Separate each bit of player information by a comma. For example, the text file might start something like this:

Sharks
Frank Jones, YES, Jim and Jan Jones
Sarah Palmer, YES, Robin and Sari Washington
Joe Smith, NO, Bob and Jamie Smith
