import csv

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

def predict_spam(does_have_links, does_have_spammy_words, length_of_text):
    if length_of_text <= 98:
        if does_have_links == "FALSE":
            return "ham"
        else:
            return "spam"
    else:
        if length_of_text > 98:
            if does_have_spammy_words == "FALSE":
                if does_have_links == "FALSE":
                    if length_of_text <= 151:
                        if length_of_text <= 142:
                            if length_of_text <= 137:
                                if length_of_text <= 136:
                                    return "ham"
                                else:
                                    return "spam"
                            else:
                                return "ham"
                        else:
                            if length_of_text <= 146:
                                if length_of_text <= 144:
                                    return "ham"
                                else:
                                    return "spam"
                            else:
                                return "ham"
                    else:
                        if length_of_text <= 160:
                            return "spam"
                        else:
                            if length_of_text <= 162:
                                return "spam"
                            else:
                                return "ham"
                else:
                    if length_of_text <= 172:
                        if length_of_text <= 130:
                            if length_of_text <= 123:
                                return "spam"
                            else:
                                if length_of_text <= 124:
                                    return "spam"
                                else:
                                    if length_of_text <= 129:
                                        return "ham"
                                    else:
                                        return "spam"
                        else:
                            return "spam"
                    else:
                        if length_of_text <= 194:
                            return "spam"
                        else:
                            return "ham"







def main():
    data = read_data_from_file()
    for row in data:
        sms_message = row[1]
        links = does_have_links(sms_message)
        spammy = does_have_spammy_words(sms_message)
        text_length = length_of_text(sms_message)
        outcome = predict_spam(links, spammy, text_length)
        print(outcome)

main()