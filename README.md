# remove-five
An assignment, find out which '5' digit to remove from a number to get the largest number left.

## algorithm explanation
examining the locations of fives, we can adress '5' as cur_five and succeeding number right after the '5' as cur_next, when looking from msb to lsb. 
if num is postive, we should remove the first 'cur_five' only if cur_next is larger than 5, making the cur_next first inline to the msb, should be bigger than the removed cur_five.

if no larger cur_next found, we should create less "damage" to the remaining number thus- remove the lsb cur_five. 

if 'num' is negative, we address the same msb, but upside down , 
knowing that,in negative form the lower the number the bigger it is.

we will do the same algorithm, but will seek the 'cur_next' which is
smaller than 5.
again we will make less dammage romving the lsb cur_five when negative if all the the succeeding numbers are bigger than 5.

