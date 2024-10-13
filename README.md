# CS4250-HW2

## A Python program that connects to a MongoDB database, carries out CRUD operations and can print out an inverted index ordered by term based on user input.

```
######### Menu ##############
#a - Create a document
#b - Update a document
#c - Delete a document.
#d - Output the inverted index ordered by term.
#q - Quit

Enter a menu choice: a
Enter the ID of the document: 4
Enter the text of the document: Why is summer so hot here? So hot!
Enter the title of the document: Arizona
Enter the date of the document: 2024-09-06
Enter the category of the document: Seasons

Enter a menu choice: d
{'found': ['Discovery:1'], 'is': ['Exercise:1', 'Arizona:1', 'California:1'], 'why': ['Discovery:1', 'Arizona:1'], 'hot': ['Arizona:2'], 'months': ['Discovery:3', 'Exercise:1'], 'later': ['Discovery:1'], 'picnics': ['California:2'], 'we': ['Discovery:1'], 'summer': ['California:1', 'Exercise:1', 'Arizona:1'], 'so': ['Arizona:2'], 'time': ['California:2'], 'for': ['California:1'], 'baseball': ['Exercise:1'], 'here': ['Arizona:1', 'California:1'], 'during': ['Exercise:1'], 'played': ['Exercise:1'], 'the': ['California:1'], 'out': ['Discovery:1']}  

Enter a menu choice: b
Enter the ID of the document: 4
Enter the text of the document: Why is summer so hot here? This is a bad time!
Enter the title of the document: Arizona
Enter the date of the document: 2024-09-07
Enter the category of the document: Seasons

Enter a menu choice: d
{'out': ['Discovery:1'], 'is': ['Arizona:2', 'Exercise:1', 'California:1'], 'why': ['Discovery:1', 'Arizona:1'], 'hot': ['Arizona:1'], 'months': ['Exercise:1', 'Discovery:3'], 'later': ['Discovery:1'], 'picnics': ['California:2'], 'we': ['Discovery:1'], 'time': ['Arizona:1', 'California:2'], 'so': ['Arizona:1'], 'summer': ['Exercise:1', 'Arizona:1', 'California:1'], 'baseball': ['Exercise:1'], 'for': ['California:1'], 'this': ['Arizona:1'], 'bad': ['Arizona:1'], 'here': ['California:1', 'Arizona:1'], 'a': ['Arizona:1'], 'played': ['Exercise:1'], 'during': ['Exercise:1'], 'the': ['California:1'], 'found': ['Discovery:1']}

Enter a menu choice: c
Enter the document ID to be deleted: 4

Enter a menu choice: d
{'is': ['Exercise:1', 'California:1'], 'out': ['Discovery:1'], 'why': ['Discovery:1'], 'months': ['Discovery:3', 'Exercise:1'], 'later': [{'is': ['Exercise:1', 'California:1'], 'out': ['Discovery:1'], 'why': ['Discovery:1'], 'months': ['Discovery:3', 'Exercise:1'], 'later': ['Discovery:1'], 'picnics': ['California:2'], 'time': ['California:2'], 'we': ['Discovery:1'], 'baseball': ['Exercise:1']fornia:1', 'Exercise:1'], 'for': ['California:1'], 'here': ['California:1'], 'played': ['Exercise:1'], 'during': ['Exercise:1'], 'the': ['California:1'], 'found': ['Discovery:1']}

Enter a menu choice: q
Leaving the application ...
```
