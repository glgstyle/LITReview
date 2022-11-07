// document.getElementById("createReviewButton").onclick = function redirectToCreateReview() {
//     location.href = "/flow/create_review/";
//     };
// document.getElementById("createTicketButton").onclick = function redirectToCreateTicket() {
//     location.href = "/flow/create_ticket/";
//     };

// Page flow
// generate url with ticket_id value
// ticket_url = document.getElementById("createReviewFromTicketButton").value;

// let id = "createReviewFromTicketButton" + i;
// let element = document.getElementById(id);
// // work with element
// if (element) {
// ticket_url = element.value;
// console.log(ticket_url)
// ticket_url = "/flow/create_review_from_ticket/" + ticket_url + "/";
// element.onclick = function redirectToCreateReviewFromTicket() {
//     location.href = ticket_url;
//     };
// }

// // Getting the button element
// var review_button = document.getElementsByName("follow-ticket-id");
// // Looping over tables
// for (var i = 0; i < review_button.length; i++) {
//     // Get the ith ticket_button
//     var table = review_button[i];
//     table.id = "createReviewFromTicketButton";
//     table.id += i+1;
//     ticket_element = document.getElementById(table.id);
//     ticket_url = ticket_element.value;
//     console.log(ticket_url)
//     ticket_url = "/flow/create_review_from_ticket/" + ticket_url + "/";
//     ticket_element.onclick = function redirectToCreateReviewFromTicket() {
//     location.href = ticket_url;
// };
// }


// ticket_url = "/flow/create_review_from_ticket/" + ticket_url + "/";
// redirect to this ticket_id onclick 
// document.getElementById("createReviewFromTicketButton").onclick = function redirectToCreateReviewFromTicket() {
//     location.href = ticket_url;
//     };

// Page create_review_from_ticket
// set the star value in form on click submit
// document.getElementById("send-review-from-ticket").onclick = function setStarsValue() {
//     let elements = document.getElementsByName('star-rating');
//     for(i = 0; i < elements.length; i++) {
//         if(elements[i].checked & ele[i].value != 6)
//         myValue = elemets[i].value;
//         else if (elements[i].value == 6)
//         myValue = 5;
//         document.getElementById('result').setAttribute('value', myValue)
//     }
// }

function setStarsValue($event) {
    console.log("input target",$event.target)
    console.log("input target",$event.target.value)
    document.getElementById('result').setAttribute('value', $event.target.value)
    }
// }