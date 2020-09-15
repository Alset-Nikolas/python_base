from bowling import GetScore

class NewGetScore(GetScore):
    def get_score(self):
        self.check_param()
        result = 0
        i = 0
        while i <= len(self.game_result) - 1:
            if self.game_result[i] == 'X':
                result += 10

                result+=self.extra_points(i)
                i-=1
            elif self.game_result[i].isdigit() and self.game_result[i + 1].isdigit():
                result += int(self.game_result[i]) + int(self.game_result[i + 1])
            elif self.game_result[i + 1] == '/':
                result += 10
                result += self.extra_points_spare(i+1)
            elif self.game_result[i] == '-' and self.game_result[i + 1].isdigit():
                result += int(self.game_result[i + 1])
            elif self.game_result[i + 1] == '-' and self.game_result[i].isdigit():
                result += int(self.game_result[i])
            elif self.game_result[i + 1] == '-' and self.game_result[i] == '-':
                result += 0
            i += 2
        return result
    def extra_points_spare(self, index):
        result = 0
        if len(self.game_result[index:]) > 1:
            if self.game_result[index+1] == 'X':
                result += 10
            elif self.game_result[index+1].isdigit():
                result += int(self.game_result[index+1])

            elif self.game_result[index+1] == '-':
                result += 0
            else:
                print('я сломался')
        return result

    def extra_points(self, index):

        result=0
        if len(self.game_result[index:]) > 2:

            if self.game_result[index+1] == 'X':
                result += 10
            elif self.game_result[index+1].isdigit() and self.game_result[index+2].isdigit():
                result += int(self.game_result[index+1]) + int(self.game_result[index+2])
            elif self.game_result[index+2] == '/':
                result += 15
            elif self.game_result[index+1] == '-' and self.game_result[index+2].isdigit():
                result += int(self.game_result[index+1])
            elif self.game_result[index+1] == '-' and self.game_result[index+2].isdigit():
                result += int(self.game_result[index+2])
            elif self.game_result[index+2] == '-' and self.game_result[index+1] == '-':
                result += 0

            if self.game_result[index+2] == 'X':
                result += 10
            elif self.game_result[index+2] == '-':
                result += 0
            elif self.game_result[index+2].isdigit() and not self.game_result[index+1].isdigit():
                result += int(self.game_result[index+2])

        elif len(self.game_result[index:])==2:

            if self.game_result[index+1] == 'X':
                result += 10


        return result


if __name__ == '__main__':
    print('811/X--3/XX17XX')
    A = NewGetScore('811/X--3/XX17XX')
    print(A.get_score())
