import math

def planner(map, start, end, coeff):
    corners = retrieve_extreme(map)
    top_left = corners[0]
    bottom_right = corners[1]

    x_extreme_left = top_left[0]
    x_extreme_right = bottom_right[0]
    y_extreme_bottom = top_left[1]
    y_extreme_top = bottom_right[1]

    path = []
    path.append(start)

    current = (start[0],start[1])

    while current[0] != end[0] and current[1] != end[1]:
        possible_squares = generate_possible_squares(current,x_extreme_left,x_extreme_right,y_extreme_top,y_extreme_bottom)
        next_node = retrieve_min_cost_node(possible_squares,map,coeff,end)
        path.append(next_node)
        current = (next_node[0],next_node[1])

def retrieve_extreme(map):
    count1 = 0
    count2 = 0
    first = True
    for row in map:
        count1 += 1
        if first:
            for column in row:
                count2 += 1
            first = False
    return ((0,0),(count2,count1))


def generate_possible_squares(point,x_left,x_right,y_top,y_bottom):
    possible_squares = []
    if point[0] > x_left:
        possible_squares.append((point[0]-1,point[1]))
    if point[0] < x_right-1:
        possible_squares.append((point[0]+1,point[1]))
    if point[1] > y_top:
        possible_squares.append((point[0],point[1]-1))
    if point[1] < y_bottom-1:
        possible_squares.append((point[0],point[1]+1))
    if point[0] > x_left and point[1] > y_top:
        possible_squares.append((point[0]-1,point[1]-1))
    if point[0] < x_right-1 and point[1] > y_top:
        possible_squares.append((point[0]+1,point[1]-1))
    if point[0] > x_left and point[1] < y_bottom-1:
        possible_squares.append((point[0]-1,point[1]+1))
    if point[0] < x_right-1 and point[1] < y_bottom-1:
        possible_squares.append((point[0]+1,point[1]+1))
    return possible_squares

def retrieve_min_cost_node(possible_squares,map,coeff,end):
    min_cost = math.inf
    min_node = tuple()
    for point in possible_squares:
        bias = calculate_bias(point,coeff,end)
        if map[point[0]][point[1]] + bias < min_cost:
            min_cost = map[point[0]][point[1]]
            min_node = (point[0],point[1])
    return min_node

def calculate_bias(point,coeff,end):
    distance = manhattan_distance(point,end)
    return coeff * distance

def manhattan_distance(point,end):
    return abs(point[0]-end[0]) + abs(point[1]-end[1])