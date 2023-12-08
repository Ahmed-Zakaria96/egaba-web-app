document.addEventListener('DOMContentLoaded', function(){

  // get csrftoken
  function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  // downvote
  const downVoteButtons = document.querySelectorAll('.q_downvote');
  downVoteButtons.forEach((button) => {
    button.addEventListener('submit', (e) => {
      const id = parseInt(e.target.button.value);
      const csrftoken = getCookie('csrftoken');


      fetch(`/api/q_down_vote/${id}/`, {
        method: 'POST',
        mode: 'same-origin',
        headers: {'X-CSRFToken': csrftoken}
      })
      .then(response => response.json())
      .then(data => {
        console.log(data)
        const downvoteColor = document.getElementById(`q_downvote${id}`)
        if (downvoteColor.classList.contains('text-danger')) {
          downvoteColor.classList.remove('text-danger')
        } else {
          downvoteColor.classList.add('text-danger')
        }
        document.getElementById(`q_upvote${id}`).classList.remove('text-success')
        const downvotecounter = document.getElementById(`q_votes${id}`)
        downvotecounter.innerHTML = data.votes;
      })

      // stop form submitting
      e.preventDefault();
    })
  })

  // upvote
  const upVoteButtons = document.querySelectorAll('.q_upvote');
  upVoteButtons.forEach((button) => {
    button.addEventListener('submit', (e) => {
      const id = parseInt(e.target.button.value);
      const csrftoken = getCookie('csrftoken');

      fetch(`/api/q_up_vote/${id}/`, {
        method: 'POST',
        mode: 'same-origin',
        headers: {'X-CSRFToken': csrftoken}
      })
      .then(response => response.json())
      .then(data => {
        console.log(data)
        const downvoteColor = document.getElementById(`q_upvote${id}`)
        if (downvoteColor.classList.contains('text-success')) {
          downvoteColor.classList.remove('text-success')
        } else {
          downvoteColor.classList.add('text-success')
        }
        document.getElementById(`q_downvote${id}`).classList.remove('text-danger')

        const downvotecounter = document.getElementById(`q_votes${id}`)
        downvotecounter.innerHTML = data.votes;
      })

      // stop form submitting
      e.preventDefault();
    })
  })
  // end of functions
})
