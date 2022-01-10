from behave import *

use_step_matcher("re")


@when('we pass 15')
def step_impl(context):
    context.result = context.fizz_buzz.game(15)


@then("we get FizzBuzz as result")
def step_impl(context):
    assert context.result == "FizzBuzz"


@when('we pass 3')
def step_impl(context):
    context.result = context.fizz_buzz.game(3)


@then("we get Fizz as result")
def step_impl(context):
    assert context.result == "Fizz"


@when('we pass 5')
def step_impl(context):
    context.result = context.fizz_buzz.game(5)


@then("we get Buzz as result")
def step_impl(context):
    assert context.result == "Buzz"


@when('we pass 7')
def step_impl(context):
    context.result = context.fizz_buzz.game(7)


@then('we get "7" as result')
def step_impl(context):
    assert context.result == '"7"'


@when('we pass 30')
def step_impl(context):
    context.result = context.fizz_buzz.game(30)


@when('we pass 33')
def step_impl(context):
    context.result = context.fizz_buzz.game(33)


@when('we pass 35')
def step_impl(context):
    context.result = context.fizz_buzz.game(35)


@when('we pass 1890')
def step_impl(context):
    context.result = context.fizz_buzz.game(1890)


@when('we pass array')
def step_impl(context):
    try:
        context.result = context.fizz_buzz.game(object)
    except Exception as ex:
        context.result = ex


@then("Exception is raised")
def step_impl(context):
    assert isinstance(context.result, Exception)


@when('we pass dict')
def step_impl(context):
    try:
        context.result = context.fizz_buzz.game(object)
    except Exception as ex:
        context.result = ex
