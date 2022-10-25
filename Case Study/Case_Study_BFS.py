graph_map = {
    'Frankfurt': ['Mannhiem', 'Wurzburg', 'Kassel'],
    'Mannhiem': ['Karlsruhe'],
    'Wurzburg': ['Erfurt', 'Nurnberg'],
    'Stuttgart': [],
    'Kassel': ['Munchen'],
    'Karlsruhe': ['Augsburg'],
    'Erfurt': [],
    'Nurnberg': ['Munchen','Stuttgart'],
    'Augsburg': ['Munchen'],
    'Munchen': []
}


def BFS(graph, s):
    visited = []
    queue = []
    visited.append(s)
    queue.append(s)

    while queue:
        u = queue.pop(0)

        print(u, "--->", end="")

        for neighbor in graph[u]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)


user_input = input("Enter the location from where you want to start or enter 1 to see all the locations: ")

while user_input != '0':

    if user_input == '1':

        print(
            " Frankfurt \n Mannhiem \n Wurzburg \n Stuttgart \n Kassel \n Karlsruhe \n Erfurt \n Nurnberg \n Augsburg \n "
            "Munchen")

    elif user_input == "Frankfurt" or user_input == "Mannhiem" or user_input == "Wurzburg" or user_input == "Stuttgart" or user_input == "Kassel" or user_input == "Karlsruhe" or user_input == "Erfurt" or user_input == "Nurnberg" or user_input == "Augsburg" or user_input == "Munchen":

        BFS(graph_map, user_input)

    else:

        print("\nYou have either entered a wrong location or forgot the case-sensitivity.")

    user_input = input("\n\nEnter the location from where you want to start or enter 1 to see all the locations or 0 "
                       "to exit: ")
