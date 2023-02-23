import json
import pandas as pd
import os


class Data:
    def __init__(self, json_files, name):
        self.cleaned = []
        self.total = 0
        self.avoid = ['select', 'which', 'the above']
        self.name = name
        if len(json_files) > 1:
            for file in json_files:
                self.f = open(file)
                self.json_file = json.load(self.f)
                self.f.close()
                if 'tqa' in file:
                    self.tqa()
                else:
                    self.science()
        self.save_json()

    def tqa(self):
        for each_dict in self.json_file:
            if each_dict['questions']['nonDiagramQuestions']:
                self.total += len(each_dict['questions']['nonDiagramQuestions'])
                for valid_question in each_dict['questions']['nonDiagramQuestions'].values():
                    try:
                        answer = valid_question['answerChoices'][valid_question['correctAnswer']['processedText']]['processedText']
                        if 'the above' not in answer and 'which' not in valid_question['beingAsked']['processedText']:
                            question = str(valid_question['beingAsked']['processedText'])
                            self.cleaned.append({
                                'tag': 'science',
                                'patterns': [question],
                                'responses': [answer]
                            })
                            self.total += 1
                    except KeyError:
                        pass
        # self.save_dataframe()
        # self.save_json()

    def save_dataframe(self):
        df = pd.DataFrame(self.cleaned)
        df.to_csv(f'{self.name}.csv', index=False)

    def save_json(self):
        final = {
            "intents": self.cleaned
        }
        json.dump(final, open(f'{self.name}.json', "w"))

    def science(self):
        for each_dict in self.json_file.keys():
            question = self.json_file[each_dict]['question'].lower()
            temp = True
            if self.json_file[each_dict]['image'] is None:
                for text in self.avoid:
                    if text in question:
                        temp = False
                        break
                if temp:
                    answer = self.json_file[each_dict]["choices"][self.json_file[each_dict]["answer"]]
                    print(f'patterns: {question}')
                    print(f'responses: {answer}')
                    self.cleaned.append({
                        'tag': 'science',
                        'patterns': [question],
                        'responses': [answer]
                    })
        # self.save_dataframe()


new_json = Data(['tqa_v1_train.json', 'tqa_v2_test.json', 'tqa_v1_val.json', 'problems.json'], 'final')
# new_json.tqa()  # clean and convert questions in TQA Dataset to csv file
# new_json.science()  # clean and convert questions in ScienceQA Dataset to csv file
# print(os.listdir())