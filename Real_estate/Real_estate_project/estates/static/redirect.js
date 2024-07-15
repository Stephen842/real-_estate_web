// Wait for 5 seconds and then redirect back to the previous page

setTimeout(function() {
    window.location.href = '../templates/pages/home.html'; // This line redirects the user to the home page
}, 5000); // 5000 milliseconds = 5 seconds

