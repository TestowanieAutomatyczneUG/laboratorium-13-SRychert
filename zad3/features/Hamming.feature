Feature: Hamming

    @empty @and
    Scenario: Hamming, empty
        Given Hamming
        And gene1 ""
        And gene2 ""
        When calculate distance
        Then distance is 0

    @same_len @identical @and @short
    Scenario: Hamming, genes same length, identical, short
        Given Hamming
        And gene1 "A"
        And gene2 "A"
        When calculate distance
        Then distance is 0

    @same_len @identical @and @long
    Scenario: Hamming, genes same length, identical, long
        Given Hamming
        And gene1 "GGACTGAAATCTG"
        And gene2 "GGACTGAAATCTG"
        When calculate distance
        Then distance is 0

    @same_len @diff @and @short
    Scenario: Hamming, genes same length, different combination, short
        Given Hamming
        And gene1 "G"
        And gene2 "T"
        When calculate distance
        Then distance is 1

    @same_len @diff @and @long
    Scenario: Hamming, genes same length, different combination, long
        Given Hamming
        And gene1 "GGACGGATTCTG"
        And gene2 "AGGACGGATTCT"
        When calculate distance
        Then distance is 9

    @diff_len @string @short @left
    Scenario: Hamming, genes diff length, different combination, long
        Given Hamming string
        '''
        'AATG','AAA'
        '''
        When calculate distance raises ValueError
        Then ValueError is raised

    @diff_len @string @short @right
    Scenario: Hamming, genes same length, different combination, long
        Given Hamming string
        '''
        'ATG','AAAA'
        '''
        When calculate distance raises ValueError
        Then ValueError is raised

    @diff_len @string @short @empty @left
    Scenario: Hamming, genes same length, different combination, long
        Given Hamming string
        '''
        '','AAAA'
        '''
        When calculate distance raises ValueError
        Then ValueError is raised

    @diff_len @string @short @empty @right
    Scenario: Hamming, genes same length, different combination, long
        Given Hamming string
        '''
        'ATG',''
        '''
        When calculate distance raises ValueError
        Then ValueError is raised

    @same_len @identical @long
    Scenario: Hamming, genes same length, identical, long
        Given Hamming string
        '''
        'GGACTGAAATCTG','GGACTGAAATCTG'
        '''
        When calculate distance
        Then distance is 0
