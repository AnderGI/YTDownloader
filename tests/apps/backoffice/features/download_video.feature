Feature: download video endpoint
  users want to download videos from youtube
  for that they will pass the start and end timestamp of a video as well as the video id
  moreover clients will be forced to use PUT method so they are the ones that generate the id 

  Scenario: happy path
    Given the user sends a PUT request to "/download/9ab393d9-03bf-42d2-8904-e60cdf557013" with body:
    """
    {
      "url": "https://www.youtube.com/watch?v=ig49C04bJt0",
      "start": {"hour":0, "minute": 0, "second": 30},
      "end": {"hour":0, "minute": 1, "second": 0}
    }
    """
    Then the response code should be 202

  Scenario: Valid start and end range but end range is lower than start rate
    Given the user sends a PUT request to "/download/9ab393d9-03bf-42d2-8904-e60cdf557013" with body:
    """
    {
      "url": "https://www.youtube.com/watch?v=ig49C04bJt0",
      "start": {"hour":0, "minute": 1, "second": 30},
      "end": {"hour":0, "minute": 0, "second": 30}
    }
    """
    Then the response code should be 406


  Scenario: invalid uuid in path variable
    Given the user sends a PUT request to "/download/aghctcghgctctcv" with body:
    """
    {
      "url": "https://www.youtube.com/watch?v=ig49C04bJt0",
      "start": {"hour":0, "minute": 0, "second": 30},
      "end": {"hour":0, "minute": 1, "second": 0}
    }
    """
    Then the response code should be 422

  Scenario: Negative hours
    Given the user sends a PUT request to "/download/9ab393d9-03bf-42d2-8904-e60cdf557013" with body:
    """
    {
      "url": "https://www.youtube.com/watch?v=ig49C04bJt0",
      "start": {"hour":-1, "minute": 0, "second": 30},
      "end": {"hour":-1, "minute": 0, "second": 0}
    }
    """
    Then the response code should be 422

  Scenario: Equal or above 24 hours
    Given the user sends a PUT request to "/download/9ab393d9-03bf-42d2-8904-e60cdf557013" with body:
    """
    {
      "url": "https://www.youtube.com/watch?v=ig49C04bJt0",
      "start": {"hour":25, "minute": 24, "second": 30},
      "end": {"hour":28, "minute": 0, "second": 0}
    }
    """
    Then the response code should be 422

  Scenario: Negative minutes 
    Given the user sends a PUT request to "/download/9ab393d9-03bf-42d2-8904-e60cdf557013" with body:
    """
    {
      "url": "https://www.youtube.com/watch?v=ig49C04bJt0",
      "start": {"hour":2, "minute": -2, "second": 30},
      "end": {"hour": 5, "minute": -54, "second": 0}
    }
    """
    Then the response code should be 422
  
 Scenario: Equal or above 60 minutes
    Given the user sends a PUT request to "/download/9ab393d9-03bf-42d2-8904-e60cdf557013" with body:
    """
    {
      "url": "https://www.youtube.com/watch?v=ig49C04bJt0",
      "start": {"hour":2, "minute": 60, "second": 30},
      "end": {"hour": 5, "minute": 874, "second": 0}
    }
    """
    Then the response code should be 422

  Scenario: Negative seconds
    Given the user sends a PUT request to "/download/9ab393d9-03bf-42d2-8904-e60cdf557013" with body:
    """
    {
      "url": "https://www.youtube.com/watch?v=ig49C04bJt0",
      "start": {"hour":2, "minute": 12, "second": -30},
      "end": {"hour": 5, "minute": 47, "second": -4}
    }
    """
    Then the response code should be 422

  Scenario: Equal or above 60 seconds
    Given the user sends a PUT request to "/download/9ab393d9-03bf-42d2-8904-e60cdf557013" with body:
    """
    {
      "url": "https://www.youtube.com/watch?v=ig49C04bJt0",
      "start": {"hour":2, "minute": 12, "second": 60},
      "end": {"hour": 5, "minute": 47, "second": 48}
    }
    """
    Then the response code should be 422
