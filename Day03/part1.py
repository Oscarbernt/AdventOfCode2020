from functools import reduce

def find_tree_collisions(instructions, file_path):
        x = 0        
        tree_count = 0
        x_limit = len(tree_map[0])
        for i in tree_map[::instructions["y"]]:
            if i[x % x_limit] == "#":
                tree_count = tree_count + 1
            x = x + instructions["x"]

        return tree_count

def get_map(file_path):
    file = open(file_path, "r")
    return file.read().splitlines()

if __name__ == "__main__":
    tree_map = get_map("map.txt")
    instruction = {"x": 3, "y": 1}
    print(find_tree_collisions(instruction, tree_map))
    # instructions = [
    #     {"x": 1, "y": 1},
    #     {"x": 3, "y": 1},
    #     {"x": 5, "y": 1},
    #     {"x": 7, "y": 1},
    #     {"x": 1, "y": 2}]

    # results = []
    # for i in instructions:
    #     results.append(find_tree_collisions(i, tree_map))

    # print("Product:", reduce((lambda x, y: x * y),results)) 
