import csv

#read the spam csv file into a list
def read_data_from_file():
    data = []
    with open('spam.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # skip the first row
        next(csv_reader)
        for row in csv_reader:
            data.append(row)
    return data

def does_have_links(sms_message):
    a = "http"
    if a in sms_message:
        return "TRUE"
    return "FALSE"

def does_have_spammy_words(sms_message):
    spammy_words = ['WINNER','URGENT', 'FreeMsg', 'Congrats!', 'free', 'FREE', 'winner', 'PRIVATE!', 'URGENT!','4U', 'Free trial']
    words = sms_message.split(' ')
    for word in words:
        for spammy in spammy_words:
            if word == spammy:
                return "TRUE"
    return "FALSE"

def length_of_text(sms_message):
    length = len(sms_message)
    return length

#write features to a file
def write_features_to_file(text_length, does_have_spammy_words, does_have_links, class_label):
    # writing to csv file
    row = [text_length, does_have_spammy_words, does_have_links, class_label]
    # 'a' indicates append while w save eonly one row a time
    with open("features.csv", 'a', newline='', encoding='utf-8') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the data rows
        csvwriter.writerow(row)


#def predict_spam(len_of text, contain_link)
#   if len_of text >2300:
        #return "spam"
#    if contein_link == True:
        #return "spam"

def main():
    data = read_data_from_file()
    for row in data:
        sms_message = row[1]
        class_label = row[0]
        links = does_have_links(sms_message)
        spammy = does_have_spammy_words(sms_message)
        text_length =  length_of_text(sms_message)
        write_features_to_file(text_length, spammy, links, class_label)

    #contain one string
    #list[0] = ham, "Go until juntrong point crazy"
    #creat for loop
    #use split to split each list[]

    #list
    #call predict_spam

main()