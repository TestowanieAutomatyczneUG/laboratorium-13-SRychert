from behave import *
from src.Hamming import Hamming

use_step_matcher("parse")


@given("Hamming")
def step_impl(context):
    context.hamming = Hamming()


@given("Hamming string")
def step_impl(context):
    context.hamming = Hamming()
    context.gene1 = context.text.split(",")[0].replace("'", "")
    context.gene2 = context.text.split(",")[1].replace("'", "").replace("\r", "")


@given("gene1 {gene1}")
def step_impl(context, gene1):
    context.gene1 = gene1


@given("gene2 {gene2}")
def step_impl(context, gene2):
    context.gene2 = gene2


@when("calculate distance")
def step_impl(context):
    context.result = context.hamming.distance(context.gene1, context.gene2)


@then("distance is {result}")
def step_impl(context, result):
    assert context.result == int(result)


@when("calculate distance raises ValueError")
def step_impl(context):
    try:
        context.result = context.hamming.distance(context.gene1, context.gene2)
    except ValueError as ex:
        context.result = ex


@then("ValueError is raised")
def step_impl(context):
    assert isinstance(context.result, ValueError)
