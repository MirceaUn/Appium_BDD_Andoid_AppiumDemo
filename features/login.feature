Feature: Sign In


  Scenario: Sign In with correct credentials
    Given I am on the homepage and I click on the LogIn button
    When I enter the username 'admin@gmail.com' and the password 'admin123'
    And I click on the login button
    When the admin page appears
    And I enter the text 'Mircea'
    Then I click on the Submit button