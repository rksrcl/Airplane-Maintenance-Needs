import unittest

"""
Returns the number of mechanics needed to maintain the planes

Pre-conditions: 
- All times are between 0 and 24
- Start time is always before the end time
- Input is an integer array in the form of [[3,8], [0, 5], [10, 18], [0, 3], [5,10], [2,6]],
where each inner array represents a plane, the first number represents the start time for maintenance,
and the second number represents the end time for maintenance

Parameters:
- arr: an integer array representing planes and the their maintenance schedule

"""
def scheduling(arr):
    if arr is None or len(arr) == 0:
        return 0
    
    arr.sort()
    end_times = []
    for airplane in arr:
        for time in end_times:
            if time <= airplane[0]: # Check whether mechanic can fit plane in schedule
                end_times.remove(time)
                break
        end_times.append(airplane[1]) # Update/add new end time
    return len(end_times)

class Test(unittest.TestCase):
    def test_add_numbers(self):

        # Provided
        output = scheduling([[3,8], [0, 5], [10, 18], [0, 3], [5,10], [2,6]])
        self.assertEqual(output, 3, "Failed provided test case")

        output = scheduling([[0, 5]])
        self.assertEqual(output, 1, "Failed provided test case")

        output = scheduling([[1, 3], [2, 4], [3, 5]])
        self.assertEqual(output, 2, "Failed provided test case")        


        # Null/empty input
        output = scheduling(None)
        self.assertEqual(output, 0, "Failed for null array")

        output = scheduling([])
        self.assertEqual(output, 0, "Failed for empty array")


        # Scheduled times are exclusive but non-overlapping
        output = scheduling([[3,8], [8, 11]])
        self.assertEqual(output, 2, "Failed for non-overlapping times")

        output = scheduling([[0,5], [0, 24]])
        self.assertEqual(output, 2, "Failed for overlapping times")


if __name__ == '__main__':
    unittest.main()