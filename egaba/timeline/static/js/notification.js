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

  // read and un read notifications
  const notificationButtons = document.querySelectorAll('.notification-read');
  notificationButtons.forEach((button) => {
    button.addEventListener('submit', (e)=>{
      const csrftoken = getCookie('csrftoken');

      // grap notification id
      const id = parseInt(e.target.button.value)

      // change div background
      const notificationDiv = document.getElementById(`notification${id}`)
      if (notificationDiv.classList.contains('bg-light')){
        notificationDiv.classList.remove('bg-light');
        notificationDiv.classList.add('bg-white')
      } else {
        notificationDiv.classList.add('bg-light');
        notificationDiv.classList.remove('bg-white')
      }

      // mark as read or un read via ajax request
      fetch(`/api/notification_read/${id}/`, {
        method: 'POST',
        mode: 'same-origin',
        headers: {'X-CSRFToken': csrftoken}
      })
      .then(response => response.json())
      .then(data => console.log(data))

      // stop form submitting
      e.preventDefault();
    })
  })

})
