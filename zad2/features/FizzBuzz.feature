Feature: FizzBuzz

  Scenario: FizzBuzz game, number 15
    When we pass 15
    Then we get FizzBuzz as result

  Scenario: FizzBuzz game, number 3
    When we pass 3
    Then we get Fizz as result

  Scenario: FizzBuzz game, number 5
    When we pass 5
    Then we get Buzz as result

  Scenario: FizzBuzz game, number 7
    When we pass 7
    Then we get "7" as result

  Scenario: FizzBuzz game, number 30
    When we pass 30
    Then we get FizzBuzz as result

  Scenario: FizzBuzz game, number 33
    When we pass 33
    Then we get Fizz as result

  Scenario: FizzBuzz game, number 35
    When we pass 35
    Then we get Buzz as result

  Scenario: FizzBuzz game, number 1890
    When we pass 1890
    Then we get FizzBuzz as result

  Scenario: FizzBuzz game, array
    When we pass array
    Then Exception is raised

  Scenario: FizzBuzz game, dict
    When we pass dict
    Then Exception is raised