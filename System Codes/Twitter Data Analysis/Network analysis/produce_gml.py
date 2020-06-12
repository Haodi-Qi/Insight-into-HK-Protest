import json
from collections import defaultdict

def gml_gen():
    for i in range(23,31):
        input_file_name = '2019-10-' + str(i) + '.txt'
        output_file_name = '2019-10-' + str(i) + '.gml'

        # From the input file (JSON objects),
        # retrieve only "text" and user "screen name"

        tweets_texts = []
        tweets_users = []
        tweets_file = open(input_file_name, "r")
        for line in tweets_file:
            try:
                tweet = json.loads(line)
                tweets_texts.append(tweet['text'].encode('utf-8'))
                tweets_users.append(tweet['user']['screen_name'])
            except:
                continue    

        # Check if tweets_texts list has some text
        print( len(tweets_texts) )

        # Start writing a GML output file
        output_file = open(output_file_name, "w")
        output_file.write("graph\n")
        output_file.write("[\n")

        # Loop through each line and extract from_user and to_user
        # e.g. from_user "retweets" from to_user
        counter = 0
        max_length = len(tweets_texts)
        pairwise_counter_dictionary = defaultdict(int)
        user_id = 0
        users = {}
        while counter < max_length:
            text = tweets_texts[counter]
            text = text.strip()
            text_tokens = text.split()

            from_user = tweets_users[counter]
            prev_token = ""
            for token in text_tokens:
                token = token.decode('utf-8')
                
                if prev_token == 'RT' and token.startswith('@'):
                    #print (token)
                    token = token.replace(":", "")
                    to_user = token.replace("@", "")
                    #print (from_user + ',' + to_user)

                    from_user_id = ""
                    to_user_id = ""
                    if (from_user in users) == False:
                        users[from_user] = user_id
                        user_id = user_id + 1
                    from_user_id = users[from_user]
                    if (to_user in users) == False:
                        users[to_user] = user_id
                        user_id = user_id + 1
                    to_user_id = users[to_user]

                    # increment counter
                    pairwise_counter_dictionary[from_user_id, to_user_id] += 1

                prev_token = token

            # while loop counter
            counter = counter + 1

        # print all nodes
        for key in users.keys():
            output_file.write("  node\n")
            output_file.write("  [\n")
            output_file.write("    id " + str(users[key]) + "\n")
            output_file.write("    label \"" + key + "\"" + "\n")
            output_file.write("  ]\n")

        # print all edges
        for keys in pairwise_counter_dictionary.keys():
            output_file.write("  edge\n")
            output_file.write("  [\n")
            output_file.write("    source " + str(keys[0]) + "\n")
            output_file.write("    target " + str(keys[1]) + "\n")
            output_file.write("    value " + str(pairwise_counter_dictionary[keys[0], keys[1]]) + "\n")
            output_file.write("  ]\n")

        output_file.write("]\n")
        output_file.close()

    return 
gml_gen()
