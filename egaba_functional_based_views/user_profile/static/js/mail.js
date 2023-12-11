document.addEventListener('DOMContentLoaded', function() {

	tinymce.init({
		selector: '.editor',
		setup: function(editor) {
			editor.on('change', function() {
				tinymce.triggerSave();
			});
		},
		height: 300,
		menubar: false,
		plugins: [
			'advlist autolink lists link image charmap print preview anchor',
			'searchreplace visualblocks code fullscreen',
			'insertdatetime media table paste code help wordcount',
			'codesample'
		],
		toolbar: 'undo redo | formatselect | ' + ' codesample ' +
			'bold italic backcolor | alignleft aligncenter ' +
			'alignright alignjustify | bullist numlist outdent indent | ' +
			'removeformat',
		content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }'
	});

	const users = document.querySelectorAll('.user_button');
	for (let i = 0; i < users.length; i++) {
		users[i].addEventListener('click', (e) => {
			document.getElementById("mail_body").innerHTML = "";
			const user_id = parseInt(e.target.dataset.id);
			const mail_box = e.target.dataset.mail;
			if (mail_box == 'inbox') {
				fetch(`../inbox_person_mails/${user_id}`)
				.then(response => response.json())
				.then(mails => {
						mails.forEach((mail, i) => {
							const mail_row = document.createElement('tr');
							let mail_data = `<td>${i+1}</td>
										<td>${mail.subject}</td>
										<td>${mail.date}</td>
										<td>
											<a href="/profile/mail/archeive/${mail.id}" onClick="event.stopPropagation();" class="btn btn-secondary p-1">
												<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-archive" viewBox="0 0 16 16">
													<path
													 d="M0 2a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1v7.5a2.5 2.5 0 0 1-2.5 2.5h-9A2.5 2.5 0 0 1 1 12.5V5a1 1 0 0 1-1-1V2zm2 3v7.5A1.5 1.5 0 0 0 3.5 14h9a1.5 1.5 0 0 0 1.5-1.5V5H2zm13-3H1v2h14V2zM5 7.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5z" />
												</svg>
											</a>
												<button type="button" class="btn btn-danger p-1" onClick="event.stopPropagation();" data-bs-toggle="modal" data-bs-target="#delete_mail${mail.id}">
													<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eraser" viewBox="0 0 16 16">
														<path
														 d="M8.086 2.207a2 2 0 0 1 2.828 0l3.879 3.879a2 2 0 0 1 0 2.828l-5.5 5.5A2 2 0 0 1 7.879 15H5.12a2 2 0 0 1-1.414-.586l-2.5-2.5a2 2 0 0 1 0-2.828l6.879-6.879zm2.121.707a1 1 0 0 0-1.414 0L4.16 7.547l5.293 5.293 4.633-4.633a1 1 0 0 0 0-1.414l-3.879-3.879zM8.746 13.547 3.453 8.254 1.914 9.793a1 1 0 0 0 0 1.414l2.5 2.5a1 1 0 0 0 .707.293H7.88a1 1 0 0 0 .707-.293l.16-.16z" />
													</svg>
												</button>

												<!-- modal -->
												<div class="modal fade" id="delete_mail${mail.id}" tabindex="-1" aria-labelledby="delete_post_model" aria-hidden="true">
													<div class="modal-dialog">
														<div class="modal-content">
															<div class="modal-header">
																<h5 class="modal-title" id="exampleModalLabel">Delete Post</h5>
																<button type="button" onClick="event.stopPropagation();" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
															</div>
															<div class="modal-body">
																Are you sure you want to delete this mail?
															</div>
															<div class="modal-footer">
																<button type="button" onClick="event.stopPropagation();" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
																<a href="/profile/mail/delete/${mail.id}" class="btn btn-danger">Delete</a>
															</div>
														</div>
													</div>
												</div>
										</td>`

							mail_row.innerHTML = mail_data
							mail_row.addEventListener('click', ()=>{
								document.location.href = `/profile/mail/${mail.id}`;

							})
							document.getElementById("mail_body").append(mail_row);
						})
					})
			} else if (mail_box == 'sent') {
				fetch(`../sent_person_mails/${user_id}`)
				.then(response => response.json())
				.then(mails => {
						mails.forEach((mail, i) => {
							const mail_row = document.createElement('tr');
							let mail_data = `<td>${i+1}</td>
										<td>${mail.subject}</td>
										<td>${mail.date}</td>
										<td>
											<a href="/profile/mail/archeive/${mail.id}" onClick="event.stopPropagation();" class="btn btn-secondary p-1">
												<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-archive" viewBox="0 0 16 16">
													<path
													 d="M0 2a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1v7.5a2.5 2.5 0 0 1-2.5 2.5h-9A2.5 2.5 0 0 1 1 12.5V5a1 1 0 0 1-1-1V2zm2 3v7.5A1.5 1.5 0 0 0 3.5 14h9a1.5 1.5 0 0 0 1.5-1.5V5H2zm13-3H1v2h14V2zM5 7.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5z" />
												</svg>
											</a>
												<button type="button" onClick="event.stopPropagation();" class="btn btn-danger p-1" data-bs-toggle="modal" data-bs-target="#delete_mail${mail.id}">
													<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eraser" viewBox="0 0 16 16">
														<path
														 d="M8.086 2.207a2 2 0 0 1 2.828 0l3.879 3.879a2 2 0 0 1 0 2.828l-5.5 5.5A2 2 0 0 1 7.879 15H5.12a2 2 0 0 1-1.414-.586l-2.5-2.5a2 2 0 0 1 0-2.828l6.879-6.879zm2.121.707a1 1 0 0 0-1.414 0L4.16 7.547l5.293 5.293 4.633-4.633a1 1 0 0 0 0-1.414l-3.879-3.879zM8.746 13.547 3.453 8.254 1.914 9.793a1 1 0 0 0 0 1.414l2.5 2.5a1 1 0 0 0 .707.293H7.88a1 1 0 0 0 .707-.293l.16-.16z" />
													</svg>
												</button>

												<!-- modal -->
												<div class="modal fade" id="delete_mail${mail.id}" tabindex="-1" aria-labelledby="delete_post_model" aria-hidden="true">
													<div class="modal-dialog">
														<div class="modal-content">
															<div class="modal-header">
																<h5 class="modal-title" id="exampleModalLabel">Delete Post</h5>
																<button type="button" onClick="event.stopPropagation();" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
															</div>
															<div class="modal-body">
																Are you sure you want to delete this mail?
															</div>
															<div class="modal-footer">
																<button type="button" onClick="event.stopPropagation();" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
																<a href="/profile/mail/delete/${mail.id}" onClick="event.stopPropagation();" class="btn btn-danger">Delete</a>
															</div>
														</div>
													</div>
												</div>
										</td>`

							mail_row.innerHTML = mail_data;
							mail_row.addEventListener('click', ()=>{
								document.location.href = `/profile/mail/${mail.id}`;

							})
							document.getElementById("mail_body").append(mail_row);
						})
					})
			} else {
				fetch(`../archeive_person_mails/${user_id}`)
				.then(response => response.json())
				.then(mails => {
						mails.forEach((mail, i) => {
							const mail_row = document.createElement('tr');
							let mail_data = `<td>${i+1}</td>
										<td>${mail.subject}</td>
										<td>${mail.date}</td>
										<td>
											<a href="/profile/mail/archeive/${mail.id}" onClick="event.stopPropagation();" class="btn btn-secondary p-1">
												<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-archive" viewBox="0 0 16 16">
													<path
													 d="M0 2a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v2a1 1 0 0 1-1 1v7.5a2.5 2.5 0 0 1-2.5 2.5h-9A2.5 2.5 0 0 1 1 12.5V5a1 1 0 0 1-1-1V2zm2 3v7.5A1.5 1.5 0 0 0 3.5 14h9a1.5 1.5 0 0 0 1.5-1.5V5H2zm13-3H1v2h14V2zM5 7.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5z" />
												</svg>
											</a>
												<button type="button" onClick="event.stopPropagation();" class="btn btn-danger p-1" data-bs-toggle="modal" data-bs-target="#delete_mail${mail.id}">
													<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-eraser" viewBox="0 0 16 16">
														<path
														 d="M8.086 2.207a2 2 0 0 1 2.828 0l3.879 3.879a2 2 0 0 1 0 2.828l-5.5 5.5A2 2 0 0 1 7.879 15H5.12a2 2 0 0 1-1.414-.586l-2.5-2.5a2 2 0 0 1 0-2.828l6.879-6.879zm2.121.707a1 1 0 0 0-1.414 0L4.16 7.547l5.293 5.293 4.633-4.633a1 1 0 0 0 0-1.414l-3.879-3.879zM8.746 13.547 3.453 8.254 1.914 9.793a1 1 0 0 0 0 1.414l2.5 2.5a1 1 0 0 0 .707.293H7.88a1 1 0 0 0 .707-.293l.16-.16z" />
													</svg>
												</button>

												<!-- modal -->
												<div class="modal fade" id="delete_mail${mail.id}" tabindex="-1" aria-labelledby="delete_post_model" aria-hidden="true">
													<div class="modal-dialog">
														<div class="modal-content">
															<div class="modal-header">
																<h5 class="modal-title" id="exampleModalLabel">Delete Post</h5>
																<button type="button" onClick="event.stopPropagation();" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
															</div>
															<div class="modal-body">
																Are you sure you want to delete this mail?
															</div>
															<div class="modal-footer">
																<button type="button" onClick="event.stopPropagation();" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
																<a href="/profile/mail/delete/${mail.id}" onClick="event.stopPropagation();" class="btn btn-danger">Delete</a>
															</div>
														</div>
													</div>
												</div>
										</td>`

							mail_row.innerHTML = mail_data;
							mail_row.addEventListener('click', ()=>{
								document.location.href = `/profile/mail/${mail.id}`;

							})
							document.getElementById("mail_body").append(mail_row);
						})
					})
			}

		})
	}
})
