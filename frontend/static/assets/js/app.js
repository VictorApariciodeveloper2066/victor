// ...existing code...
// Código para el botón tipo hamburguesa en dispositivos móviles y el formulario de contacto

document.addEventListener('DOMContentLoaded', () => {
  const burger = document.querySelector('.burger');
  const navLinks = document.querySelector('.nav-links');

  if (burger && navLinks) {
    burger.addEventListener('click', () => {
      navLinks.classList.toggle('mobile-active');
    });
  }

  const contactForm = document.getElementById('contact-form');
  if (contactForm) {
    contactForm.addEventListener('submit', function (event) {
      event.preventDefault();

      const submitButton = this.querySelector('button[type="submit"]');
      if (submitButton) submitButton.classList.add('loading');

      const formData = new FormData(this);

      fetch('/send_email', {
        method: 'POST',
        body: formData
      })
        .then(response => response.text())
        .then(data => {
          showFlashMessage('Mensaje enviado correctamente.', 'success');
          this.reset(); // limpia el formulario
          if (submitButton) submitButton.classList.remove('loading');
        })
        .catch(error => {
          showFlashMessage('Hubo un error al enviar el mensaje.', 'danger');
          console.error('Error:', error);
          if (submitButton) submitButton.classList.remove('loading');
        });
    });
  }
});

/* Función para mostrar mensajes flash en #flash-messages */
function showFlashMessage(message, category) {
  const flashContainer = document.getElementById('flash-messages');
  if (!flashContainer) return;

  const flashMessage = document.createElement('div');
  flashMessage.className = `alert ${category}`;
  flashMessage.textContent = message;

  flashContainer.appendChild(flashMessage);

  setTimeout(() => {
    flashMessage.remove();
  }, 5000);
}
// ...existing code...