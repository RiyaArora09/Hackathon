
console.log("Blaa");

// fetch('https://icanhazdadjoke.com/slack')
//     .then(data => data.json())
//     .then(jokeData => {
//         const jokeText = jokeData.attachments[0].text;
//         const assistElement = document.getElementById('assist');
//         assistElement.innerHTML = jokeText;
//     })

// try {
//   console.log("Document", document?.getElementsByClassName('emailBodyContainer--2Tdt5TmqVI'));
//   console.log("Document 2.0", document?.getElementsByClassName('emailBodyContainer--2Tdt5TmqVI')[0]?.textContent);
//   console.log("Content", document.getElementsByClassName('emailBodyContainer--2Tdt5TmqVI')[0].textContent,'gurvirqwerty');

// } catch(error) {
//   console.log("Error is ", error);
// }

var value = "Good morning Amazon support, my name is Alex Chapman I am a Level 3 Amazon flex deliverer with over 100 some blocks completed in over 5 months. I had a scheduled block on Sunday June 25th at 4:45am. I continuously have issues with the app freezing and glitching. I've wrote customer service about this situation previously. I've tried to refresh app numerous times and it kept doing the same thing. It caused me to completely miss my block and I don't want that to affect my standing. Could you all please correct that thank you";

fetch('http://127.0.0.1:5000/getResponse', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({ contact: value})
})
.then(response => {
    console.log("Response is", response);
    return response.json();
})
.then(data => {
  console.log("Data is :", data.message);
  console.log(data); // Handle the response data
  const assistElement = document.getElementById('assist');
  assistElement.innerHTML = data.message;
})
.catch(error => {
  console.error('Error:', error);
});



// fetch('http://127.0.0.1:5000')
//   .then(response => response.json())
//   .then(data => {
//     // const jokeText = jokeData.attachments[0].text;
//     console.log("Data is ", data)
//     const assistElement = document.getElementById('assist');
//     assistElement.innerHTML = data.message;
//   })
//   .catch(err => {
//     console.log("Error", err)
//   })


