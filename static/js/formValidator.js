// formValidator.js
class FormValidator {
    constructor(formId) {
        this.form = $(`#${formId}`);
        this.validationAlert = $('#validationAlert');
        this.validationAlert.hide();
    }

    validateField(field) {
        const note = field.val();  // Get the value from the textarea
        const minLength = parseInt(field.data('min-length'));
        const required = field.data('required');
        const requiredMessage = field.data('required-message');
        const minLengthMessage = field.data('min-length-message');

        const errors = [];

        if (required && !note) {
            errors.push(requiredMessage);
        }

        if (note.length < minLength) {
            errors.push(minLengthMessage);
        }

        return errors;
    }

    showErrors(errors) {
        if (errors.length > 0) {
            this.validationAlert.html(errors.join('<br>')).show();
        } else {
            this.validationAlert.hide();
        }
    }

    validate() {
        const noteField = this.form.find('#note');
        const errors = this.validateField(noteField);
        this.showErrors(errors);
        return errors.length === 0; // Return true if no errors
    }
}
