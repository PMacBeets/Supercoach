import Const
import Player
import xlrd


class ScTeam():
    def __init__(self, name: str):
        self.name = name
        self.year = None
        self.round = None
        self.players_dict = {
            Const.positions[0]: [],     # Defender
            Const.positions[1]: [],     # Midfield
            Const.positions[2]: [],     # Ruck
            Const.positions[3]: []      # Forward
        }

    def name_team(self, name: str):
        self.name = name

    def check_add_player(self, pos_in: str, fullname: str, team: str):
        name = fullname.split(" ", 1)

        # If there is space for the player
        if len(self.players_dict[pos_in]) < Const.pos_num_dict[pos_in][1]:

            tmp_player = Player.Player(name[0],name[1], team)
            print(tmp_player)
            self.players_dict[pos_in].append(tmp_player)

        else:
            print("TOO MANY PLAYERS")
            exit(1)

    def read_in_sc_team(self):
        wb = xlrd.open_workbook(Const.FILENAME)
        Team = wb.sheet_by_name("Team")
        j = 0;
        pos_in = None
        for i in range(Team.nrows):
            if str(Team.cell_value(i, 0)) != "":
                pos_in = str(Team.cell_value(i, 0))
                j += 1
                i += 1
            else:
                self.check_add_player(pos_in, Team.cell_value(i, 1), Team.cell_value(i, 2))
        # Read In Watchlist
