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

  const follow = document.getElementById('follow');
  follow.addEventListener('submit', (event) => {
    const user_to_follow = parseInt(event.target.profile.value);
    const csrftoken = getCookie('csrftoken')

    fetch("/api/follow/", {
      method: 'POST',
      mode: 'same-origin',
      headers: {'X-CSRFToken': csrftoken},
      body: JSON.stringify({
        'user_to_follow': user_to_follow
      })
    })
    .then(response => response.json())
    .then(data => {
      if (data['message'] == "Followed"){
        document.getElementById(`follow${user_to_follow}`).classList.add('btn-success')
        document.getElementById(`follow${user_to_follow}`).classList.remove('btn-primary')
        document.getElementById(`follow${user_to_follow}`).innerHTML = "Following"
      } else {
        document.getElementById(`follow${user_to_follow}`).classList.add('btn-primary')
        document.getElementById(`follow${user_to_follow}`).classList.remove('btn-success')
        document.getElementById(`follow${user_to_follow}`).innerHTML = "Follow"
      }
      console.log(data)
    })

    // stop form submitting
    event.preventDefault();
  })
})
