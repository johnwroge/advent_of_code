'''
As far as the Elf has been able to figure out, you have to figure out which of the 
numbers you have appear in the list of winning numbers. The first match makes the card
 worth one point and each match after the first doubles the point value of that card.


Card 1: 
'41 48 83 86 17','83 86  6 31 17  9 48 53'

set {41, 48 ,83, 86, 17}
iterate over winning values O(n)

initialize count = 0

iterate over candidates 
    check if candidate is in set (O(1))
        if yes and count is 0
            increment count by1
        if yes and count > 0 
            count is itself x 2
        
add amount to final total and move on to next line


There's no such thing as "points". Instead, scratchcards only cause you to
 win more scratchcards equal to the number of winning numbers you have.

Specifically, you win copies of the scratchcards below the winning
card equal to the number of matches. So, if card 10 were to have 
5 matching numbers, you would win one copy each of cards
11, 12, 13, 14, and 15.

Sum = (n/2) * (a + a_n)


'''



with open('/Users/johnwroge/advent_of_code/2023/Day4/day4.txt', 'r') as file:
    contents = file.read().splitlines() 

results = []
for line in contents:
    day, cards = line.split(':')
    results.append(cards.split('|'))

final_total = 0

card_index = 1 
final_total_2 = 0

for line in results:
    wins, candidates = line
    set_to_check = set()
    for number_string in wins.split():
        set_to_check.add(number_string)
    
    curr_total_part1 = 0
    card_total_part2 = 0
    
    for winning_string in candidates.split():
        
        if winning_string in set_to_check:
            card_total_part2 += 1
            if curr_total_part1 == 0:
                curr_total_part1 += 1
            else:
                curr_total_part1 *= 2
    # total (1) 4 = int(4/2 * 2 1 )
    final_total_2 += int(((card_total_part2)//2) * (card_index + 1 + card_index + 1 + card_total_part2))

    card_index += 1
    final_total += curr_total_part1

print('Total cards for file of cards is: ', final_total)
print('The total cards for part 2 is: ', final_total_2)          





