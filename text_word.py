def search_text(text, dic):
    for word in text.split():
    #for line in text:
        #for word in line.split():
        words_to_dict(word.lower(), dic)


def words_to_dict(word, dict):
    if word in dict:
        temp_value = dict[word]
        dict[word] = temp_value + 1
    else:
        dict[word] = 1


def most_common_word(dic):
    temp = 0
    word = None
    for k, v in dic.items():
        if v > temp:
            temp = v
            word = k

    return  word, temp





def main():
    dic = {}
    text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis fringilla nisi dolor, eu tempor elit aliquet'\
     'ornare. Aenean egestas lorem enim, a aliquam lorem egestas in. Etiam posuere purus imperdiet, auctor dolor iaculis' \
     ', blandit turpis. Mauris sed mattis tellus, quis euismod nibh. Pellentesque id dui quis felis aliquam interdum ut' \
      'elementum orci. Nullam luctus convallis turpis, sit amet commodo arcu efficitur vel. Cras vitae lectus eu libero' \
       'placerat blandit. In hac habitasse platea dictumst. Nulla facilisi. In vulputate ex in ornare consectetur. ' \
       'Suspendisse potenti. Pellentesque in ullamcorper augue. Pellentesque leo orci, tempus ac vestibulum a, pharetra' \
       'vel eros. Maecenas in elit varius, eleifend magna ut, lacinia est. Sed eget viverra est. Duis dui ipsum, dapibus' \
       'nec volutpat id, bibendum eget ligula.'

    search_text(text, dic)
    word, reptts = most_common_word(dic)

    print(f"Mosr kommon word is {word} with {reptts} repirs")


if __name__ == "__main__":
    main()