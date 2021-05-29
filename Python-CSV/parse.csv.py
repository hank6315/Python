import csv


'''
with open('name.csv' , 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open("new_names.csv", 'w',   newline='') as new_file:
        csv_writer = csv.writer(new_file , delimiter='\t')

        for line in csv_reader:
            print(line)
            csv_writer.writerow(line)
'''

'''
with open('new_names.csv' , 'r') as csv_file:
    #csv_reader = csv.reader(csv_file, delimiter='\t')
    #dictReader
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line)
'''


with open('name.csv' , 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open("dic_new_names.csv", 'w',   newline='') as new_file:
        fieldnames = ['first_name', 'last_name']
        #fieldnames = ['first_name', 'last_name', 'email']

        csv_writer = csv.DictWriter(new_file , fieldnames=fieldnames , delimiter='\t')
        csv_writer.writeheader()

        for line in csv_reader:
            print(line)
            #del line['email']
            csv_writer.writerow(line)

