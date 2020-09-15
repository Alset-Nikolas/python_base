from pprint import pprint

from bowling import GetScore
from bowling_NEW import NewGetScore


class Processing:

    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.all_player = {}
        self.res = []

    def run(self):
        self.parsing_input_file()
        self.pprint()
        print("\t\t\t\t\tГотово!")

    def parsing_input_file(self):
        with open(self.input_file, encoding='UTF-8') as f:
            tour = []
            for line in f:
                if "winner is " in line:
                    self.tour_handling(tour)
                    tour = []


                else:
                    tour.append(line)

    def tour_handling(self, tour):
        tour_new=[0]*(len(tour)+1)
        tour_new[0]=tour[0][:-1]

        for i,line in enumerate(tour[1:]):
            result_player=line.split()[1]
            if "### Tour" in line:
                tour_new[i + 1] = tour[i+1][:-1]
            else:
                try:
                    result_player_numeral = GetScore(result_player).get_score()
                    self.add_matr(line.split())
                except Exception as er:
                    result_player_numeral = str(er)

                tour_new[i+1]=(line[:-2] + "\t" + str(result_player_numeral))
        winner_name = self.determine_the_winner(tour_new);
        self.add_matr_winner(winner_name)
        tour_new[-1] = "winner is "+winner_name
        self.parsing_output_file(tour_new)

    def add_matr(self, data):
        if data[0] not in self.all_player:
            self.all_player[data[0]] = [1,0]
        else:
            self.all_player[data[0]][0] += 1

    def add_matr_winner(self, name):
        if name != 'Никто':
            self.all_player[name][1] +=1

    def determine_the_winner(self, tour_new):
        winner_name = 'Никто'
        winner_res = '0'
        for line in tour_new[1:-1]:
            line_split = line.split()
            if line_split[0] == "###":
                continue
            if line_split[2].isdigit():
                if int(line_split[2]) > int(winner_res):
                    winner_res = line_split[2]
                    winner_name = line_split[0]
        return winner_name


    def parsing_output_file(self, tour_new):
        with open(self.output_file, encoding='UTF-8', mode='a') as f:
            for line in tour_new:
                f.write(line+'\n')

    def _convert_to_list(self):

        for v,a in self.all_player.items():
            self.res.append([v,a[0], a[1]])



    def pprint(self):
        '''
        # +----------+------------------+--------------+
        # | Игрок    |  сыграно матчей  |  всего побед |
        # +----------+------------------+--------------+
        # | Татьяна  |        99        |      23      |
        # ...
        # | Алексей  |        20        |       5      |
        # +----------+------------------+--------------+
        '''
        print("+------------+--------------------+--------------+")
        print("|   Игрок    |  сыграно матчей    |  всего побед |")
        print("+------------+--------------------+--------------+")
        self._convert_to_list()
        for line in self.res:
            print(f'| {line[0]:^10} | {line[1]:^18} | {line[2]:^12} |')
            print("+------------+--------------------+--------------+")


class NewProcessing(Processing):
    def tour_handling(self, tour):
        tour_new=[0]*(len(tour)+1)
        tour_new[0]=tour[0][:-1]

        for i,line in enumerate(tour[1:]):
            result_player=line.split()[1]
            if "### Tour" in line:
                tour_new[i + 1] = tour[i+1][:-1]
            else:
                try:
                    result_player_numeral = NewGetScore(result_player).get_score()
                    self.add_matr(line.split())
                except Exception as er:
                    result_player_numeral = str(er)

                tour_new[i+1]=(line[:-2] + "\t" + str(result_player_numeral))
        winner_name = self.determine_the_winner(tour_new);
        self.add_matr_winner(winner_name)
        tour_new[-1] = "winner is "+winner_name
        self.parsing_output_file(tour_new)

if __name__ == "__main__":
    A = Processing(input_file="tournament.txt",
                   output_file="tournament_result.txt")

    A.run()