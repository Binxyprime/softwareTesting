from main import Interface
from unittest import TestCase
from plugins.ReqTracer import requirements, story
from shape_checker import get_triangle_type, get_quad_type

import sys


class TestGetShapes(TestCase):

    # test requirements for asking a question beginning with 'How', 'What', 'Where', 'Why', and 'Who'
    # testing requirement #0006, #0007
    #0007 The system shall answer questions that begin with one of the following valid question keywords: "How", "What", "Where", "Why" and "Who"

    # what
    @requirements(['#0001', '#0002', '#0006', '#0007', '#0010', '#0013'])
    def test_ask_triangle_equilateral_what(self):
        obj = Interface()
        result = obj.ask('What type of triangle is 1.0 1 1?')
        self.assertEqual(result, 'equilateral')

    # who
    @requirements(['#0006', '#0007', '#0010', '#0014'])
    def test_ask_who(self):
        obj = Interface()
        result = obj.ask('Who was Abe Lincoln?')
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    # how
    @requirements(['#0006', '#0007', '#0010', '#0014'])
    def test_ask_how(self):
        obj = Interface()
        result = obj.ask('How did Abe Lincoln die?')
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    # where
    @requirements(['#0006', '#0007', '#0010', '#0014'])
    def test_ask_where(self):
        obj = Interface()
        result = obj.ask('Where did Abe Lincoln die?')
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    # why
    @requirements(['#0006', '#0007', '#0010', '#0014'])
    def test_ask_why(self):
        obj = Interface()
        result = obj.ask('Why did Abe Lincoln start killing vampires?')
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    #0008 If the system does not detect a valid question keyword it shall return "Was that a question?"

    # when
    @requirements(['#0006', '#0007', '#0008', '#0010'])
    def test_ask_when(self):
        obj = Interface()
        result = obj.ask('When did Abe Lincoln become president?')
        self.assertEqual(result, 'Was that a question?')

    #0009 If the system does not detect a question mark at end of the string it shall return "Was that a question?"
    @requirements(['#0006', '#0007', '#0009', '#0010'])
    def test_ask_no_question_mark(self):
        obj = Interface()
        result = obj.ask('Whats up')
        self.assertEqual(result, 'Was that a question?')

    #0010 The system shall break a question down into words separated by spaces
    @requirements(['#0006', '#0007', '#0008', '#0009', '#0010', '#0014'])
    def test_ask_no_spaces(self):
        obj = Interface()
        result = obj.ask('How,What,When,Where,Why,Who?')
        self.assertEqual(result, 'Was that a question?')

    @requirements(['#0006', '#0007', '#0009', '#0010', '#0014'])
    def test_ask_spaces(self):
        obj = Interface()
        result = obj.ask('How What When Where Why Who?')
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    #0011 The system shall determine an answer to a question as a correct if the keywords provide a 90% match and return the answer
    @requirements(['#0001', '#0002', '#0006', '#0007', '#0010', '#0011', '#0013'])
    def test_ask_triangle_equilateral_percentage(self):
        obj = Interface()
        result = obj.ask('What type triangle is 1.0 1 1?')
        self.assertEqual(result, 'equilateral')

    #0012 The system shall exclude any number value from match code and provide the values to generator function (if one exists)
    @requirements(['#0001', '#0002', '#0006', '#0007', '#0010', '#0011', '#0012', '#0013'])
    def test_ask_triangle_equilateral_number_match(self):
        obj = Interface()
        result = obj.ask('What type of 1 1 1.0 triangle is?')
        self.assertEqual(result, 'equilateral')

    #0013 When a valid match is determined the system shall return the answer
    @requirements(['#0001', '#0002', '#0006', '#0007', '#0010', '#0013'])
    def test_ask_triangle_equilateral_match(self):
        obj = Interface()
        result = obj.ask('What type of triangle is 1 1.0 1?')
        self.assertEqual(result, 'equilateral')

    #0014 When no valid match is determined the system shall return "I don't know, please provide the answer"
    @requirements(['#0006', '#0007', '#0010', '#0014'])
    def test_ask_dont_know(self):
        obj = Interface()
        result = obj.ask('Why did Abe Lincoln start killing vampires?')
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    #0015 The system shall provide a means of providing an answer to the previously asked question.
    @requirements(['#0006', '#0007', '#0010', '#0015', '#0016'])
    def test_provide_answer(self):
        obj = Interface()
        obj.ask('Why did Abe Lincoln start killing vampires?')
        obj.teach('Because Abe hates glitter')
        result = obj.ask('Why did Abe Lincoln start killing vampires?')
        self.assertEqual(result, 'Because Abe hates glitter')

    #0016 The system shall accept and store answers to previous questions in the form of a string or a function pointer and store it as the generator function.
    @requirements(['#0001', '#0002', '#0006', '#0007', '#0010', '#0013', '#0015', '#0016'])
    def test_ask_tri(self):
        obj = Interface()
        obj.ask('What type of t is 1.0 1 1?')
        obj.teach(get_triangle_type)
        result = obj.ask('What type of tri is 1.0 1 1?')
        self.assertEqual(result, 'equilateral')

    #0017 If no previous question has been asked the system shall respond with "Please ask a question first"
    @requirements(['#0001', '#0002', '#0006', '#0007', '#0010', '#0013', '#0016', '#0017'])
    def test_no_prev_question(self):
        obj = Interface()
        result = obj.teach('answer')
        self.assertEqual(result, 'Please ask a question first')

    #0018 If an attempt is made to provide an answer to an already answered question the system shall respond with "I don\'t know about that. I was taught differently" and not update the question
    @requirements(['#0006', '#0007', '#0010', '#0016', '#0018'])
    def test_provide_answer_already_asked(self):
        obj = Interface()
        obj.ask('Why did Abe Lincoln start killing vampires?')
        obj.teach('Because Abe hates glitter')
        result = obj.teach('Because Abe wants to add to his glitter collection')
        self.assertEqual(result, "I don\'t know about that. I was taught differently")

    @requirements(['#0006', '#0007', '#0010', '#0016', '#0018'])
    def test_provide_answer_already_asked2(self):
        obj = Interface()
        obj.ask('Why did Abe Lincoln start killing vampires?')
        obj.teach('Because Abe hates glitter')
        result = obj.teach('Because Abe hates glitter')
        self.assertEqual(result, "I don\'t know about that. I was taught differently")

    #0019 The system shall provide a means of updating an answer to the previously asked question.
    @requirements(['#0006', '#0007', '#0010', '#0015', '#0016', '#0019'])
    def test_provide_answer_corrected(self):
        obj = Interface()
        obj.ask('Why did Abe Lincoln start killing vampires?')
        obj.teach('Because Abe hates glitter')
        obj.correct('Because Abe wants to add to his glitter collection')
        result = obj.ask('Why did Abe Lincoln start killing vampires?')
        self.assertEqual(result, 'Because Abe wants to add to his glitter collection')

    # This code should return 'Square' but it can't because the arguments are cut off of obj.last_question.
    @requirements(['#0006', '#0007', '#0010', '#0015', '#0016', '#0019'])
    def test_provide_answer_corrected_square(self):
        obj = Interface()
        obj.ask('What type of flamingo is this 1 1 1 1?')
        obj.teach(get_triangle_type)
        obj.correct(get_quad_type)
        result = obj.ask(obj.last_question + '?')
        self.assertEqual(result, 'invalid')

    #0020 The system shall accept and store answers to previous questions in the form of a string or a function pointer and store it as the generator function.
    @requirements(['#0006', '#0007', '#0010', '#0015', '#0016', '#0020'])
    def test_provide_answer_corrected_sentence(self):
        obj = Interface()
        obj.ask('Why did Abe Lincoln start killing vampires?')
        obj.teach('Because Abe hates glitter')
        obj.correct('Because Abe wants to add to his glitter collection')
        result = obj.ask('Why did Abe Lincoln start killing vampires?')
        self.assertEqual(result, 'Because Abe wants to add to his glitter collection')

    @requirements(['#0003', '#0006', '#0007', '#0010', '#0015', '#0016', '#0020'])
    def test_provide_answer_corrected_square2(self):
        obj = Interface()
        obj.ask('What type of flamingo is this 1 1 1 1?')
        obj.teach(get_triangle_type)
        obj.correct(get_quad_type)
        result = obj.ask('What type of flamingo is this 1 1 1 1?')
        self.assertEqual(result, 'Square')

    #0021 If no previous question has been asked the system shall respond with "Please ask a question first"
    @requirements(['#0006', '#0007', '#0010', '#0013', '#0016', '#0017', '#0021'])
    def test_no_prev_question_corrected(self):
        obj = Interface()
        result = obj.correct('answer')
        self.assertEqual(result, "Please ask a question first")

    # Coverage
    def test_no_prev_question_not_a_string(self):
        obj = Interface()
        with self.assertRaises(Exception, msg='Not A String!'):
            obj.ask(1)

