import time


def isValid(x, y, sol):
    if x >= 0 and y >= 0 and x < N and y < N and sol[x][y] == -1:
        return True
    return False


def displaySolution(sol):
    for x in range(N):
        for y in range(N):
            print(sol[x][y], end=' ')
        print()


def findKnightTourSol():
    sol = [[-1 for x in range(N)] for y in range(N)]
    xMove = [2, 1, -1, -2, -2, -1, 1, 2]
    yMove = [1, 2, 2, 1, -1, -2, -2, -1]
    sol[0][0] = 0
    if knightTour(0, 0, 1, sol, xMove, yMove) == False:
        print("Solution does not exist")
        return False
    else:
        displaySolution(sol)
    return True


def knightTour(x, y, move, sol, xMove, yMove):
    if move == N * N:
        return True

    for k in range(8):
        xNext = x + xMove[k]
        yNext = y + yMove[k]
        if isValid(xNext, yNext, sol):
            sol[xNext][yNext] = move
            if knightTour(xNext, yNext, move + 1, sol, xMove, yMove) == True:
                return True
            else:
                sol[xNext][yNext] = -1

    return False


if __name__ == "__main__":
    N = int(input("Please enter the size of the board (Less than or equal to 8) : "))
    # starting time of the algorithm is saved
    start_time = time.time()
    findKnightTourSol()
    print("\nExecution time is %s seconds" % (time.time() - start_time))
