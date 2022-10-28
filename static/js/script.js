document.getElementById("createReviewButton").onclick = function redirectToCreateReview() {
    location.href = "/flow/create_review/";
    };
document.getElementById("createTicketButton").onclick = function redirectToCreateTicket() {
    location.href = "/flow/create_ticket/";
    };

// Page flow
// generate url with ticket_id value
ticket_url = document.getElementById("createReviewFromTicketButton").value;
ticket_url = "/flow/create_review_from_ticket/" + ticket_url + "/";
// redirect to this ticket_id onclick 
document.getElementById("createReviewFromTicketButton").onclick = function redirectToCreateReviewFromTicket() {
    location.href = ticket_url;
    };

// Page create_review_from_ticket
// set the star value in form on click submit
document.getElementById("send-review-from-ticket").onclick = function setStarsValue() {
    let ele = document.getElementsByName('star-rating');
    for(i = 0; i < ele.length; i++) {
        if(ele[i].checked & ele[i].value != 6)
        myValue = ele[i].value;
        else if (ele[i].value == 6)
        myValue = 5;
        document.getElementById('result').setAttribute('value', myValue)
    }
}
