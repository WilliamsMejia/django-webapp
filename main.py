import csv

#Main data is stored in CSV file so we first need to open it
with open('Clean_RV.csv') as csv_file:
    reader = csv.reader(csv_file)
    verseList = []
    chapNum = 1
    books = "Génesis"
    chapDict = {}

    #The name of  every book in the Bible (old and new testament)
    starting_dict = {'Génesis': None, 'Éxodo': None, 'Levítico': None, 'Números': None, 'Deuteronomio': None, 'Josué': None, 'Jueces': None, 'Rut': None,
                   '1 Samuel': None, '2 Samuel': None, '1 Reyes': None, '2 Reyes': None, '1 Crónicas': None, '2 Crónicas': None, 'Esdras': None, 'Nehemías': None,
                    'Ester': None, 'Job': None, 'Salmos': None, 'Proverbios': None, 'Eclesiastés': None, 'Cantares': None, 'Isaías': None, 'Jeremías': None, 'Lamentaciones': None,
                    'Ezequiel': None, 'Daniel': None, 'Oseas': None, 'Joel': None, 'Amós': None, 'Abdías': None, 'Jonás': None, 'Miqueas': None, 'Nahúm': None, 'Habacuc': None, 'Sofonías': None,
                    'Hageo': None, 'Zacarías': None, 'Malaquías': None, 'S. Mateo': None, 'S. Marcos': None, 'S. Lucas': None, 'S.Juan': None, 'Hechos': None, 'Romanos': None, '1 Corintios': None,
                    '2 Corintios': None, 'Gálatas': None, 'Efesios': None, 'Filipenses': None, 'Colosenses': None, '1 Tesalonicenses': None, '2 Tesalonicenses': None, '1 Timoteo': None,
                    '2 Timoteo': None, 'Tito': None, 'Filemón': None, 'Hebreos': None, 'Santiago': None, '1 Pedro': None, '2 Pedro': None, '1 Juan': None, '2 Juan': None, '3 Juan': None,
                    'Judas': None, 'Apocalipsis': None}

    #This is just an ugly solution to getting rid of the headers in the CSV file
    for row in reader:
        break
    for row in reader:

        break


    for row in reader:
        booknum, book, chapternum, versenum, verse = row

        #Checking if its the start of a new book and if it is then adding a dictionary with a list value to the corresponding book key in 'starting_dict'
        if (books != book):
            chapDict.update({chapNum:verseList})
            verseList = []
            chapNum = int(chapternum)
            starting_dict.update({books:chapDict})
            chapDict = {}
            books = book

        #checking if its a new chapter if it is is then we add a key value pair {chapternum: verseList} to the chapDictionary
        if int(chapternum) != chapNum:

            chapDict.update({chapNum:verseList})
            verseList = []
            chapNum = int(chapternum)

        #the way this code is specifially set up, it would not catch the last chapter of the book of Apocolipse so I added this edge case catch
        verseList.append(verse)
        if book == "Apocalipsis" and chapternum == "21" and versenum == '27':
            chapDict.update({chapNum:verseList})
            verseList = []
            chapNum = int(chapternum)
            starting_dict.update({books:chapDict})
            break

    #This is just 
    for row in reader:
        booknum, book, chapternum, versenum, verse = row
        verseList.append(verse)

    chapDict.update({22:verseList})
    starting_dict.update({"Apocalipsis":chapDict})

    str = ''
    while str != 'n':
        bChoice = input("What Book would you like to read? ")
        cChoice = int(input("What Chapter would you like to read? "))
        vChoice = int(input("What Verse would you like to read? "))
        temp = starting_dict.get(bChoice)
        chap = temp.get(cChoice)
        print(chap[vChoice-1])
        str = input("Would you like to continue? y/n: ")
