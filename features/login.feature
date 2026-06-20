@login
Feature: User Authentication

  Background:
    Given I navigate to the login page

  @smoke
  Scenario: Successful login with valid credentials
    When I log in with valid credentials
    Then I should be logged in

  @regression
  Scenario: Failed login with invalid credentials
    When I log in with username "invalid_user@test.com" and password "WrongPassword123!"
    Then I should see a login error message

  @regression
  Scenario: Failed login with no credentials provided
    When I log in with no credentials provided
    Then I should see a login error message
