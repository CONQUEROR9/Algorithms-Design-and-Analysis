import sys
import time


class KnightsTourProblem:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.board = []
        self.generate_the_board() # generates the board

    def generate_the_board(self):  # Creates a nested list to represent the game board
        for i in range(self.h):
            self.board.append([0] * self.w)

    def print_the_board(self):
        print("  ")
        print("------")
        for elem in self.board:
            print(elem)
        print("------")
        print("  ")

    def generate_knight_legal_moves(self, cur_pos):  # Generates a list of legal moves for the knight to take next
        possible_position = []
        move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for move in move_offsets:
            new_x = cur_pos[0] + move[0]
            new_y = cur_pos[1] + move[1]

            if new_x >= self.h:
                continue
            elif new_x < 0:
                continue
            elif new_y >= self.w:
                continue
            elif new_y < 0:
                continue
            else:
                possible_position.append((new_x, new_y))

        return possible_position

    def visit_lonely_neighbors(self, to_visit):
        # It is more efficient to visit the lonely neighbors first,
        # since these are at the edges of the chessboard and cannot
        # be reached easily if done later in the traversal
        neighbor_list = self.generate_knight_legal_moves(to_visit)
        empty_neighbours = []

        for neighbor in neighbor_list:
            value = self.board[neighbor[0]][neighbor[1]]
            if value == 0:
                empty_neighbours.append(neighbor)

        scores = []
        for empty in empty_neighbours:
            score = [empty, 0]
            moves = self.generate_knight_legal_moves(empty)
            for m in moves:
                if self.board[m[0]][m[1]] == 0:
                    score[1] += 1
            scores.append(score)

        scores_sort = sorted(scores, key=lambda s: s[1])
        sorted_neighbours = [s[0] for s in scores_sort]
        return sorted_neighbours

    def knight_tour(self, n, path, to_visit):

        # Recursive definition of knights tour. Inputs are as follows:
        # n = current depth of search tree
        # path = current path taken
        # to_visit = node to visit

        # starting time of the algorithm is saved
        start_time = time.time()

        self.board[to_visit[0]][to_visit[1]] = n
        path.append(to_visit)  # append the newest vertex to the current point
        print("Visiting: ", to_visit)

        if n == self.w * self.h:  # if every grid is filled
            self.print_the_board()
            print(path)
            print("\nVisited all the squares in the chess board!")
            print("\nExecution time is %s seconds" % (time.time() - start_time))
            sys.exit(0)

        else:
            sorted_neighbours = self.visit_lonely_neighbors(to_visit)
            for neighbor in sorted_neighbours:
                self.knight_tour(n + 1, path, neighbor)

            # If we exit this loop, all neighbours failed so we reset
            self.board[to_visit[0]][to_visit[1]] = 0
            try:
                path.pop()
                print("Going back to: ", path[-1])
            except IndexError:
                print("No path found")
                print("Execution time is %s seconds" % (time.time() - start_time))
                sys.exit(0)


if __name__ == '__main__':
    # Define the size of grid.
    size = int(input("Enter the size of the chess board: "))
    tour = KnightsTourProblem(size, size)
    tour.knight_tour(1, [], (0, 0))
    tour.print_the_board()
