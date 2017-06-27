import csv
#global variables for teams:
sharks = []
dragons = []
raptors = []

#read the csv file with the player info and create a player dictionary:
def read_players():
    player_reader = csv.reader(open('soccer_players.csv'))
    player_dictionary = {}
    for row in player_reader:
        key = row[0]
        player_dictionary[key] = row[1:]
#deleting the first row with column titles:
    del player_dictionary['Name']
    return player_dictionary

#distribute kids based on experience:
def experienced_players():
    exp_kids = []
#calling the previous function to use the player dictionary:
    player_list = read_players()
    for keys, values in player_list.items():
        if values[1] == "YES":
            exp_kids.append(keys)
    return exp_kids

def inexperienced_players():
    inexp_kids = []
#calling the previous function to use the player dictionary:
    player_list = read_players()
    for keys, values in player_list.items():
        if values[1] == "NO":
            inexp_kids.append(keys)
    return inexp_kids

#finalize teams:
def make_teams():
#calling a previous function to generate 2 separate lists for experienced and inexperienced kids:
    ek = experienced_players()
    iek = inexperienced_players()
    sharks.extend(ek[0:3])
    sharks.extend(iek[0:3])
    dragons.extend(ek[3:6])
    dragons.extend(iek[3:6])
    raptors.extend(ek[6:9])
    raptors.extend(iek[6:9])
    return sharks, dragons, raptors

#update the player dictionary to include the assigned teams:
def final_league():
#calling the function to create a player dictionary
    letter_info = read_players()
    for keys, values in letter_info.items():
        if keys in sharks:
            values.append("Sharks")
        if keys in dragons:
            values.append("Dragons")
        if keys in raptors:
            values.append("Raptors")
    return letter_info

#write the league info into the text file:
def create_textfile():
    files = final_league()
    with open("teams.txt", "w") as textfile:
        textfile.write("Sharks" + "\n")
        for keys,values in files.items():
            if values[3] == "Sharks":
                textfile.write(str(keys) + ", " + str(values[1]) + ", " + str(values[2]) + "\n")
        textfile.write("\n")
        textfile.write("Dragons" + "\n")
        for keys, values in files.items():
            if values[3] == "Dragons":
                textfile.write(str(keys) + ", " + str(values[1]) + ", " + str(values[2]) + "\n")
        textfile.write("\n")
        textfile.write("Raptors" + "\n")
        for keys, values in files.items():
            if values[3] == "Raptors":
                textfile.write(str(keys) + ", " + str(values[1]) + ", " + str(values[2]) + "\n")
        textfile.write("\n")

#generate letters to send the guardians:
def letter_generator():
    letters = final_league()
    for keys, values in letters.items():
        if values[3] == "Sharks":
            practice_start = '8am'
        if values[3] == "Dragons":
            practice_start = '9am'
        if values[3] == "Raptors":
            practice_start = '10am'
    for keys, values in letters.items():
        letter = ("Dear {},\n"
            "Congratulations! Your child, {}, is selected to play on the {} team. "
            "The first practice is at {} next Saturday, July 1st."
            "Thanks,\n"
            "Coach Deniz".format(values[2],keys,values[3],practice_start))
        with open("{}.txt".format((keys.lower()).replace(" ", "_")), "w") as textfile:
            textfile.write(letter)


if __name__ == "__main__":
    read_players()
    experienced_players()
    inexperienced_players()
    make_teams()
    create_textfile()
    final_league()
    letter_generator()
