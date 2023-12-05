# direct import
import game.Level.start
game.Level.start.selectdifficulty(2)

# import without a package prefix
#   - when done this way the construct
#     of calling an objectis lesser
from game.Level import start

start.selectdifficulty(2)

# import required functionality only
#   - benefit of calling the object directly
from game.Level.start import selectdifficulty

selectdifficulty(2)