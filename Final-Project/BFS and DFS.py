import threading # used to stop the process when the process crosses the time limit defined by the user
import time # used to calculate the time of execution of the program


class KnightsTourProblem:
    def __init__(self, board_size, timelimit):

        # initial state is set to 1, 1
        self.initialState = [1, 1]

        # actions a knight can take is set
        self.actions = [[-2, 1], [-2, -1], [-1, 2], [1, 2],
                        [2, 1], [2, -1], [1, -2], [-1, -2]]

        # board size is set
        self.board_size = board_size

        # timeout flag for breaking the search algorithm since it takes a long time for the inputs above 6
        self.timeout = False

        # timer initialization
        # timer works on a thread and stopExecution method will be invoked once timelimit is reached
        self.timer = threading.Timer(timelimit, self.haltexecution)

    # sets timeout flag to True so that search algorithm finishes with timeout
    def haltexecution(self):
        self.timeout = True

    # final state implementation; checks if the state length is equal to the number of tiles on board
    # an element of a node's state indicates a unique tile that is already visited
    def finalstate(self, state):
        if len(state) == (self.board_size * self.board_size):
            return True
        else:
            return False


class Node:

    def __init__(self, problem, parent=None, action=None, state=None):

        # location of node on board
        self.location = None

        # problem that the node belongs to
        self.problem = problem

        # parent of the node
        self.parent = parent

        # action that is taken to reach this node
        self.action = action

        # if node doesn't have a parent, then it is the root node so its state is initialized with the initial state
        # location is set to initial state as well
        if self.parent is None:
            self.state = []
            self.state.append(self.problem.initialState)
            self.location = self.problem.initialState

        # if it is not the root node enters here to set its state and location
        # gets the state of its parent and then current location of the node is appended to state
        else:
            self.state = self.parent.state[:]
            new_x = self.parent.location[0] + self.action[0]
            new_y = self.parent.location[1] + self.action[1]
            self.state.append([new_x, new_y])
            self.location = [new_x, new_y]


# checks if a child node is already in the queue or not
def isChildInQueue(queue, child):
    for node in queue:
        if node.state == child.state:
            return True
    return False


# function for solving the knights tour problem using breadth first search
def bfs(problem):
    # thread which will terminate the process once timelimit is reached is started
    problem.timer.start()
    # starting time of the algorithm is saved
    start_time = time.time()

    # root node is created
    node = Node(problem)
    # applies goal test to root node
    if problem.finalstate(node.state):
        print("A solution found. ")
        print(node.state)
        print("Execution time is %s seconds" % (time.time() - start_time))
        return

    # queue is initialized
    queue = []
    queue.append(node)
    # visited is initialized
    visited = []
    # goalNotFound variable is used to determine whether the search ends successfully or unsuccessfully,
    # and it is initialized to 0
    goalNotFound = True
    # keeps the number of nodes that are expanded
    number_of_expanded_nodes = 0
    # as long as queue has nodes and timeout doesn't occur and the goal state is not found loop continues
    while not problem.timeout and goalNotFound and queue:
        # first element in the queue is retrieved(act as a queue) and number of expanded nodes is increased by 1
        node = queue.pop(0)
        number_of_expanded_nodes += 1
        # state of the newly popped node is put into explored set
        visited.append(node.state)
        for action in problem.actions:
            temp_x = node.location[0] + action[0]
            temp_y = node.location[1] + action[1]
            if temp_x > 0 and temp_x <= problem.board_size and temp_y > 0 and temp_y <= problem.board_size:
                child = Node(problem, node, action)
                if child.location not in node.state and child.state not in visited and not isChildInQueue(queue, child):
                    if problem.finalstate(child.state):
                        goalNotFound = False
                        break
                    queue.append(child)
    # a solution is found; timeout didn't occur and a goal state is found (goalNotFound becomes false)
    if not goalNotFound and not problem.timeout:
        print("A solution found. ")
        print(child.state)
        print("Execution time is %s seconds" % (time.time() - start_time))
    # a solution is not found; timeout didn't occur and a goal state is not found (goalNotFound remains true)
    elif goalNotFound and not problem.timeout:
        print("No solution exists. ")
    # timeout occurred; a goal state is not found (goalNotFound remains true) and timeout occurred
    elif goalNotFound and problem.timeout:
        print("Timeout")
    # prints the search method and number of expanded nodes
    print("Searched with breadth first search method. ")
    print("Number of nodes expanded: " + str(number_of_expanded_nodes))
    return 0



# function for solving the knights tour problem using depth first search
def dfs(problem):
    # thread which will terminate the process once timelimit is reached is started
    problem.timer.start()
    # starting time of the algorithm is saved
    start_time = time.time()

    # root node is created
    node = Node(problem)
    # applies goal test to root node
    if problem.finalstate(node.state):
        print("A solution found. ")
        print(node.state)
        print("Execution time is %s seconds" % (time.time() - start_time))
        return

    # queue is initialized
    queue = []
    queue.append(node)
    # visited set is initialized
    visited = []
    # goalNotFound variable is used to determine whether the search ends successfully or unsuccessfully,
    # and it is initialized to 0
    goalNotFound = True
    # keeps the number of nodes that are expanded
    num_expanded_node = 0
    # as long as queue has nodes and timeout doesn't occur and the goal state is not found loop continues
    while not problem.timeout and goalNotFound and queue:
        # last element in the queue is retrieved(acts as a stack) and number of expanded nodes is increased by 1
        node = queue.pop()
        num_expanded_node += 1
        # state of the newly popped node is put into visited set
        visited.append(node.state)
        for action in problem.actions:
            temp_x = node.location[0] + action[0]
            temp_y = node.location[1] + action[1]
            if temp_x > 0 and temp_x <= problem.board_size and temp_y > 0 and temp_y <= problem.board_size:
                child = Node(problem, node, action)
                if child.location not in node.state and child.state not in visited and not isChildInQueue(queue, child):
                    if problem.finalstate(child.state):
                        goalNotFound = False
                        break
                    queue.append(child)

    # a solution is found; timeout didn't occur and a goal state is found (goalNotFound becomes false)
    if not goalNotFound and not problem.timeout:
        print("A solution found. ")
        print(child.state)
        print("Execution time is %s seconds" % (time.time() - start_time))
    # a solution is not found; timeout didn't occur and a goal state is not found (goalNotFound remains true)
    elif goalNotFound and not problem.timeout:
        print("No solution exists. ")
        print(child.state)
    # timeout occurred; a goal state is not found (goalNotFound remains true) and timeout occurred
    elif goalNotFound and problem.timeout:
        print("Timeout")
    # prints the search method and number of expanded nodes
    print("Searched with depth first search method. ")
    print("Number of nodes expanded: " + str(num_expanded_node))
    return 0


if __name__ == '__main__':
    # User has to enter the board size, timelimit and algorithm choice and that algorithm is used to
    # find a solution
    board_size = int(input("Enter board size: "))
    timelimit = int(input("Enter timelimit: "))
    choice = input("Which search algorithm `bfs`, `dfs`, `both` or `exit`: ")
    problem = KnightsTourProblem(board_size, timelimit)
    if choice == "bfs":
        bfs(problem)
    elif choice == "dfs":
        dfs(problem)
    elif choice == "both":
        bfs(problem)
        time.sleep(3)
        dfs(problem)
    else:
        print("Exiting")
