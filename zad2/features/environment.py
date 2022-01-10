from src.FizzBuzz import FizzBuzz


def before_scenario(context, scenario):
    context.fizz_buzz = FizzBuzz()


def after_scenario(context, scenario):
    context.fizz_buzz = None
