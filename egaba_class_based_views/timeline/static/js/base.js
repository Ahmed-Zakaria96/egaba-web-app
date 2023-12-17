document.addEventListener('DOMContentLoaded', function(){

  // open socket connection
  const NotificationSocket = new WebSocket(
      'ws://'
      + window.location.host
      + '/ws/notification/'
  );

  NotificationSocket.onmessage = function(e) {
      console.log('test')
      const data = JSON.parse(e.data);
      const notification = document.getElementById('notification');
      notification.classList.add('text-danger');
      document.getElementById('notification_count').hidden = false
      document.getElementById('notification_count').innerHTML = data.count
      console.log(data);
  };

  NotificationSocket.onclose = function(e) {
      console.error('Chat socket closed unexpectedly');
  };
})
