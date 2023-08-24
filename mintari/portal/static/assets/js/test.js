$("#multipleValidation").validate({
    errorElement: "span",
    rules: {
      first_name: {
        required: true
      },
      last_name: {
        required: true
      },
      email: {
        required: true,
        email: true
      },
      password: {
        required: true,
        minlength: 6
      },
      confirm_password: {
        required: true,
        minlength: 6,
        equalTo: "#password"
      }
    },
    messages: {
      name: "Please enter your name",
      email: {
        required: "Enter your email",
        email: "Enter a valid email"
      },
      password: {
        required: "Enter your password",
        minlength: "Password should contain minimum 6 characters with at-least One Capital and one Number"
      },
      confirm_password: {
        required: "Enter your password",
        minlength: "Password should contain minimum 6 character",
        equalTo: "Did not match the password"
      }
    }
  });