from functools import reduce

## part 1
f=open("input-day-2.txt", "r")
phrases = f.read().split("\n")[:-1]
# for testing only
# phrases = ['abcdef','bababc','abbcde','abcccd','aabcdd','abcdee','ababab']

final_counts = {}
final_counts['2'] = 0
final_counts['3'] = 0

def update_final_counts(value):
    if value in list(d.values()):
        final_counts[str(value)] += 1
    return;

for p in phrases:
    d = {}
    for c in p:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    update_final_counts(2)
    update_final_counts(3)

print(reduce(lambda x, y: x*y, list(final_counts.values())))

# part 2
# for testing only
# phrases = ['abcde','fghij','klmno','pqrst','fguij','axcye','wvxyz']

f=open("input-day-2.txt", "r")
phrases = f.read().split("\n")[:-1]
word_len = len(phrases[0])
size = len(phrases) - 1

def determine_repeat(phrases, word_len, size):
    for index, word in enumerate(phrases):
        for i in range(index + 1, size):
            ## iterate thru all other words below
            comparison_word = phrases[i]
            for c in range(0, word_len):
                first = word[:c] + word[c+1:]
                second = comparison_word[:c] + comparison_word[c+1:]
                if first == second:
                    return first;

print(determine_repeat(phrases, word_len, size))
