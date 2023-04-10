import csv
import datetime
current_date = datetime.date.today().strftime('%Y-%m-%d')
output_dir = r'C:\Users\darba\Documents\GitHub\Life-Sanity-Check\april2023'
questions = [current_date, 'Weight Change', 'Topics of Focus', 'How I moved towards my goals', 'What I did to get out of my comfort zone', 'Major events/notes', 'Favorite song this week', 'Times meditated','Most read book', 'One serious situation that was treated playfully' ]
responses = []

for question in questions:
    response = input(question + ' ')
    responses.append(response)


messages = questions.copy()
messages.extend(responses)

filename = f'{current_date}Weekly.csv'
full_path = f'{output_dir}/{filename}'
with open(full_path, mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(messages[:len(questions)])
    writer.writerow(messages[len(questions):])

print(f'CSV file "{full_path}" created successfully in directory "{output_dir}"!')


