// scripts.js

function loadQuestionnaire() {
    const department = document.getElementById('department').value;
    const courseName = document.getElementById('courseName').value;

    // Update the HTML content with the questionnaire
    const questionnaireContainer = document.getElementById('questionnaireContainer');
    questionnaireContainer.innerHTML = '';
    
    // Fetch and include the questionnaire HTML file
    fetch(`questionnaire.html`)
        .then(response => response.text())
        .then(data => {
            questionnaireContainer.innerHTML = data;
            showQuestionnaire();
        })
        .catch(error => console.error('Error:', error));
}

function showQuestionnaire() {
    // Hide the department form
    document.getElementById('departmentForm').style.display = 'none';

    // Show the questionnaire
    document.getElementById('questionnaireContainer').style.display = 'block';
}

function submitForm() {
    // Collect answers, department, and course number
    const answers = {
        classSize: document.querySelector('input[name="classSize"]:checked').value,
        teachingStyle: document.querySelector('input[name="teachingStyle"]:checked').value,
        // Add more answers as needed
    };

    const department = document.getElementById('department').value;
    const courseName = document.getElementById('courseName').value;

    // Include department and course number in the answers
    answers.department = department;
    answers.courseName = courseName;

    // Make a request to the Python backend with the collected answers
    fetch('http://localhost:5000/api/process_answers', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(answers)
    })
        .then(response => response.json())
        .then(data => {
            // Handle the data received from the Python backend
            console.log(data.results);
            // Redirect to the output page with the results
            window.location.href = 'output.html';
        })
        .catch(error => console.error('Error:', error));
}
