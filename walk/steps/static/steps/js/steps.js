document.addEventListener('DOMContentLoaded', (event) => {
    let goal = document.getElementById("id_goals");

    if((goal==null)){
        form = document.getElementById("goal-form");
        form.remove();

        let body = document.getElementById("goal-log");
        body.classList.remove("d-none");
    };
    
    let steps = document.getElementById("id_steps");

    if((steps==null)){
        form = document.getElementById("steps-form");
        form.remove();

        let body = document.getElementById("steps-log");
        body.classList.remove("d-none");

        // body.insertAdjacentHTML("afterbegin", "<p>You have already set a Goal of {% if user.is_authenticated %} {{ user }} {% endif %} for the week!</p>");
    }

    let userSteps = document.getElementById("userSteps").innerText;
    let userGoal = document.getElementById("userGoal").innerText;
    let progressBar = document.getElementById('progressBar');
    let progressLabel = document.getElementById('progressLabel');

    userSteps = parseInt(userSteps);
    userGoal = parseInt(userGoal);

    let progress = (userSteps/userGoal);
    progress = (progress*100);
    progress = Math.round(progress)


    if(progress == NaN){
        result = '0%';
    }
    else{
        let result = progress+'%'
    
        progressBar.style.width=result;
        progressBar.innerText=result;

        progressLabel.innerText=result;
    }

    if(progress <= 25){
        progressBar.classList.remove('bg-info');
        progressBar.classList.add('bg-warning');
    }
    
  })