const form = document.getElementById('cardForm');
const result = document.getElementById('result');

const nameInput = form.querySelector('[name="name"]');
const messageInput = form.querySelector('[name="message"]');
const imageInput = form.querySelector('[name="image"]');

const previewName = document.getElementById('preview-name');
const previewMessage = document.getElementById('preview-message');
const previewImage = document.getElementById('preview-image');

// Live Preview
nameInput.addEventListener('input', () => previewName.innerText = nameInput.value);
messageInput.addEventListener('input', () => previewMessage.innerText = messageInput.value);
imageInput.addEventListener('change', () => {
    const file = imageInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = e => {
            previewImage.src = e.target.result;
            previewImage.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }
});

// AJAX Submit
form.addEventListener('submit', function (e) {
    e.preventDefault();
    const formData = new FormData(form);
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    fetch("/generate/", {
        method: 'POST',
        body: formData,
        headers: { 'X-CSRFToken': csrftoken }
    })
        .then(res => res.json())
        .then(data => {
            if (data.link) {
                result.innerHTML = `<p>Your Shareable Link:</p>
            <a href="${data.link}" target="_blank">${data.link}</a>`;
            } else {
                result.innerHTML = `<p>Error: ${data.error}</p>`;
            }
        })
        .catch(err => console.log(err));
});
