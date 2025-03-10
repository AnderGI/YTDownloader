Feature: download video endpoint
  users want to download videos from youtube
  for that they will pass the start and end timestamp of a video as well as the video id
  moreover clients will be forced to use PUT method so they are the ones that generate the id 

  Scenario: happy path
    Given the user sends a PUT request to "/download/9ab393d9-03bf-42d2-8904-e60cdf557013" with body:
    """
    {
      "url": "https://www.youtube.com/watch?v=ig49C04bJt0",
      "start_timestamp": "00:00:30",
      "end_timestamp": "00:01:00"
    }
    """
    Then the response code should be 202


  Scenario: invalid uuid in path variable
    Given the user sends a PUT request to "/download/aghctcghgctctcv" with body:
    """
    {
      "url": "https://www.youtube.com/watch?v=ig49C04bJt0",
      "start_timestamp": "00:00:30",
      "end_timestamp": "00:01:00"
    }
    """
    Then the response code should be 422


  Scenario: invalid url in json body request
    Given the user sends a PUT request to "/download/cf29d0d3-005c-4692-ad05-7d0fe64b2841" with body:
    """
    {
      "url": "lererererereñe",
      "start_timestamp": "00:00:30",
      "end_timestamp": "00:01:00"
    }
    """
    Then the response code should be 422
  
  Scenario: invalid start timestamp in json body request
    Given the user sends a PUT request to "/download/cf29d0d3-005c-4692-ad05-7d0fe64b2841" with body:
    """
    {
      "url": "https://www.youtube.com/watch?v=ig49C04bJt0",
      "start_timestamp": true,
      "end_timestamp": "00:01:00"
    }
    """
    Then the response code should be 422

  Scenario: invalid end timestamp in json body request
    Given the user sends a PUT request to "/download/cf29d0d3-005c-4692-ad05-7d0fe64b2841" with body:
    """
    {
      "url": "https://www.youtube.com/watch?v=ig49C04bJt0",
      "start_timestamp": "00:00:30",
      "end_timestamp": "lerelerelerele"
    }
    """
    Then the response code should be 422