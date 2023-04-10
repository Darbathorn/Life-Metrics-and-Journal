import csv
import datetime
current_date = datetime.date.today().strftime('%Y-%m-%d')
output_dir = r'C:\Users\darba\Documents\GitHub\Life-Sanity-Check\april2023'
questions = [current_date, 'Happiness', 'Self-Confidence', 'Weight', 'Strength (Self-evaluated)', 'Topic I was wrong about', 'Thought revision on topic', 'Goal for tomorrow', 'One thing I did today for the sake of tomorrow', 'One nice thing', 'One bad thing that happened to me today', 'Why was it the best thing that ever happened to me', 'Major events/remarks']
responses = []

for question in questions:
    response = input(question + ' ')
    responses.append(response)


messages = questions.copy()
messages.extend(responses)

filename = f'{current_date}.csv'
full_path = f'{output_dir}/{filename}'
with open(full_path, mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(messages[:len(questions)])
    writer.writerow(messages[len(questions):])

print(f'CSV file "{full_path}" created successfully in directory "{output_dir}"!')
