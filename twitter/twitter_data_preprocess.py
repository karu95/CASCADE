import csv
import json
import preprocessor as p

csv_file_path = 'FullDataset.csv'

user_csv_path = 'userProfileWithIDs-1.1.csv'

out_csv_file = 'my_tweet.csv'

json_file_path = 'tweets.json'

csv_data = []

data={}

with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        post_data = {}
        post_id = row[1]
        post_data['author'] = row[0]
        post_data['text'] = p.clean(row[2])
        data[post_id] = post_data
        csv_data.append([post_id, [post_id],int(row[3])])
        prev_comment_ids = []
        for i in range(4, len(row), 4):
            if ('' in row[i:i+4]):
                break
            else:
                comment_data = {}
                comment_id = row[i+1]
                comment_data['author'] = row[i]
                comment_data['text'] = p.clean(row[i+2])
                sacastic = int(row[i+3])
                data[comment_id] = comment_data
                csv_data.append([comment_id, [post_id] + prev_comment_ids, sacastic])
                prev_comment_ids.append(comment_id)

with open(user_csv_path) as user_csv:
    csv_reader = csv.reader(user_csv)
    for row in csv_reader:
        post_data = {}
        post_id = row[1]
        post_data['author'] = row[0]
        post_data['text'] = p.clean(row[2])
        data[post_id] = post_data
        for i in range(4, len(row), 3):
            if ('' in row[i:i+3]):
                break
            else:
                comment_data = {}
                comment_id = row[i]
                comment_data['author'] = row[0]
                comment_data['text'] = p.clean(row[i+1])
                sacastic = int(row[i+2])
                data[comment_id] = comment_data

with open(json_file_path, 'w') as j_file:
    j_file.write(json.dumps(data, indent=4))

with open(out_csv_file, 'w') as out_csv:
    wr = csv.writer(out_csv)
    wr.writerows(csv_data)

