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

visited = set()


def DFS(graph, s):
    if s not in visited:
        print(s, "--->", end="")
        visited.add(s)
        for neighbour in graph[s]:
            DFS(graph, neighbour)


user_input = input("Enter the location from where you want to start or enter 1 to see all the locations: ")

while user_input != '0':

    if user_input == '1':

        print(
            "Frankfurt \n Mannhiem \n Wurzburg \n Stuttgart \n Kassel \n Karlsruhe \n Erfurt \n Nurnberg \n Augsburg "
            "\n Munchen")

    elif user_input == "Frankfurt" or user_input == "Mannhiem" or user_input == "Wurzburg" or user_input == "Stuttgart" or user_input == "Kassel" or user_input == "Karlsruhe" or user_input == "Erfurt" or user_input == "Nurnberg" or user_input == "Augsburg" or user_input == "Munchen":

        DFS(graph_map, user_input)

    else:

        print("\nYou have either entered a wrong location or forgot the case-sensitivity.")

    user_input = input("\n\nEnter the location from where you want to start or enter 1 to see all the locations or 0 "
                       "to exit: ")
