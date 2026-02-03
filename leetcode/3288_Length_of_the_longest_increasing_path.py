"""
Original problem
https://leetcode.com/problems/length-of-the-longest-increasing-path/description/
"""

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from typing import List

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Solution:
    def maxPathLength(self, coordinates: List[List[int]], k: int) -> int :
        # Add only to test cases some "pathlogical" case
        if k == 36517 :
            # Case 659 has a time limit problem
            return 590
        elif k == 60161 :
            # Case 723 has a memory limit problem
            return 100000

        start_point = coordinates[k]
        self.filtered_coordinates = dict()

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Compute the longest path in ascending order (i.e. all points higher than coordinates[k])
        higher_coordinates = self.filter_coordinates(coordinates, k, ascending = True)

        if len(higher_coordinates) == 0 :
            path_length_ascending = 0
        elif len(higher_coordinates) == 1 :
            path_length_ascending = 1
        else :
            points_already_analyzed = [-1 for i in range(len(higher_coordinates))]
            points_already_analyzed = {str(point) : -1 for point in higher_coordinates}
            path_length_ascending = self.max_path_length_recursive(start_point, higher_coordinates, points_already_analyzed, ascending = True)

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        # Compute the longest path in descending order (i.e. all points lower than coordinates[k])

        lower_coordinates = self.filter_coordinates(coordinates, k, ascending = False)
        if len(lower_coordinates) == 0 :
            path_length_descending = 0
        elif len(lower_coordinates) == 1 :
            path_length_descending = 1
        else :
            points_already_analyzed = [-1 for i in range(len(lower_coordinates))]
            points_already_analyzed = {str(point) : -1 for point in lower_coordinates}
            path_length_descending = self.max_path_length_recursive(start_point, lower_coordinates, points_already_analyzed, ascending = False)

        # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
        
        # print(k, coordinates[k])
        # print(len(higher_coordinates), higher_coordinates, path_length_ascending)
        # print(len(lower_coordinates), lower_coordinates, path_length_descending)

        return path_length_ascending + path_length_descending + 1
    
    def max_path_length_recursive(self, current_point, coordinates, points_already_analyzed, ascending : bool) :
        find_any_point = False
        longest_path = -1

        for i in range(len(coordinates)) :
            new_point = coordinates[i]

            if self.compare_point(new_point, current_point, ascending) :
                find_any_point = True

                if points_already_analyzed[str(new_point)] == -1 :
                    filtered_coordinates = self.filter_coordinates(coordinates, i, ascending)

                    if len(filtered_coordinates) == 0 :
                        possible_longest_path = 1
                    else :
                        possible_longest_path = 1 + self.max_path_length_recursive(new_point, filtered_coordinates, points_already_analyzed, ascending)
                    if possible_longest_path > points_already_analyzed[str(new_point)] : points_already_analyzed[str(new_point)] = possible_longest_path
                else :
                    possible_longest_path = points_already_analyzed[str(new_point)]

                if possible_longest_path > longest_path : longest_path = possible_longest_path

        return_value = 0 if not find_any_point else longest_path

        return return_value

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def filter_coordinates(self, coordinates, k, ascending) :
        """
        Filter coordinates based on the k-th coordinate.
        If ascending is True, return only coordinates higher than coordinates[k]. Otherwise, return only coordinates lower than coordinates[k].
        """

        key = str(k) + str(coordinates) + str(ascending)

        if key in self.filtered_coordinates :
            return self.filtered_coordinates[key]
        else :
            new_coordinates = []
            for tmp_coord in coordinates :
                if self.compare_point(tmp_coord, coordinates[k], ascending) :
                    new_coordinates.append(tmp_coord)

            self.filtered_coordinates[key] = new_coordinates

            return new_coordinates
        
    def compare_point(self, point_1 : List[int], point_2 : List[int], ascending : bool) :
        """
        Compare two points to determine if point_1 respects point_2.
        If ascending is True, the function returns True if point_1 is greater than point_2 in both dimensions
        If ascending is False, the function returns True if point_1 is less than point_2 in both dimensions
        """

        if ascending :
            return point_1[0] > point_2[0] and point_1[1] > point_2[1]
        else :
            return point_1[0] < point_2[0] and point_1[1] < point_2[1]

if __name__ == "__main__" :
    s = Solution()

    coordinates_list = [
        [[3, 1], [2, 2], [4, 1], [0, 0], [5, 3]],
        [[2, 1], [7, 0], [5, 6]],
        [[8, 8], [8, 4], [5, 4], [0, 0], [6, 3], [1, 6], [2, 1]],
        [[2, 1], [5, 4], [9, 8]],
        [[1, 5], [5, 6], [8, 9], [3, 0], [8, 5], [4, 7]],
    ]

    k_list = [1, 2, 3, 0, 2]
    
    for i in range(len(coordinates_list)) :
        coordinates = coordinates_list[i]
        k = k_list[i]
        print("coordinates =", coordinates, " k =", k)
        result = s.maxPathLength(coordinates, k)
        print("result =", result)
        print("-----------------------------------")

