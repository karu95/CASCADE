import csv
import json
import preprocessor as p

csv_path = 'userProfileWithIDs-1.1.csv'

out_json = 'sarcasmTweets1.json'

# out_csv = 'my_user_tweet.csv'

data={}

csv_data=[]


with open(csv_path) as user_csv:
    csv_reader = csv.reader(user_csv)
    for row in csv_reader:
        post_data = {}
        post_id = row[1]
        post_data['author'] = row[0]
        post_data['text'] = p.clean(row[2])
        # csv_data.append([post_id, ['0'], int(row[3])])
        data[post_id] = post_data
        for i in range(4, len(row), 3):
            if ('' in row[i:i+3]):
                break
            else:
                comment_data = {}
                comment_id = row[i]
                comment_data['text'] = p.clean(row[i+1])
                sacastic = int(row[i+2])
                data[comment_id] = comment_data
                # csv_data.append([post_id, [str(comment_id)], sacastic])


with open(out_json, 'a+') as o_json:
    o_json.write(json.dump(data, indent=4))


# with open(out_csv) as o_csv:
#     csv_writer = csv.writer(o_csv)
#     csv_writer.writerows(csv_data)
