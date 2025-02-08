Feature: Enter Value


  Scenario: Entering a value and checking that it is shown
    Given I am on the homepage and I click on the EnterSomeValue button
    When I fill the text 'Mircea'
    And I click on the submit button
    Then I check if the text submitted appears on the page