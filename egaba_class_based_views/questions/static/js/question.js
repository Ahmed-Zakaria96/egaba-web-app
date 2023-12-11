document.addEventListener("DOMContentLoaded", function() {

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
  const adownVoteButtons = document.querySelectorAll('.a_downvote');
  adownVoteButtons.forEach((button) => {
    button.addEventListener('submit', (e) => {
      const id = parseInt(e.target.button.value);
      const csrftoken = getCookie('csrftoken');

      fetch(`/api/a_down_vote/${id}/`, {
        method: 'POST',
        mode: 'same-origin',
        headers: {'X-CSRFToken': csrftoken}
      })
      .then(response => response.json())
      .then(data => {
        console.log(data)
        const downvoteColor = document.getElementById(`a_downvote${id}`)
        if (downvoteColor.classList.contains('text-danger')) {
          downvoteColor.classList.remove('text-danger')
        } else {
          downvoteColor.classList.add('text-danger')
        }
        document.getElementById(`a_upvote${id}`).classList.remove('text-success')
        document.getElementById(`a_upvote${id}`).classList.add('text-secondary')
        const downvotecounter = document.getElementById(`a_votes${id}`)
        downvotecounter.innerHTML = data.votes;
      })

      // stop form submitting
      e.preventDefault();
    })
  })

  // upvote
  const aupVoteButtons = document.querySelectorAll('.a_upvote');
  aupVoteButtons.forEach((button) => {
    button.addEventListener('submit', (e) => {
      const id = parseInt(e.target.button.value);
      const csrftoken = getCookie('csrftoken');

      fetch(`/api/a_up_vote/${id}/`, {
        method: 'POST',
        mode: 'same-origin',
        headers: {'X-CSRFToken': csrftoken}
      })
      .then(response => response.json())
      .then(data => {
        const downvoteColor = document.getElementById(`a_upvote${id}`)
        if (downvoteColor.classList.contains('text-success')) {
          downvoteColor.classList.remove('text-success')
        } else {
          downvoteColor.classList.add('text-success')
        }
        document.getElementById(`a_downvote${id}`).classList.remove('text-danger')
        document.getElementById(`a_downvote${id}`).classList.add('text-secondary')

        const downvotecounter = document.getElementById(`a_votes${id}`)
        downvotecounter.innerHTML = data.votes;
      })

      // stop form submitting
      e.preventDefault();
    })
  })
  // end
})
