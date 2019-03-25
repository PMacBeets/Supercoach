
import Const
import DataContainer
import ScTeam

THISYEAR = 2019



# --------- Function ---------- #

def add_all_teams(data: DataContainer):
    for key in Const.positions:
        data.add_team(key)

# --------- Main ---------- #

my_scteam = ScTeam.ScTeam("OOORRazziooOOO")

my_scteam.read_in_sc_team()

# update byes
# update averages




