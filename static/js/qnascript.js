$(document).ready(function() {
    $('#hide').hide();

    // Define the JSON object
    var data = {
        "question": "What is the capital of France?",
        "answers": [
            {
                "student_id": "2022BCSE035",
                "answer_text": "Paris"
            },
            {
                "student_id": "2021BITE075",
                "answer_text": "Paris"
            },
            {
                "student_id": "2022BCSE034",
                "answer_text": "Lyon"
            }
        ]
    };

    // Render the question
    $("#question").text(data.question);

    // Render the answers
    $.each(data.answers, function(index, answer) {
        $("#answers").append(`<li><h2 id="stid">${answer.student_id}</h2><p class="ans">${answer.answer_text}</p>
        </li>`);
    });
});


function showPopup() {
    $('.ask_form').css('display','flex');
    $('#hide').show();
    $('#show').hide();
}
function hidePopup() {
    $('.ask_form').css('display','none');
    $('#show').show();
    $('#hide').hide();
}