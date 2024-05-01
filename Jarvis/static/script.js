document.getElementById('activate-button').addEventListener('click', function() {
    // Simulate voice command (replace with actual speech recognition)
    var command = "get time";
  
    fetch('../jarvis/time', {
      method: 'POST'  // Specify POST method for consistency with backend
    })
    .then(response => response.json())
    .then(data => {
      console.log(data);  // Log the response data (time in this case)
      // Display the time on your webpage using DOM manipulation
    })
    .catch(error => console.error(error));
  });