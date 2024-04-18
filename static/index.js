document.addEventListener("DOMContentLoaded", function() {
    const formWrappers = document.querySelectorAll(".form-wrapper");
  
    formWrappers.forEach(function(formWrapper) {
      formWrapper.style.opacity = 0;
      formWrapper.style.transform = "translateY(20px)";
      fadeIn(formWrapper);
    });
  
    function fadeIn(element) {
      let op = 0.1;
      const timer = setInterval(function() {
        if (op >= 1) {
          clearInterval(timer);
        }
        element.style.opacity = op;
        element.style.transform = "translateY(0)";
        op += op * 0.1;
      }, 20);
    }
  });
  