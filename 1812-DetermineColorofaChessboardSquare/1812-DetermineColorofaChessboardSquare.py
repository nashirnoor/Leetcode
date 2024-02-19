class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        black = "aceg"
        white = "bdfh"
        if coordinates[0] in black and int(coordinates[1]) % 2 == 1:
            return False
        elif coordinates[0] in white and int(coordinates[1]) % 2 == 0:
            return False
        else:
            return True
        
"
