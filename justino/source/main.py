from question_answer import QA
from shape_checker import get_triangle_type, get_quad_type
from storyFunctions import date_time, fibonacci, npi, rebuke_user, metric_display, metricConversion, fav_num, \
    colorPrint,  colorWheel, nFactorial, square_root, abs_value, hypotenuse, joke, numE, pokemon
from git_utils import is_file_in_repo, get_file_info, get_git_file_info, get_repo_branch, get_repo_url
import time
import difflib

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
            'What time is it ': QA('What time is it ', date_time),
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
            'What is the hypotenuse of a right triangles who\'s side lengths are n and n': QA(
                'What is the hypotenuse of a right triangles who\'s side lengths are and ', hypotenuse),
            'Who\'s that Pokemon ': QA('Who\'s that Pokemon ', pokemon),

            # Lab 5 additions
            'Is the in the repo ': QA('Is the in the repo ', is_file_in_repo),
            'What is the status of ': QA('What is the status of ', get_git_file_info),
            'What is the deal with ': QA('What is the deal with ', get_file_info),
            'What branch is ': QA('What branch is ', get_repo_branch),
            'Where did come from ': QA('Where did come from ', get_repo_url),
        }
        # Used to restore question_answers after a clear memory command
        self.question_answers_COPY = {
            'What type of triangle is ': QA('What type of triangle is ', get_triangle_type),
            'What type of quadrilateral is ': QA('What type of quadrilateral is ', get_quad_type),
        }
        self.last_question = None

    def ask(self, question=""):
        start = time.clock()
        if not isinstance(question, str):
            self.last_question = None
            raise Exception('Not A String!')

        end = time.clock()
        clocktime = end - start
        if len(question) > 0:
            f = open('log.txt', 'a')
            f.write('QUESTION => ' + question + '\t\t' + str(clocktime) + '\n')
            f.close()

        if question[-1] != self.exclamation_mark and question[-1] != self.period_mark:
            if question[-1] != self.question_mark or question.split(' ')[0] not in self.keywords:
                self.last_question = None
                return NOT_A_QUESTION_RETURN

        parsed_question = ""
        args = []
        units = ['tera', 'giga', 'mega', 'kilo', 'hecto', 'deci', 'no_unit', 'deca', 'centi', 'milli', 'micro', 'nano',
                 'pico', 'yellow', 'blue', 'red']
        for keyword in question[:-1].split(' '):
            try:
                if keyword in units:
                    args.append(keyword)
                elif keyword[0] == '<' and keyword[-1] == '>':
                    args.append(keyword[1:-1])
                else:
                    args.append(float(keyword))
            except Exception as ex:  # <---ADDED
                print ex  # <---ADDED
                parsed_question += "{0} ".format(keyword)
        parsed_question = parsed_question[0:-1]
        self.last_question = parsed_question
        start = time.clock()
        for answer in self.question_answers.values():
            if difflib.SequenceMatcher(a=answer.question, b=parsed_question).ratio() >= .90:
                if answer.function is None:
                    end = time.clock()
                    clocktime = end - start
                    f = open('log.txt', 'a')
                    f.write('ANSWER => ' + answer.value + '\t\t' + str(clocktime) + '\n')
                    f.close()
                    return answer.value
                else:
                    end = time.clock()
                    clocktime = end - start
                    f = open('log.txt', 'a')
                    f.write('ANSWER => ' + str(answer.function(*args)) + '\t\t' + str(clocktime) + '\n')
                    f.close()
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

        return
