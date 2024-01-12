import random
from unittest.mock import patch
from io import StringIO
import unittest
import solution

"""
Returns the number of mechanics needed to maintain the planes with:
- a warning for user if there are duplicate times for plane maintenance scheduled
- consideration of the possibility of unscheduled maintenance

Pre-conditions: 
- All times are between 0 and 24
- Start time is always before the end time
- Input is an integer array in the form of [[3,8], [0, 5], [10, 18], [0, 3], [5,10], [2,6]],
where each inner array represents a plane, the first number represents the start time for maintenance,
and the second number represents the end time for maintenance

Parameters:
- a: an integer array representing planes and the their maintenance schedule

"""
def scheduling(a):
     
    if a is None or len(a) == 0:
        return 0
    
    arr = [plane[:] for plane in a]
    if len(set(map(tuple, arr))) != len(arr):
        print("It appears there are duplicate times for plane maintenance. "
              "Please confirm if this represents different planes undergoing maintenance at the same time.")
    for airplane in arr:
        rand = int(random.gauss(0, 1)) # Account for unscheduled maintenance
        variable = max(-5, min(5, rand))
        if variable > 0:
            if variable + airplane[1] >= 24:
                airplane[1] = 24
            else:
                airplane[1] += variable

    solution.scheduling(arr)

class Test(unittest.TestCase):
    def test_duplicate_times_message(self):
        warning = ("It appears there are duplicate times for plane maintenance. "
                   "Please confirm if this represents different planes undergoing maintenance at the same time.")

        # Check duplicate cases
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            scheduling([[3,8], [8, 11], [3, 8]])
            message = mock_stdout.getvalue().strip()
            self.assertEqual(message, warning, "Failed printing warning for duplicates")
            
            
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            scheduling([[0, 7], [0, 7]])
            message = mock_stdout.getvalue().strip()
            self.assertEqual(message, warning, "Failed printing warning for duplicates")
        
        # Ensure no false alarms are raised
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            scheduling([[0, 7], [8, 9]])
            message = mock_stdout.getvalue().strip()
            self.assertNotEqual(message, warning)

        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            scheduling([[8, 9], [16, 24]])
            message = mock_stdout.getvalue().strip()
            self.assertNotEqual(message, warning)

            



if __name__ == '__main__':
    unittest.main()