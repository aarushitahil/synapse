from itertools import combinations

#sample input:
#l = [('Kevin', {'Halsey', 'Taylor Swift', 'Mitski', 'Joji', 'Shawn Mendes', 'Sabrina Carpenter', 'Nicki Minaj', 'Conan Gray', 'One Direction', 'Justin Bieber'}), ('Stuart', {'Kendrick Lamar', 'Steve Lacy', 'Tyler the Creator', 'Joji', 'TheWeeknd', 'Coldplay', 'Kanye West', 'Travis Scott', 'Frank Ocean', 'Brent Faiyaz'}), ('Bob', {'Conan Gray', 'Joji', 'Dove Cameron', 'Mitski', 'Arctic Monkeys', 'Steve Lacy', 'Kendrick Lamar', 'Isabela LaRosa', 'Shawn Mendes', 'Coldplay', 'Lauv'}), ('Edith', {'Metallica', 'Billie Eilish', 'TheWeeknd', 'Mitski', 'NF', 'Conan Gray', 'Kendrick Lamar', 'Nicki Minaj', 'Kanye West', 'Coldplay'})]

#taking input
k, s, b, e = map(int, input('Enter number of artists for Kevin, Stuart, Bob and Edith (as space seperated integers): ').split())   
print('Enter artists for each dj (in the same order with each artist on new line):')
l = zip(['Kevin', 'Stuart', 'Bob', 'Edith'], [{input() for _ in range(k)}, {input() for _ in range(s)}, {input() for _ in range(b)}, {input() for _ in range(e)}]) 

combos = []     #list of tuples with dj pairs and their overlap 

for (name1, set1), (name2, set2) in list(combinations(l, 2)):   #iterating over all possible combinations
    overlap = len(set1.intersection(set2))
    if overlap >= 0.3*max(len(set1), len(set2)): 
        combos.append((name1, name2, overlap)) #we now have all possible pairs

combos.sort(key=lambda x: x[2], reverse=True) #sorting 

for name1, name2, overlap in combos:
    print(f'{name1}, {name2}')