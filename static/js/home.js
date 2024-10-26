$(document).ready(function () {
    const formValidator = new FormValidator('questionForm'); // Create an instance of FormValidator

    $('#questionsContainer').hide();

    $('#questionForm').on('submit', async function (event) {
        event.preventDefault();  // Prevent the default form submission

        if (!formValidator.validate()) {
            return; // Stop if validation fails
        }

        // Get the value from the textarea
        const note = $('#note').val();

        // Make an AJAX POST request
        const response = await $.ajax({
            url: '/api/generate',
            type: 'POST',
            contentType: 'application/x-www-form-urlencoded',
            data: { note }  // Send the note as data
        });

        // Update the questions list
        const questionsList = $('#questionsList');
        questionsList.empty();  // Clear previous questions

        if (response.status === 'success') {
            $('#questionsContainer').show();  // Show the questions container
            response.questions.forEach(function (question) {
                questionsList.append($('<li>').text(question));  // Append each question as a list item
            });
        } else {
            formValidator.showErrors(response.errors);
        }
    });

    // Real-time validation while typing
    $('#note').on('input', function () {
        const noteField = $(this);
        const errors = formValidator.validateField(noteField); // Validate on input
        formValidator.showErrors(errors); // Show errors
    });
});
