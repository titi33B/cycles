from ftplib import all_errors
from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 
class MoveActorsAction(Action):

   def execute(self, cast, script):
    all_cast = cast.get_all_actors()

    for i in range(len(all_cast)):
        all_cast[i].move_next()

        
# Override the execute(cast, script) method as follows:
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor