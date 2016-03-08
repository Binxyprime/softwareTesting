from source.main import Interface
from unittest import TestCase
from test.plugins.ReqTracer import story
from datetime import datetime
import getpass
from storyFunctions import *
from storyFunctions import npi
from shape_checker import get_triangle_type, get_quad_type


class TestGetStoryCases(TestCase):

    # time
    @story('When I ask "What time is it?" I want to be given the current date/time so I can stay up to date')
    def test_story_ask_datetime(self):
        obj = Interface()
        result = obj.ask('What time is it?')
        self.assertEqual(result, datetime.now().strftime('%m: %d: %y: %H:%M:%S'))

    # fibonacci
    @story('When I ask "What is the n digit of fibonacci" I want to receive the answer so I don\'t have to figure it out myself')
    def test_story_ask_fib(self):
        obj = Interface()
        result = obj.ask("What is the 5 digit of fibonacci?")
        self.assertEqual(result, 5)

    # Pi up to 100 places
    @story('When I ask "What is the n digit of pi" I want to receive the answer so I don\'t have to figure it out myself')
    def test_story_ask_npi(self):
        obj = Interface()
        result = obj.ask("What is the 11 digit of pi?")
        self.assertEqual(result, 5)

    @story('When I ask "What is the n digit of pi" I want to receive the answer so I don\'t have to figure it out myself')
    def test_story_ask_npi_one(self):
        obj = Interface()
        result = obj.ask("What is the 1 digit of pi?")
        self.assertEqual(result, 3)

    @story('When I ask "What is the n digit of pi" I want to receive the answer so I don\'t have to figure it out myself')
    def test_story_ask_npi_zero(self):
        obj = Interface()
        result = obj.ask("What is the 0 digit of pi?")
        self.assertEqual(result, 'Invalid index for pi')

    # open the door
    @story('When I say "Open the door hal", I want the application to say "I\'m afraid I can\'t do that <user name> so I know that is not an option')
    def test_story_open_door_hal(self):
        obj = Interface()
        result = obj.ask("Open the door hal?")
        self.assertEqual(result, 'I\'m afraid I can\'t do that <' + getpass.getuser() + '>')

    # unit conversions
    @story('When I ask for a numeric conversion I want at least 10 different units I can convert from/to')
    def test_story_ten_unit_conversions(self):
        obj = Interface()
        result = obj.ask("What are numeric conversions?")
        self.assertEqual(result, 'tera = 6, giga = 5, mega = 4, kilo = 3, deca = 1, no_unit = 0, deci = -1, centi = -2, '
           '\n milli = -3, micro = -4, nano = -5, pico = -6; '
           '\n Format = "Convert <value> <unit> to <unit to convert to>"')

    # this tests that algorithm gives correct results
    @story('When I ask for a numeric conversion I want at least 10 different units I can convert from/to')
    def test_story_unit_conversions_test(self):
        result = metricConversion(100000, 'deci', 'deca')
        self.assertEqual(result, '1000.0 deca')

    # clear memory
    @story('When I ask "Please clear memory" I was the application to clear user set questions and answers so I can reset the application')
    def test_story_clear_mem(self):
        obj = Interface()
        result = obj.ask("Please clear memory?")
        self.assertEqual(result, 'Memory cleared')

    @story('When I ask "Please clear memory" I was the application to clear user set questions and answers so I can reset the application')
    def test_story_clear_mem_teach(self):
        obj = Interface()
        obj.ask('Why did Abe Lincoln start killing vampires?')
        obj.teach('Because Abe hates glitter')
        obj.ask('Why did Abe Lincoln start killing vampires?')
        obj.ask("Please clear memory?")
        result = obj.ask('Why did Abe Lincoln start killing vampires?')
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    # this test verifies that obj retains its original settings after a clear
    @story('When I ask "Please clear memory" I was the application to clear user set questions and answers so I can reset the application')
    def test_ask_triangle_equilateral_clear_mem(self):
        obj = Interface()
        obj.ask('Please clear memory?')
        result = obj.ask('What type of triangle is 1.0 1 1?')
        self.assertEqual(result, 'equilateral')

    # conversion value
    @story('When I ask "Convert <number> <units> to <units>" I want to receive the converted value and units so I can know the answer.')
    def test_story_convert_number_to_unit(self):
        obj = Interface()
        result = obj.ask("Convert 10 deci to deca?")
        self.assertEqual(result, '0.1 deca')

    @story('When I ask "Convert <number> <units> to <units>" I want to receive the converted value and units so I can know the answer.')
    def test_story_convert_number_to_unit_period_punctuation(self):
        obj = Interface()
        result = obj.ask("Convert 10 deci to deca.")
        self.assertEqual(result, '0.1 deca')

    # home-made requirements

    # fav number
    @story('When I tell the system "My favorite number is <number>" I want to be mocked to remind myself I am just a man.')
    def test_story_favorite_number(self):
        obj = Interface()
        result = obj.ask('My favorite number is 5.')
        self.assertEqual(result, 'The number 5 is a dumb number.')

    # e
    @story('When I ask "What is the n digit of e" I want to receive the answer so I don\'t have to figure it out myself')
    def test_story_ask_e(self):
        obj = Interface()
        result = obj.ask("What is the 5 digit of e?")
        self.assertEqual(result, 2)

    @story('When I ask "What is the n digit of e" I want to receive the answer so I don\'t have to figure it out myself')
    def test_story_ask_e_bad_index(self):
        obj = Interface()
        result = obj.ask("What is the 0 digit of e?")
        self.assertEqual(result, 'Invalid index for e')

    # color wheel
    @story('When I ask "What are color conversions" I want to know what colors I am allowed to mix.')
    def test_story_color_list(self):
        obj = Interface()
        result = obj.ask("What are color conversions?")
        self.assertEqual(result, 'yellow, red, and blue are the primary colors available for mixing')

    # color
    @story('When I ask "What color does <color> and <color> make?" I want the system to tell me so I don\'t have to get my hands dirty.')
    def test_story_color_paint1(self):
        obj = Interface()
        result = obj.ask("What color does blue and yellow make?")
        self.assertEqual(result, 'green')

    @story('When I ask "What color does <color> and <color> make?" I want the system to tell me so I don\'t have to get my hands dirty.')
    def test_story_color_paint2(self):
        obj = Interface()
        result = obj.ask("What color does blue and blue make?")
        self.assertEqual(result, 'blue')

    @story('When I ask "What color does <color> and <color> make?" I want the system to tell me so I don\'t have to get my hands dirty.')
    def test_story_color_paint3(self):
        obj = Interface()
        result = obj.ask("What color does blue and red make?")
        self.assertEqual(result, 'violet')

    @story('When I ask "What color does <color> and <color> make?" I want the system to tell me so I don\'t have to get my hands dirty.')
    def test_story_color_paint4(self):
        obj = Interface()
        result = obj.ask("What color does yellow and yellow make?")
        self.assertEqual(result, 'yellow')

    @story('When I ask "What color does <color> and <color> make?" I want the system to tell me so I don\'t have to get my hands dirty.')
    def test_story_color_paint5(self):
        obj = Interface()
        result = obj.ask("What color does yellow and red make?")
        self.assertEqual(result, 'orange')

    @story('When I ask "What color does <color> and <color> make?" I want the system to tell me so I don\'t have to get my hands dirty.')
    def test_story_color_paint6(self):
        obj = Interface()
        result = obj.ask("What color does yellow and blue make?")
        self.assertEqual(result, 'green')

    @story('When I ask "What color does <color> and <color> make?" I want the system to tell me so I don\'t have to get my hands dirty.')
    def test_story_color_paint7(self):
        obj = Interface()
        result = obj.ask("What color does red and yellow make?")
        self.assertEqual(result, 'orange')

    @story('When I ask "What color does <color> and <color> make?" I want the system to tell me so I don\'t have to get my hands dirty.')
    def test_story_color_paint8(self):
        obj = Interface()
        result = obj.ask("What color does red and red make?")
        self.assertEqual(result, 'red')

    @story('When I ask "What color does <color> and <color> make?" I want the system to tell me so I don\'t have to get my hands dirty.')
    def test_story_color_paint9(self):
        obj = Interface()
        result = obj.ask("What color does red and blue make?")
        self.assertEqual(result, 'violet')

    # factorial
    @story('When I say "Give me the n factorial of <number>." I want it to return it so I don\'t have to calculate it.')
    def test_story_factorial(self):
        obj = Interface()
        result = obj.ask("Give me the n factorial of 5.")
        self.assertEqual(result, 120)

    # joke
    @story('When I say "tell me a joke" I want to be told an incredibly poor joke')
    def test_story_joke(self):
        obj = Interface()
        result = obj.ask("Tell me a joke!")
        self.assertEqual(result, "To whoever took my Microsoft Office: I will find you. You have my Word.")

    # square root
    @story('When I ask "What is the square root of n" I want to be told it instead of getting a calculator.')
    def test_story_square_root(self):
        obj = Interface()
        result = obj.ask('What is the square root of 4?')
        self.assertEqual(result, 2)

    @story('if I tell the system to "give me absolute value of <number>" I want it to tell me')
    def test_story_absolute_value_neg(self):
        obj = Interface()
        result = obj.ask('What is the absolute value of -5?')
        self.assertEqual(result, 5)

    @story('if I tell the system to "give me absolute value of <number>" I want it to tell me')
    def test_story_absolute_value(self):
        obj = Interface()
        result = obj.ask('What is the absolute value of 5?')
        self.assertEqual(result, 5)

    @story('If I ask "What is the hypotenuse of a right triangles who\'s side lengths are <length> and <length>" I want an answer')
    def test_story_hypotenuse(self):
        obj = Interface()
        result = obj.ask('What is the hypotenuse of a right triangles who\'s side lengths are 3 and 3?')
        self.assertEqual(result, 4.242640687119285)

    @story('Who\'s that Pokemon!?')
    def test_story_whos_that_pokemon(self):
        obj = Interface()
        result = obj.ask('Who\'s that Pokemon?')
        self.assertEqual(result, 'Snorlax, and hes too tired to program anymore today')