import math

def min_geo_dist(locations_a, locations_b):
    """
    Function that calculates closest points of each point of locations_a in locations_b.

    Input: 2 arrays: locations_a and locations_b
    Output: array: res, contains points in locations_b which each point in locations_a is closest to.
    """
    res_array = []
    for loc_a in locations_a:
        closest_point = locations_b[0]  # initialize closest point to be first element of locations_b
        min_distance = euc_dist(loc_a, locations_b[0])  # initialize minimum distance to be distance between loc_a 
                                                        # and the first point of second array
        for loc_b in locations_b:
            if euc_dist(loc_a,loc_b) < min_distance:
                closest_point = loc_b
                min_distance = euc_dist(loc_a,loc_b)
        
        res_array.append(closest_point)

    return res_array


def euc_dist(point_a, point_b):
    """
    Helper function of min_geo_dist that calculates distance between points.

    Input: 2 tuples/lists: point_a, point_b
    Output: float: dist
    """
    x_diff = point_a[0]-point_b[0]
    y_diff = point_a[1]-point_b[1]
    dist = math.sqrt(x_diff^2 + y_diff^2)  # Euclidean distance formula
    return dist
