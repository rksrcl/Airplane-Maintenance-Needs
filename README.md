**Solution to AircraftMaintenanceScheduling**

Questions:
- What are some efficient and straightforward ways to solve without sorting the array?
- Python has a really nice sorting algorithm - how would this play out in other languages? Ex: in Java, we could use the Comparator.
- What happens if users accidentally schedule two planes for maintenance at the same time?*
- What if unexpected maintenance is discovered?*


Assumptions I made:
- Mechanics work around the clock.
- Mechanics are able to fix the plane they are assigned to.
- Mechanics never go over the allotted time, and maintenance time does not get extended.*
- When there is a duplicate input, that means different planes are scheduled for maintenance at the same time,*
- The provided input is either an empty array like [], or has entries that match the expected input. Ex: [[], []] will not be inputted.
- All provided times for planes are on the same day.
- Maintenance begins on time.

*I played around with a solution that could account for unscheduled maintenance and printed a warning for duplicate times (addressing those questions and assumptions) in solution2.py.

Different paths or solutions:
- I considered using a double for-loop through the array, looping through all the planes twice and checking the times. If the maintenance times for two planes overlapped, I would increase the counter for the number of mechanics.
- I considered using a TreeMap (in Java) for storing the schedules. However, this could be problematic if two planes were scheduled for maintenance at the same time, as TreeMaps require unique keys.
