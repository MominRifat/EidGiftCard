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
                result.innerHTML = `
                   <p style="text-align:center; color:#1e88e5; font-weight:600;">
                    আপনার শেয়ারযোগ্য লিঙ্ক:
                    </p>
                    <div class="share-link-box">
                        <a href="${data.link}" target="_blank">${data.link}</a>
                        <div class="link-actions">
                            <button class="copy-btn">Copy করুন</button>
                            <button class="visit-btn">Visit করুন</button>
                            <span class="copy-feedback">Copied!</span>
                        </div>
                    </div>
                `;

                // Copy button
                const copyBtn = result.querySelector('.copy-btn');
                const visitBtn = result.querySelector('.visit-btn');
                const linkText = result.querySelector('.share-link-box a');
                const feedback = result.querySelector('.copy-feedback');

                copyBtn.addEventListener('click', () => {
                    navigator.clipboard.writeText(linkText.href)
                        .then(() => {
                            feedback.style.display = 'inline';
                            setTimeout(() => feedback.style.display = 'none', 1500);
                        })
                        .catch(err => console.log('কপি করা যায়নি:', err));
                });

                // Visit button
                visitBtn.addEventListener('click', () => {
                    window.open(linkText.href, '_blank');
                });

            } else {
                result.innerHTML = `<p>Error: ${data.error}</p>`;
            }
        })
        .catch(err => console.log(err));
});
