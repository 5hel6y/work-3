
Caption = [
            {
             'ter': '11',
             'ber': '22',
             'ner': {
                     'a': '1',
                     'b': '2',
                     'c': '3',
                     'd': '4',
                     'e': '5'
                     }
             },
             {
             'ter': '11',
             'ber': '22',
             'ner': {
                     'a': '1',
                     'b': '2',
                     'c': '3',
                     'd': '4',
                     'e': '5'
                     }
             },
             {
             'ter': '11',
             'ber': '22',
             'ner': {
                     'a': '1',
                     'b': '2',
                     'c': '3',
                     'd': '4',
                     'e': '5'
                     }
             },
           ]


def listos():
    ners = []
    for item in Caption:
        ners.append(tuple(item["ner"].values()))
    for i in ners:
        print(i)


listos()
