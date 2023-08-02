import csv

fields = ['Book_Number', 'Book', 'Chapter_Numer', 'Verse_Number', 'Verse']
with open('Clean_RV.csv') as csv_file:
    reader = csv.reader(csv_file)
    count = 0
    graph = {}
    currList = []
    currBNum = -1
    books = ""

    for row in reader:
        booknum, book, chapternum, versenum, verse = row
        if book != book:
            