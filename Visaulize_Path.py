import numpy as np
import cv2 # type: ignore

def visualize_maze(path, save_image=False, file_name='maze_output.png'):
    # Define your maze
    maze = [
        [1, 2, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 3, ' ', ' ', ' ', 4],
        [' ', 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, ' ', ' ', ' ', ' ', 15, ' ', ' ', ' ', 16],
        [' ', ' ', ' ', ' ', ' ', 17, ' ', ' ', ' ', ' ', 18, 19, 20, 21, 22, 23, ' ', ' ', ' ', 24],
        [' ', ' ', ' ', ' ', ' ', 25, ' ', ' ', ' ', ' ', ' ', ' ', 26, ' ', 27, 28, 29, 30, 31, 32],
        [' ', 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, ' ', ' ', ' ', ' ', ' ', 45, ' '],
        [' ', 46, ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 47, ' ', ' ', ' ', ' ', ' ', 48, ' '],
        [' ', 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, ' ', ' ', 64, ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 65, ' ', ' ', 66, 67, 68, ' ', 69, ' '],
        [' ', 70, 71, 72, 73, 74, 75, ' ', 76, 77, 78, 79, 80, ' ', ' ', ' ', 81, 82, 83, ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 84, 85, 86, ' ']
    ]

    # Define the colors
    white = (255, 255, 255)  # White color for nodes
    red = (0, 0, 255)        # Red color for the path
    black = (0, 0, 0)        # Black background

    # Create an image with black background
    height, width = len(maze), len(maze[0])
    img = np.ones((height * 40, width * 40, 3), dtype=np.uint8) * 0  # Black background

    # Create a set for quick lookup of path nodes
    path_set = set(map(int, path))

    for i in range(height):
        for j in range(width):
            # Calculate the position for drawing
            x, y = j * 40 + 10, i * 40 + 30
            if maze[i][j] != ' ':
                if int(maze[i][j]) in path_set:
                    # Draw red star for path nodes
                    cv2.putText(img, '*', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, red, 2, cv2.LINE_AA)
                else:
                    # Draw white node for other nodes
                    cv2.putText(img, 'o', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, white, 2, cv2.LINE_AA)

    # Optionally save the maze as an image file
    if save_image:
        cv2.imwrite(file_name, img)

# Function to visualize a single path
def visualize_path(path, algorithm_name, save_file_name):
    visualize_maze(path, save_image=True, file_name=save_file_name)  # Save image for each algorithm

    # Display the saved image
    img = cv2.imread(save_file_name)
    if img is None:
        print(f"Error loading image for {algorithm_name}.")
        return
    cv2.imshow(f'{algorithm_name} Shortest Path', img)

Mappings = {'1': (0, 0), '2': (0, 1), '0': (9, 19), '3': (0, 15), '4': (0, 19), '5': (1, 1), '6': (1, 2), '7': (1, 3), '8': (1, 4), '9': (1, 5), '10': (1, 6), '11': (1, 7), '12': (1, 8), '13': (1, 9), '14': (1, 10), '15': (1, 15), '16': (1, 19), '17': (2, 5), '18': (2, 10), '19': (2, 11), '20': (2, 12), '21': (2, 13), '22': (2, 14), '23': (2, 15), '24': (2, 19), '25': (3, 5), '26': (3, 12), '27': (3, 14), '28': (3, 15), '29': (3, 16), '30': (3, 17), '31': (3, 18), '32': (3, 19), '33': (4, 1), '34': (4, 2), '35': (4, 3), '36': (4, 4), '37': (4, 5), '38': (4, 6), '39': (4, 7), '40': (4, 8), '41': (4, 9), '42': (4, 10), '43': (4, 11), '44': (4, 12), '45': (4, 18), '46': (5, 1), '47': (5, 12), '48': (5, 18), '49': (6, 1), '50': (6, 2), '51': (6, 3), '52': (6, 4), '53': (6, 5), '54': (6, 6), '55': (6, 7), '56': (6, 8), '57': (6, 9), '58': (6, 10), '59': (6, 11), '60': (6, 12), '61': (6, 13), '62': (6, 14), '63': (6, 15), '64': (6, 18), '65': (7, 11), '66': (7, 14), '67': (7, 15), '68': (7, 16), '69': (7, 18), '70': (8, 1), '71': (8, 2), '72': (8, 3), '73': (8, 4), '74': (8, 5), '75': (8, 6), '76': (8, 8), '77': (8, 9), '78': (8, 10), '79': (8, 11), '80': (8, 12), '81': (8, 16), '82': (8, 17), '83': (8, 18), '84': (9, 16), '85': (9, 17), '86': (9, 18)}

def path_mapping(path):
    node_path = []
    for node in path:
        co_ordinates = Mappings[node]
        node_path.append(co_ordinates)
    return node_path
