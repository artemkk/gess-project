# Author: Artem Kuryachy
# Date: 05/14/2020
# Description: Portfolio Project Gess Game. Mix of Go and Chess. Turn-based, 2 players.


class GessGame:
    """
    Gess Game class that serves to do the following:
    - Track turns
    - Display game board
    - Allow player to make move based on piece selection and new footprint selection
    - Allow player to resign
    - Display game state
    It does not communicate with other classes as there is no use of composition or inheritance.
    """

    def __init__(self):
        """
        Initialization method containing class data attributes:
        :var self._board - Game board that is altered through make_move() method by the players
        :var self._ring_board - Unseen game board utilized to track number of rings on game board when move is made
        :var self._state - State of game initialized as "UNFINISHED" and change in game_state() method
        :var self._x_axis - Reference list of the x axis for indexing, used in make_move() and convert_to_axes()
        :var self._coord_x_old - Parsed user input of piece center x coordinate (letter coordinate) on board,
        initiated as None
        :var self._coord_x_new - Parsed user input of new footprint center x coordinate (letter coordinate) on board
        initiated as None
        :var self._coord_y_old - Parsed user input of piece center x coordinate (letter coordinate) on board
        initiated as None
        :var self._coord_y_new - Parsed user input of new footprint center y coordinate (letter coordinate) on board
        initiated as None
        :var self._footprint_old - Selected piece footprint, initiated as empty list
        :var self._footprint_new - New footprint of piece at desired location, initiated as empty list
        :var self._ring_corner_x - X-axis index of top-left corner of ring; used in check_ring() method
        :var self._ring_corner_y - Y-axis index of top-left corner of ring; used in check_ring() method
        :var self._ring_check - List used to create potential ring piece; verified if piece or not in check_ring()
        :var self._move_x - X-axis index of top-left corner of 'moving' footprint, used to check for obstructions
        :var self._move_y - Y-axis index of top-left corner of 'moving' footprint, used to check for obstructions
        :var self._footpring_move - 'Movement' footprint used to check for movement obstruction between old and new
        piece centers
        :var self._white_ring_count - Tracker for number of white rings present on game board
        :var self._black_ring_count - Tracker for number of black rings present on game board
        :var self._piece_compass - Reference list for movement orientation based on stone presence in piece
        :var self._piece - The user selected piece to be moved, initiated as empty list
        :var self._orientation - Integer used with self._piece_compass to determine whether direction of movement by
        the piece is permitted by checking stone placement in piece, initiated as None
        :var self._turn_count - Initiated as zero, used to keep track of turns and ergo which player is allowed to move
        :var self._termination_trigger - Trigger variable initialized as False used to stop make_move() method
        """
        self._board = [["a", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---",
                        "---", "---", "---", "---", "---", "---", "---"],
                       ["b", "---", "---", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---",
                        "---", "---", "---", "---", "-W-", "---", "---"],
                       ["c", "---", "-B-", "-B-", "-B-", "---", "---", "-B-", "---", "---", "---", "---", "---", "---",
                        "-W-", "---", "---", "-W-", "-W-", "-W-", "---"],
                       ["d", "---", "---", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---",
                        "---", "---", "---", "---", "-W-", "---", "---"],
                       ["e", "---", "-B-", "---", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---",
                        "---", "---", "---", "-W-", "---", "-W-", "---"],
                       ["f", "---", "---", "-B-", "---", "---", "---", "-B-", "---", "---", "---", "---", "---", "---",
                        "-W-", "---", "---", "---", "-W-", "---", "---"],
                       ["g", "---", "-B-", "---", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---",
                        "---", "---", "---", "-W-", "---", "-W-", "---"],
                       ["h", "---", "-B-", "-B-", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---",
                        "---", "---", "---", "-W-", "-W-", "-W-", "---"],
                       ["i", "---", "-B-", "-B-", "-B-", "---", "---", "-B-", "---", "---", "---", "---", "---", "---",
                        "-W-", "---", "---", "-W-", "-W-", "-W-", "---"],
                       ["j", "---", "-B-", "-B-", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---",
                        "---", "---", "---", "-W-", "-W-", "-W-", "---"],
                       ["k", "---", "-B-", "-B-", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---",
                        "---", "---", "---", "-W-", "-W-", "-W-", "---"],
                       ["l", "---", "-B-", "---", "-B-", "---", "---", "-B-", "---", "---", "---", "---", "---", "---",
                        "-W-", "---", "---", "-W-", "---", "-W-", "---"],
                       ["m", "---", "-B-", "-B-", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---",
                        "---", "---", "---", "-W-", "-W-", "-W-", "---"],
                       ["n", "---", "-B-", "---", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---",
                        "---", "---", "---", "-W-", "---", "-W-", "---"],
                       ["o", "---", "---", "-B-", "---", "---", "---", "-B-", "---", "---", "---", "---", "---", "---",
                        "-W-", "---", "---", "---", "-W-", "---", "---"],
                       ["p", "---", "-B-", "---", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---",
                        "---", "---", "---", "-W-", "---", "-W-", "---"],
                       ["q", "---", "---", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---",
                        "---", "---", "---", "---", "-W-", "---", "---"],
                       ["r", "---", "-B-", "-B-", "-B-", "---", "---", "-B-", "---", "---", "---", "---", "---", "---",
                        "-W-", "---", "---", "-W-", "-W-", "-W-", "---"],
                       ["s", "---", "---", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---",
                        "---", "---", "---", "---", "-W-", "---", "---"],
                       ["t", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---",
                        "---", "---", "---", "---", "---", "---", "---"],
                       [" ", "-1-", "-2-", "-3-", "-4-", "-5-", "-6-", "-7-", "-8-", "-9-", "-10", "-11", "-12", "-13",
                        "-14", "-15", "-16",
                        "-17", "-18", "-19", "-20"]
                       ]
        self._ring_board = [
            ["a", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---",
             "---", "---", "---", "---", "---", "---", "---"],
            ["b", "---", "---", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---",
             "---", "---", "---", "---", "-W-", "---", "---"],
            ["c", "---", "-B-", "-B-", "-B-", "---", "---", "-B-", "---", "---", "---", "---", "---", "---",
             "-W-", "---", "---", "-W-", "-W-", "-W-", "---"],
            ["d", "---", "---", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---",
             "---", "---", "---", "---", "-W-", "---", "---"],
            ["e", "---", "-B-", "---", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---",
             "---", "---", "---", "-W-", "---", "-W-", "---"],
            ["f", "---", "---", "-B-", "---", "---", "---", "-B-", "---", "---", "---", "---", "---", "---",
             "-W-", "---", "---", "---", "-W-", "---", "---"],
            ["g", "---", "-B-", "---", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---",
             "---", "---", "---", "-W-", "---", "-W-", "---"],
            ["h", "---", "-B-", "-B-", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---",
             "---", "---", "---", "-W-", "-W-", "-W-", "---"],
            ["i", "---", "-B-", "-B-", "-B-", "---", "---", "-B-", "---", "---", "---", "---", "---", "---",
             "-W-", "---", "---", "-W-", "-W-", "-W-", "---"],
            ["j", "---", "-B-", "-B-", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---",
             "---", "---", "---", "-W-", "-W-", "-W-", "---"],
            ["k", "---", "-B-", "-B-", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---",
             "---", "---", "---", "-W-", "-W-", "-W-", "---"],
            ["l", "---", "-B-", "---", "-B-", "---", "---", "-B-", "---", "---", "---", "---", "---", "---",
             "-W-", "---", "---", "-W-", "---", "-W-", "---"],
            ["m", "---", "-B-", "-B-", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---",
             "---", "---", "---", "-W-", "-W-", "-W-", "---"],
            ["n", "---", "-B-", "---", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---",
             "---", "---", "---", "-W-", "---", "-W-", "---"],
            ["o", "---", "---", "-B-", "---", "---", "---", "-B-", "---", "---", "---", "---", "---", "---",
             "-W-", "---", "---", "---", "-W-", "---", "---"],
            ["p", "---", "-B-", "---", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---",
             "---", "---", "---", "-W-", "---", "-W-", "---"],
            ["q", "---", "---", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---",
             "---", "---", "---", "---", "-W-", "---", "---"],
            ["r", "---", "-B-", "-B-", "-B-", "---", "---", "-B-", "---", "---", "---", "---", "---", "---",
             "-W-", "---", "---", "-W-", "-W-", "-W-", "---"],
            ["s", "---", "---", "-B-", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---",
             "---", "---", "---", "---", "-W-", "---", "---"],
            ["t", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---", "---",
             "---", "---", "---", "---", "---", "---", "---"],
            [" ", "-1-", "-2-", "-3-", "-4-", "-5-", "-6-", "-7-", "-8-", "-9-", "-10", "-11", "-12", "-13",
             "-14", "-15", "-16",
             "-17", "-18", "-19", "-20"]
            ]
        self._state = "UNFINISHED"
        self._x_axis = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                        "t"]
        self._coord_x_old = None
        self._coord_x_new = None
        self._coord_y_old = None
        self._coord_y_new = None
        self._ring_corner_x = None
        self._ring_corner_y = None
        self._move_x = None
        self._move_y = None
        self._white_ring_count = 1
        self._black_ring_count = 1
        self._footprint_move = []
        self._footprint_old = []
        self._footprint_new = []
        self._ring_check = []
        self._piece_compass = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
        self._piece = []
        self._orientation = None
        self._turn_count = 0
        self._termination_trigger = False

    def get_game_state(self):
        """
        Get method to return Game State
        :return: self._state
        :rtype: str
        """
        return self._state

    def get_turn_count(self):
        """
        Get method to return Turn Count
        :return: self._turn_count
        :rtype: int
        """
        return self._turn_count

    def get_piece(self):
        """
        Get method to return Piece
        :return: self._piece
        :rtype: list
        """
        return self._piece

    def get_footprint(self):
        """
        Get method to return old and new footprints
        :return: self._footprint_old
        :rtype: list
        :return: self._footprint_new
        :rtype: list
        """
        return self._footprint_old, self._footprint_new

    def get_orientation(self):
        """
        Get method to return orientation of movement
        :return: self._orientation
        :rtype: int
        """
        return self._orientation

    def get_board(self):
        """
        Get method used to return gameboard
        :return: self._board
        :rtype: Print-out of list of list
        """
        for i in self._board:
            print(' '.join(i))

    def get_ring_board(self):
        """
        Get method used to return gameboard
        :return: self._ring_board
        :rtype: Print-out of list of list
        """
        for i in self._board:
            print(' '.join(i))

    def check_state(self):
        """
        Method to verify that the game has not yet been won and making a move is allowable.
        :return: No return.
        """
        if self._state != "UNFINISHED":
            self._termination_trigger = True

    def convert_to_axes(self, centr, new_centr):
        """
        Support method for make_move() used to convert the alphanumeric inputs into indexable values for the x and y
        axis
        :param centr: str alphanumeric combination for center of piece to be moved
        :param new_centr: str alphanumeric combination for where the center of the selected piece is intended to be
        placed
        :return: No return. Incorrect input return handled in make_move() termination_trigger check.
        """
        # Deconstruct centr letter coordinate and number coordinate
        coord_old = list(str(centr))
        coord_new = list(str(new_centr))

        # Check if 1st element is letter and in bounds
        if coord_old[0] in self._x_axis:
            if coord_old[0] != "a" and coord_old[0] != "t":
                self._coord_x_old = self._x_axis.index(coord_old[0])
        else:
            self._termination_trigger = True
            return print("INVALID X AXIS SELECTION FOR CENTER")

        if coord_new[0] in self._x_axis:
            if coord_new[0] != "a" and coord_new[0] != "t":
                self._coord_x_new = self._x_axis.index(coord_new[0])
        else:
            self._termination_trigger = True
            return print("INVALID X AXIS SELECTION FOR NEW CENTER")

        # Check if 2nd element (number) is one or two digits
        self._coord_y_old = []
        self._coord_y_new = []
        if len(coord_old) > 2:
            self._coord_y_old = [''.join(coord_old[1:3])]
        else:
            self._coord_y_old.append(coord_old[-1])

        if len(coord_new) > 2:
            self._coord_y_new = [''.join(coord_new[1:3])]
        else:
            self._coord_y_new.append(coord_new[-1])

        # Check bounds
        if not 1 < int(self._coord_y_old[-1]) < 20:
            self._termination_trigger = True
            return print("INVALID Y AXIS SELECTION")

        # Convert str to int
        self._coord_y_old = int(self._coord_y_old[-1])
        self._coord_y_new = int(self._coord_y_new[-1])

    def generate_piece_and_footprint(self):
        """
        Support method for make_move()to generate the old and new footprints to act as current and next piece locations,
        along with generating the piece itself in terms of its elements (stones, empty spaces)
        :return: No return.
        """

        # Footprint of gameboard indexes from first input coordinates of current piece center
        self._footprint_old = [[self._coord_x_old - 1, self._coord_y_old - 1],
                               [self._coord_x_old - 1, self._coord_y_old],
                               [self._coord_x_old - 1, self._coord_y_old + 1],
                               [self._coord_x_old, self._coord_y_old - 1], [self._coord_x_old, self._coord_y_old],
                               [self._coord_x_old, self._coord_y_old + 1],
                               [self._coord_x_old + 1, self._coord_y_old - 1],
                               [self._coord_x_old + 1, self._coord_y_old],
                               [self._coord_x_old + 1, self._coord_y_old + 1]]

        # Footprint of gameboard indexes from second input coordinates of new center
        self._footprint_new = [[self._coord_x_new - 1, self._coord_y_new - 1],
                               [self._coord_x_new - 1, self._coord_y_new],
                               [self._coord_x_new - 1, self._coord_y_new + 1],
                               [self._coord_x_new, self._coord_y_new - 1], [self._coord_x_new, self._coord_y_new],
                               [self._coord_x_new, self._coord_y_new + 1],
                               [self._coord_x_new + 1, self._coord_y_new - 1],
                               [self._coord_x_new + 1, self._coord_y_new],
                               [self._coord_x_new + 1, self._coord_y_new + 1]]

        # Formulate piece to be moved
        self._piece = [self._board[self._coord_x_old - 1][self._coord_y_old - 1],
                       self._board[self._coord_x_old - 1][self._coord_y_old],
                       self._board[self._coord_x_old - 1][self._coord_y_old + 1],
                       self._board[self._coord_x_old][self._coord_y_old - 1],
                       self._board[self._coord_x_old][self._coord_y_old],
                       self._board[self._coord_x_old][self._coord_y_old + 1],
                       self._board[self._coord_x_old + 1][self._coord_y_old - 1],
                       self._board[self._coord_x_old + 1][self._coord_y_old],
                       self._board[self._coord_x_old + 1][self._coord_y_old + 1]]

    def verify_piece_choice_validity(self):
        """
        Support method for make_move() that assures the easier has chosen a piece in line with the game rules.
        :return: No return. Incorrect player's turn or scenario where both stone colors are present is handled
        in make_move() termination_trigger check.
        """
        # Check for color singularity
        if "-B-" in self._piece and "-W-" in self._piece:
            self._termination_trigger = True
            return print("INVALID PIECE SELECTION; STONES OF BOTH COLOR PRESENT")

        # Verify the chosen piece belongs to the player who's turn it is
        if (self._turn_count % 2) == 0 or self._turn_count == 0:
            if "-W-" in self._piece:
                self._termination_trigger = True
                return print("NOT YOUR TURN; BLACK TO MAKE MOVE")
        else:
            if "-B-" in self._piece:
                self._termination_trigger = True
                return print("NOT YOUR TURN; WHITE TO MAKE MOVE")

    def check_ring_break(self):
        """
        Method to verify that if ring break is occuring, that it is not the last ring the player has on the board.
        This is done by executing the proposed move on the test board titled ring_board, and then counting the number
        of rings remaining for each player after execution. Player can break other players ring but not their own from
        making their move.
        :return: No return.
        """
        # Perform Move On Test Board
        count = 0
        for _ in self._footprint_new:
            self._ring_board[self._footprint_new[count][0]][self._footprint_new[count][1]] = self._piece[count]
            # If there's overlap, place new footprint in that area; if not, then 'put' (more apt to say 'leave')
            # old footprint
            if self._footprint_old[count] in self._footprint_new:
                self._ring_board[self._footprint_new[count][0]][self._footprint_new[count][1]] = self._piece[count]
            else:
                self._ring_board[self._footprint_old[count][0]][self._footprint_old[count][1]] = "---"
            count += 1

        # Recount Rings; if they're at zero, do not allow move
        self._black_ring_count = 0
        self._white_ring_count = 0
        for y in range(2, 18):
            self._ring_corner_y = y

            # X is x-axis; Letter
            for x in range(1, 17):
                self._ring_corner_x = x

                # Generate temporary piece
                self._ring_check = [self._ring_board[self._ring_corner_x][self._ring_corner_y],
                                    self._ring_board[self._ring_corner_x][self._ring_corner_y + 1],
                                    self._ring_board[self._ring_corner_x][self._ring_corner_y + 2],
                                    self._ring_board[self._ring_corner_x + 1][self._ring_corner_y],
                                    self._ring_board[self._ring_corner_x + 1][self._ring_corner_y + 1],
                                    self._ring_board[self._ring_corner_x + 1][self._ring_corner_y + 2],
                                    self._ring_board[self._ring_corner_x + 2][self._ring_corner_y],
                                    self._ring_board[self._ring_corner_x + 2][self._ring_corner_y + 1],
                                    self._ring_board[self._ring_corner_x + 2][self._ring_corner_y + 2]]

                # Check if temporary piece can be classified as a ring and of what color, and add to tally
                if self._ring_check.count("-B-") == 8 and self._ring_check[4] == "---":
                    self._black_ring_count += 1

                if self._ring_check.count("-W-") == 8 and self._ring_check[4] == "---":
                    self._white_ring_count += 1

        # Make sure ring being broken is the player's whose turn it is to allow offensive ring break of opponent
        if (self._turn_count % 2) == 0 or self._turn_count == 0:
            if self._black_ring_count == 0:
                self._termination_trigger = True
                return print("CANNOT BREAK OWN ONLY EXISTING RING")
        else:
            if self._white_ring_count == 0:
                self._termination_trigger = True
                return print("CANNOT BREAK OWN ONLY EXISTING RING")

    def check_center(self):
        """
        Verifies whether movement larger than a maximum of 3 spaces can be made by checking center square contents
        :return: No return.
        """
        x_diff = self._coord_x_new - self._coord_x_old
        y_diff = self._coord_y_new - self._coord_y_old

        # Must have center piece occupied to move more than 3 squares
        if abs(x_diff) > 3 or abs(y_diff) > 3:
            # Player making turn already checked so color does not matter at this point
            if "-B-" or "-W-" not in self._piece[4]:
                self._termination_trigger = True
                return print("CANNOT MOVE THAT FAR WITH SELECTED PIECE")

    def check_direction(self):
        """
        Interpret direction of movement based on position of old and new center coordinates and verify it's validity.
        :return: No return.
        """
        x_diff = self._coord_x_new - self._coord_x_old
        y_diff = self._coord_y_new - self._coord_y_old

        # Check if direction of movement of chosen piece is valid
        if 0 <= abs(x_diff) <= 1 and 0 <= abs(y_diff) <= 1:
            self._orientation = self._piece_compass.index([x_diff, y_diff])

        # Adjust inputs depending on distance of movement
        if (abs(x_diff) == 0 or abs(x_diff) == 2) and (abs(y_diff) == 0 or abs(y_diff) == 2):
            if x_diff == 2:
                x_diff -= 1
            if x_diff == -2:
                x_diff += 1
            if y_diff == 2:
                y_diff -= 1
            if y_diff == -2:
                y_diff += 1
            self._orientation = self._piece_compass.index([x_diff, y_diff])

        if (abs(x_diff) == 0 or abs(x_diff) == 3) and (abs(y_diff) == 0 or abs(y_diff) == 3):
            if x_diff == 3:
                x_diff -= 2
            if x_diff == -3:
                x_diff += 2
            if y_diff == 3:
                y_diff -= 2
            if y_diff == -3:
                y_diff += 2
            m = self._piece_compass.index([x_diff, y_diff])
            self._orientation = self._piece_compass.index([x_diff, y_diff])

        # Verify that piece square corresponding with direction of movement is indeed occupied
        u = self._piece[self._orientation]
        if self._piece[self._orientation] == "---":
            self._termination_trigger = True
            return print("INVALID MOVE; MOVEMENT DIRECTION NOT SUPPORTED BY PIECE STRUCTURE")

    def check_obstruction(self):
        """
        Method to verify unobstructed travel for piece from old center coordinates to new center coordinates.
        :return: No return.
        """
        x_diff = self._coord_x_new - self._coord_x_old
        y_diff = self._coord_y_new - self._coord_y_old

        # Check travel distance; Travel distance of one by the center should not be impacted by obstruction as piece
        # capture will occur
        if abs(x_diff > 1) or abs(y_diff > 1):
            # Initialize origin of movement
            self._move_x = self._coord_x_old
            self._move_y = self._coord_y_old

            # Verify and create center coordinates of the new temporary footprint_move which will incrementally shift
            # in the desired direction away from the footprint_old towards footprint_new
            for i in range(1, abs(x_diff) + 1):
                if self._orientation == 0:
                    self._move_x = self._move_x - 1
                    self._move_y = self._move_y - 1

                if self._orientation == 1:
                    self._move_x = self._move_x - 1
                    self._move_y = self._move_y

                if self._orientation == 2:
                    self._move_x = self._move_x - 1
                    self._move_y = self._move_y + 1

                if self._orientation == 3:
                    self._move_x = self._move_x
                    self._move_y = self._move_y - 1

                if self._orientation == 5:
                    self._move_x = self._move_x
                    self._move_y = self._move_y + 1

                if self._orientation == 6:
                    self._move_x = self._move_x + 1
                    self._move_y = self._move_y - 1

                if self._orientation == 7:
                    self._move_x = self._move_x + 1
                    self._move_y = self._move_y

                if self._orientation == 8:
                    self._move_x = self._move_x + 1
                    self._move_y = self._move_y + 1

                # Generate new temporary footprint
                self._footprint_move = [[self._move_x - 1, self._move_y - 1],
                                        [self._move_x - 1, self._move_y],
                                        [self._move_x - 1, self._move_y + 1],
                                        [self._move_x, self._move_y - 1], [self._move_x, self._move_y],
                                        [self._move_x, self._move_y + 1],
                                        [self._move_x + 1, self._move_y - 1],
                                        [self._move_x + 1, self._move_y],
                                        [self._move_x + 1, self._move_y + 1]]

                # Check if there are stones in the path of the piece
                count = 0
                for _ in self._footprint_move:
                    # Do not count overlaps between the temporary piece and the chosen piece to be moved
                    if self._footprint_move[count] not in self._footprint_old:
                        # Check if stones are present
                        if self._board[self._footprint_move[count][0]][self._footprint_move[count][1]] != "---":
                            # Check if temporary footprint arrived at new footprint by comparing centers;
                            # If it has, the piece only traveled a distance of one square and therefore captured stones
                            # rather than having any in its path
                            # If not, this means that, given the direction of travel, there are stones in the path
                            # of the piece to the declared new center location; invalidate the move
                            if self._footprint_move[4] != self._footprint_new[4]:
                                self._termination_trigger = True
                                return print("INVALID MOVE; OBSTRUCTION")
                    count += 1

    def border_scrubber(self):
        """
        Method to maintain vacancy of border zones on the game board.
        :return: No return.
        """
        # 'Clear' columns 1 and 20
        for i in range(0, 20):
            self._board[i][1] = "---"
            self._board[i][-1] = "---"

        # 'Clear' rows 0 and 19
        for i in range(1, 21):
            self._board[0][i] = "---"
            self._board[19][i] = "---"

    def check_win(self):
        """
        Method to check how many rings exist on the game board after a piece has moved.
        :return: No return.
        """
        # Iterate through each column to construct a temporary piece
        self._black_ring_count = 0
        self._white_ring_count = 0
        # Y is y-axis; Number
        for y in range(2, 18):
            self._ring_corner_y = y

            # X is x-axis; Letter
            for x in range(1, 17):
                self._ring_corner_x = x

                # Generate temporary piece
                self._ring_check = [self._board[self._ring_corner_x][self._ring_corner_y],
                                    self._board[self._ring_corner_x][self._ring_corner_y + 1],
                                    self._board[self._ring_corner_x][self._ring_corner_y + 2],
                                    self._board[self._ring_corner_x + 1][self._ring_corner_y],
                                    self._board[self._ring_corner_x + 1][self._ring_corner_y + 1],
                                    self._board[self._ring_corner_x + 1][self._ring_corner_y + 2],
                                    self._board[self._ring_corner_x + 2][self._ring_corner_y],
                                    self._board[self._ring_corner_x + 2][self._ring_corner_y + 1],
                                    self._board[self._ring_corner_x + 2][self._ring_corner_y + 2]]

                # Check if temporary piece can be classified as a ring and of what color, and add to tally
                if self._ring_check.count("-B-") == 8 and self._ring_check[4] == "---":
                    self._black_ring_count += 1

                if self._ring_check.count("-W-") == 8 and self._ring_check[4] == "---":
                    self._white_ring_count += 1

        # Check if move made has reduced the ring tally of opposing player to 0
        if self._black_ring_count == 0:
            self._state = "WHITE_WON"

        if self._white_ring_count == 0:
            self._state = "BLACK_WON"

    def update_ring_board(self):
        """
        Method to match the ring counting board to the actual game board after a valid move is made
        :return: No return.
        """
        self._ring_board = self._board

    def make_move(self, centr, new_centr):
        """
        Method to move user-selected piece to new location on the gameboard.
        :param centr: str alphanumeric combination for center of piece to be moved
        :param new_centr: str alphanumeric combination for where the center of the selected piece is intended to be
        placed
        :return: Boolean value True if execution not halted by activation of self._termination_trigger. False if it is.
        """

        # Run validation functions
        self._termination_trigger = False
        self.check_state()
        self.convert_to_axes(centr, new_centr)
        self.generate_piece_and_footprint()
        self.verify_piece_choice_validity()
        self.check_center()
        self.check_direction()
        self.check_obstruction()
        self.check_ring_break()

        if self._termination_trigger is True:
            return False

        # Initiate movement
        count = 0
        for _ in self._footprint_new:
            self._board[self._footprint_new[count][0]][self._footprint_new[count][1]] = self._piece[count]
            # If there's overlap, place new footprint in that area; if not, then 'put' (more apt to say 'leave')
            # old footprint
            if self._footprint_old[count] in self._footprint_new:
                self._board[self._footprint_new[count][0]][self._footprint_new[count][1]] = self._piece[count]
            else:
                self._board[self._footprint_old[count][0]][self._footprint_old[count][1]] = "---"

            count += 1

        self.border_scrubber()
        self.check_win()
        self.update_ring_board()
        self._turn_count += 1
        return True

    def resign_game(self):
        """
        Method to allow player to resign during their turn in the game
        :return: Statement declaring winner opposite of whoever resigned
        :rtype: str
        """
        # Verify who is asking to resign
        if (self._turn_count % 2) == 0 or self._turn_count == 0:
            self._state = "WHITE_WON"
        else:
            self._state = "BLACK_WON"
