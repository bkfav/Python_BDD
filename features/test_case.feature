Feature: Register User
    @smoke
    Scenario: Navigate to home page
    When Navigate to url "http://automationexercise.com"
    Then Verify that home page is visible successfully 
        """
        Ensure that Home text color should be orange. 
        """
    
    @sainty
    Scenario: Open sign-up page
    When Click on "Signup / Login" button
    Then Verify "New User Signup!" is shown

    @regression
    Scenario Outline: Make the sign-up
    Given Enter "<name>" and "<email>" address
    When Click "Signup" button
    Then Verify that "ENTER ACCOUNT INFORMATION" is visible 
    Examples:
        | name | email | 
        | Tony Jaa  | tony.jaa@gmail.com  |
    