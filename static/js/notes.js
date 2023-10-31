var subjects;
var subject;
function redir(i){
  window.location.href = subject[i][1];
}

$(document).ready(function () {
  fetch("static/js/data.json")
    .then((response) => response.json())
    .then((data) => {
      subjects = data;
      console.log(data);
    })
    .catch((error) => console.error("Error:", error));

  $("#branch").change(function () {
    var choice = $("#var_select").val();
    var branch = $("#branch").val();
    subject = subjects[branch]["" + choice];
    $(".link").remove();
    
    // render the notes according to the year and branch
      for (let i = 0; i < 6; i++) {
        $("#rendered_data").append(`<div class="link">
        <div class="link_innerWrap">
          <h1>${subject[i][0]}</h1>
          <button class="para_link btn btn-outline-success"
            onclick='redir(${i})'>Download</button>
        </div>
        
      </div>`);
      }
  });
});
