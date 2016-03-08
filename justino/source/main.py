from question_answer import QA
from shape_checker import get_triangle_type, get_quad_type
from storyFunctions import *
from source.git_utils import *
import copy

import difflib
from datetime import datetime
NOT_A_QUESTION_RETURN = "Was that a question?"
UNKNOWN_QUESTION = "I don't know, please provide the answer"
NO_QUESTION = 'Please ask a question first'
NO_TEACH = 'I don\'t know about that. I was taught differently'
NO_CLEAR = 'I haven\'t been taught anything new to clear'

class Interface(object):
    def __init__(self):
        self.how_dict = {}
        self.what_dict = {}
        self.where_dict = {}
        self.who_dict = {}

        self.keywords = ['How', 'What', 'Where', 'Who', "Why", "Please", "Open", "Convert", "My", "Who\'s", "Is"]
        self.question_mark = chr(0x3F)  # ?
        self.exclamation_mark = chr(0x21)  # !
        self.period_mark = chr(0x2E)  # .

        self.question_answers = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_quad_type),
            'What time is it?': QA('What time is it? ', datetime.now().strftime('%m: %d: %y: %H:%M:%S')),
            'What is the n digit of fibonacci ': QA('What is the n digit of fibonacci ', fibonacci),
            'What is the n digit of pi ': QA('What is the n digit of pi ', npi),
            'What is the n digit of e ': QA('What is the n digit of e ', numE),
            'Please clear memory ': QA('Please clear memory ', self.clear_mem),
            'Open the door hal': QA('Open the door hal', rebuke_user),
            'What are numeric conversions ': QA('What are numeric conversions ', metric_display),
            'Convert to ': QA('Convert to ', metricConversion),
            'My favorite number is ': QA('My favorite number is ', fav_num),
            'What are color conversions ': QA('What are color conversion ', colorPrint),
            'What color does and make ': QA('What color does and make ', colorWheel),
            'Give me the n factorial of ': QA('Give me the n factorial of ', nFactorial),
            "Tell me a joke": QA("Tell me a joke", joke),
            'What is the square root of ': QA('What is the square root of', square_root),
            'What is the absolute value of ': QA('What is the absolute value of ', abs_value),
            'What is the hypotenuse of a right triangles who\'s side lengths are n and n': QA('What is the hypotenuse of a right triangles who\'s side lengths are 3 and 3', hypotenuse),
            'Who\'s that Pokemon ': QA('Who\'s that Pokemon ', pokemon),

            # Lab 5 additions
            'Is the <file path> in the repo?': QA('Is the <file path> in the repo?', check_valid_path)
        }
        # Used to restore question_answers after a clear memory command
        self.question_answers_COPY = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_quad_type),
            'What time is it?': QA('What time is it? ', datetime.now().strftime('%m: %d: %y: %H:%M:%S')),
            'What is the n digit of fibonacci ': QA('What is the n digit of fibonacci ', fibonacci),
            'What is the n digit of pi ': QA('What is the n digit of pi ', npi),
            'What is the n digit of e ': QA('What is the n digit of e ', numE),
            'Please clear memory ': QA('Please clear memory ', self.clear_mem),
            'Open the door hal': QA('Open the door hal', rebuke_user),
            'What are numeric conversions ': QA('What are numeric conversions ', metric_display),
            'Convert to ': QA('Convert to ', metricConversion),
            'My favorite number is ': QA('My favorite number is ', fav_num),
            'What are color conversions ': QA('What are color conversion ', colorPrint),
            'What color does and make ': QA('What color does and make ', colorWheel),
            'Give me the n factorial of ': QA('Give me the n factorial of ', nFactorial),
            "Tell me a joke": QA("Tell me a joke", joke),
            'What is the square root of ': QA('What is the square root of', square_root),
        }
        self.last_question = None

    def ask(self, question=""):
        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not A String!')

        if question[-1] != self.exclamation_mark and question[-1] != self.period_mark:
            if question[-1] != self.question_mark or question.split(' ')[0] not in self.keywords:
                self.last_question = None
                return NOT_A_QUESTION_RETURN

        parsed_question = ""
        args = []
        units = ['tera', 'giga', 'mega', 'kilo', 'hecto', 'deci', 'no_unit', 'deca', 'centi', 'milli', 'micro', 'nano', 'pico', 'yellow', 'blue', 'red']
        for keyword in question[:-1].split(' '):
            try:
                if keyword in units:
                    args.append(keyword)
                else:
                    args.append(float(keyword))
            except Exception as ex: #<---ADDED
                print ex #<---ADDED
                parsed_question += "{0} ".format(keyword)
        parsed_question = parsed_question[0:-1]
        self.last_question = parsed_question
        for answer in self.question_answers.values():
            if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                if answer.function is None:
                    return answer.value
                else:
                    return answer.function(*args)
        else:
            return UNKNOWN_QUESTION

    def teach(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        elif self.last_question in self.question_answers.keys():
            return NO_TEACH
        else:
            self.__add_answer(answer)

    def correct(self, answer=""):
        if self.last_question is None:
            return NO_QUESTION
        else:
            self.__add_answer(answer)

    def clear_mem(self):
        self.question_answers = {}
        self.question_answers = self.question_answers_COPY.copy()
        return 'Memory cleared'

    def __add_answer(self, answer):
        self.question_answers[self.last_question] = QA(self.last_question, answer)
