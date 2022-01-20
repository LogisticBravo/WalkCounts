document.addEventListener('DOMContentLoaded', (event) => {
    let goal = document.getElementById("id_goals");

    if((goal==null)){
        form = document.getElementById("goal-form");
        form.remove();

        let body = document.getElementById("goal-log");
        body.classList.remove("d-none");
        // body.insertAdjacentHTML("afterbegin", "<p>You have already set a Goal of {% if user.is_authenticated %} {{ user }} {% endif %} for the week!</p>");
    }
  })