Feature: roman

  Scenario: roman, 1
     Given there is roman
      When we pass 1
      Then we get I as an result

  Scenario: roman, 2
     Given there is roman
      When we pass 2
      Then we get II as an result

  Scenario: roman, 3
     Given there is roman
      When we pass 3
      Then we get III as an result

  Scenario: roman, 4
     Given there is roman
      When we pass 4
      Then we get IV as an result

  Scenario: roman, 5
     Given there is roman
      When we pass 5
      Then we get V as an result

  Scenario: roman, 6
     Given there is roman
      When we pass 6
      Then we get VI as an result

  Scenario: roman, 9
     Given there is roman
      When we pass 9
      Then we get IX as an result

  Scenario: roman, 27
     Given there is roman
      When we pass 27
      Then we get XXVII as an result

  Scenario: roman, 48
     Given there is roman
      When we pass 48
      Then we get XLVIII as an result

  Scenario: roman, 49
     Given there is roman
      When we pass 49
      Then we get XLIX as an result

  Scenario: roman, 59
     Given there is roman
      When we pass 59
      Then we get LIX as an result

  Scenario: roman, 93
     Given there is roman
      When we pass 93
      Then we get XCIII as an result

  Scenario: roman, 141
     Given there is roman
      When we pass 141
      Then we get CXLI as an result

  Scenario: roman, 163
     Given there is roman
      When we pass 163
      Then we get CLXIII as an result

  Scenario: roman, 402
     Given there is roman
      When we pass 402
      Then we get CDII as an result

  Scenario: roman, 575
     Given there is roman
      When we pass 575
      Then we get DLXXV as an result

  Scenario: roman, 911
     Given there is roman
      When we pass 911
      Then we get CMXI as an result

  Scenario: roman, 1024
     Given there is roman
      When we pass 1024
      Then we get MXXIV as an result

  Scenario: roman, 3000
     Given there is roman
      When we pass 3000
      Then we get MMM as an result
