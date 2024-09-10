import chess
import io

class Opening:
    def __init__ (self, name, moves):
        self.name = name
        self.children = []
        move_arr = moves.split()
        self.moves = move_arr
        self.level = len(move_arr)


    def addChild(self, child):
        self.children.append(child)


def readNodes():
    openings = []
    with open("openings.txt", "r") as f:
        name = ""
        moves = ""
        while True:
            for i in range(2):
                line = f.readline()
                if (line == ""):
                    return openings

                if (i == 0):
                    name = line
                elif (i == 1):
                    moves = line
            openings.append(Opening(name, moves))
    




if __name__ == "__main__":
    openings = readNodes()

    for node in openings:
        print("****************")
        print(node.name)
        print(node.moves)
        print("****************")
