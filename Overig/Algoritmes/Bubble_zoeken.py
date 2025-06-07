''' Bubble zoeken (tijdens het sorteren de grootste (of kleinste) waarden "naar boven bubbelen")
Hetzelde als de ingebouwde .sort functie (Die overigens veel sneller is)
'''

def bubble_sort(lijst):
    n = len(lijst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lijst[j] > lijst[j+1]:
                lijst[j], lijst[j+1] = lijst[j+1], lijst[j]

lijst = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(lijst)
print(lijst)
