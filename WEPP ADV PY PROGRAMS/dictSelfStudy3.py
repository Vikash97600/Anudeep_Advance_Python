# 1. You have student scores for different subjects. Create a dictionary that maps
# each student to their highest score.
# Sample Data:
# scores = [
# {'student': 'Alice', 'subject': 'Math', 'score': 90},
# {'student': 'Alice', 'subject': 'English', 'score': 85},
# {'student': 'Bob', 'subject': 'Math', 'score': 75},
# {'student': 'Bob', 'subject': 'English', 'score': 80},
# {'student': 'Charlie', 'subject': 'Math', 'score': 95},
# {'student': 'Charlie', 'subject': 'English', 'score': 88}
# ]
'''
scores = [
{'student': 'Alice', 'subject': 'Math', 'score': 90},
{'student': 'Alice', 'subject': 'English', 'score': 85},
{'student': 'Bob', 'subject': 'Math', 'score': 75},
{'student': 'Bob', 'subject': 'English', 'score': 80},
{'student': 'Charlie', 'subject': 'Math', 'score': 95},
{'student': 'Charlie', 'subject': 'English', 'score': 88}
]
# stuScore={}
# for i in scores:
#     if i['student'] in stuScore:
#         if i['score']>stuScore[i['student']]:
#             stuScore[i['student']]=i['score']
#     else:
#         stuScore[i['student']]=i['score']
# print(stuScore)
    #    or
stuScore={
    student:max(items['score'] for items in scores if items['student']==student)
    for student in {items['student'] for items in scores}
}
print(stuScore)

'''

# 2. You have a list of items, each with a name and a category. Group the items by
# their category, where each category maps to a list of item names.
# Sample Data:
# items = [
# {'name': 'Apple', 'category': 'Fruit'},
# {'name': 'Banana', 'category': 'Fruit'},
# {'name': 'Carrot', 'category': 'Vegetable'},
# {'name': 'Broccoli', 'category': 'Vegetable'},
# {'name': 'Chicken', 'category': 'Meat'}
# ]
items = [
{'name': 'Apple', 'category': 'Fruit'},
{'name': 'Banana', 'category': 'Fruit'},
{'name': 'Carrot', 'category': 'Vegetable'},
{'name': 'Broccoli', 'category': 'Vegetable'},
{'name': 'Chicken', 'category': 'Meat'}
]

# itemCat={}
# for i in items:
#     if i['category'] in itemCat:
#         itemCat[i['category']].append(i['name'])
#     else:
#         itemCat[i['category']]=[i['name']]
# for j,k in itemCat.items():
#     print(j,k)

# or
category_items = {
    category: [item['name'] for item in items if item['category']== category]
    for category in {item['category'] for item in items}
}
for i,j in category_items.items():
    print(i,j)