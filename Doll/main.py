# 
# from registration import registration
# registration()
# doll.registration("eliza", 17)
# doll = Doll()
# doll.registration("eliza", 17)
# from registration import Doll

from registration import Doll


test = Doll("Белоснежный", "черный", 20, "черный", "большие" )
test.registration("eliza", 17)
# doll.info()


from skin import choice
from hair import hair
from height import heightt
from eye import eye
from lips import lips


def main():
    skin = choice()
    hair_color = hair()
    height = heightt()
    eyes_color = eye()
    lip = lips()

    doll = Doll(skin=skin, hair_color=hair_color, height=height, eyes_color=eyes_color, lip=lip )
    doll.registration("eliza", 17)
    doll.info()

main()