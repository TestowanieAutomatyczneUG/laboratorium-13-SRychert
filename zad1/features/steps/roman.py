from behave import *
from src.roman import roman

use_step_matcher("re")


@given('there is roman')
def step_impl(context):
    context.roman = roman


@when('we pass 1')
def step_impl(context):
    context.result = context.roman(1)


@then('we get I as an result')
def step_impl(context):
    assert context.result == 'I'


@when('we pass 2')
def step_impl(context):
    context.result = context.roman(2)


@then('we get II as an result')
def step_impl(context):
    assert context.result == 'II'


@when('we pass 3')
def step_impl(context):
    context.result = context.roman(3)


@then('we get III as an result')
def step_impl(context):
    assert context.result == 'III'


@when('we pass 4')
def step_impl(context):
    context.result = context.roman(4)


@then('we get IV as an result')
def step_impl(context):
    assert context.result == 'IV'


@when('we pass 5')
def step_impl(context):
    context.result = context.roman(5)


@then('we get V as an result')
def step_impl(context):
    assert context.result == 'V'


@when('we pass 6')
def step_impl(context):
    context.result = context.roman(6)


@then('we get VI as an result')
def step_impl(context):
    assert context.result == 'VI'


@when('we pass 9')
def step_impl(context):
    context.result = context.roman(9)


@then('we get IX as an result')
def step_impl(context):
    assert context.result == 'IX'


@when('we pass 27')
def step_impl(context):
    context.result = context.roman(27)


@then('we get XXVII as an result')
def step_impl(context):
    assert context.result == 'XXVII'


@when('we pass 48')
def step_impl(context):
    context.result = context.roman(48)


@then('we get XLVIII as an result')
def step_impl(context):
    assert context.result == 'XLVIII'


@when('we pass 49')
def step_impl(context):
    context.result = context.roman(49)


@then('we get XLIX as an result')
def step_impl(context):
    assert context.result == 'XLIX'


@when('we pass 59')
def step_impl(context):
    context.result = context.roman(59)


@then('we get LIX as an result')
def step_impl(context):
    assert context.result == 'LIX'


@when('we pass 93')
def step_impl(context):
    context.result = context.roman(93)


@then('we get XCIII as an result')
def step_impl(context):
    assert context.result == 'XCIII'


@when('we pass 141')
def step_impl(context):
    context.result = context.roman(141)


@then('we get CXLI as an result')
def step_impl(context):
    assert context.result == 'CXLI'


@when('we pass 163')
def step_impl(context):
    context.result = context.roman(163)


@then('we get CLXIII as an result')
def step_impl(context):
    assert context.result == 'CLXIII'


@when('we pass 402')
def step_impl(context):
    context.result = context.roman(402)


@then('we get CDII as an result')
def step_impl(context):
    assert context.result == 'CDII'


@when('we pass 575')
def step_impl(context):
    context.result = context.roman(575)


@then('we get DLXXV as an result')
def step_impl(context):
    assert context.result == 'DLXXV'


@when('we pass 911')
def step_impl(context):
    context.result = context.roman(911)


@then('we get CMXI as an result')
def step_impl(context):
    assert context.result == 'CMXI'


@when('we pass 1024')
def step_impl(context):
    context.result = context.roman(1024)


@then('we get MXXIV as an result')
def step_impl(context):
    assert context.result == 'MXXIV'


@when('we pass 3000')
def step_impl(context):
    context.result = context.roman(3000)


@then('we get MMM as an result')
def step_impl(context):
    assert context.result == 'MMM'
