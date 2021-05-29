import json


'''
array = '{"fruits": ["apple", "banana", "orange"]}'
data  = json.loads(array)
fruits_list = data['fruits']
print(fruits_list[0])
'''


mylist = [
    {
        'phone': 123,
        'destktp' : 'apple',
        'day' : [1,2,4,4],
        'information':
                        {
                            'book' : 'gofo',
                            'music': 'hello'
                        }

    },
    {
        'phone': 456,
        'destktp' : 'goolge',
        'day' : [6,7,8,8],
        'information':
                        {
                            'book' : 'te',
                            'music': 'sss'
                        }
    }
]


for item in mylist :
    if item['information']['book'] == 'te':
     print(item['information']['book'])


