# --- Day 1: Historian Hysteria ---

TheChief Historianis always present for the big Christmas sleigh launch, but nobody has seen him in months! Last anyone heard, he was visiting locations that are historically significant to the North Pole; a group of Senior Historians has asked you to accompany them as they check the places they think he was most likely to visit.

As each location is checked, they will mark it on their list with astar. They figure the Chief Historianmustbe in one of the first fifty places they'll look, so in order to save Christmas, you need to help them getfifty starson their list before Santa takes off on December 25th.

Collect stars by solving puzzles.  Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first.  Each puzzle grantsone star. Good luck!

You haven't even left yet and the group of Elvish Senior Historians has already hit a problem: their list of locations to check is currentlyempty. Eventually, someone decides that the best place to check first would be the Chief Historian's office.

Upon pouring into the office, everyone confirms that the Chief Historian is indeed nowhere to be found. Instead, the Elves discover an assortment of notes and lists of historically significant locations! This seems to be the planning the Chief Historian was doing before he left. Perhaps these notes can be used to determine which locations to search?

Throughout the Chief's office, the historically significant locations are listed not by name but by a unique number called thelocation ID. To make sure they don't miss anything, The Historians split into two groups, each searching the office and trying to create their own complete list of location IDs.

There's just one problem: by holding the two lists upside by side(your puzzle input), it quickly becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?

For example:

```shell
3   4
4   3
2   5
1   3
3   9
3   3
```
Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up thesmallest number in the left listwith thesmallest number in the right list, then thesecond-smallest left numberwith thesecond-smallest right number, and so on.

Within each pair, figure outhow far apartthe two numbers are; you'll need toadd up all of those distances. For example, if you pair up a3from the left list with a7from the right list, the distance apart is4; if you pair up a9with a3, the distance apart is6.

In the example list above, the pairs and distances would be as follows:

To find thetotal distancebetween the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is2 + 1 + 0 + 1 + 2 + 5, a total distance of11!

Your actual left and right lists contain many location IDs.What is the total distance between your lists?

