function checkAvailableData(inputId, url, fieldIndicator, messageContainerId) {
    const field = $('#' + inputId);
    const fieldValue = field.val();
    let btnSubmit = $('#submitButton')
    let messageContainer = $('#' + messageContainerId)

    if (validateField(fieldValue, fieldIndicator)) {
        // Realizar la solicitud AJAX
        setTimeout(function () {
            $.ajax({
                url: `${url}`, // URL del script de verificación
                method: 'POST',
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                    'X-CSRFToken': csrftoken
                },
                data: {field: fieldValue, fieldIndicator: fieldIndicator}, // Enviar el nombre de usuario al servidor
                success: function (response) {
                    if (response['available'] === true) {
                        messageContainer.empty()
                        let message = `<p class="text-green-600 text-xs font-semibold dark:text-green-400 flex items-center gap-2">
                                            <svg fill="none" class="w-5 h-5" stroke="currentColor" stroke-width="1.5"
                                                 viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                                                <path stroke-linecap="round" stroke-linejoin="round"
                                                      d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                            </svg>
                                            ${response['message']}</p>`
                        messageContainer.append(message)
                        btnSubmit.prop('disabled', false)
                        btnSubmit.removeClass('cursor-not-allowed')
                    } else {
                        messageContainer.empty()
                        let message = `<p class="text-red-600 text-xs font-semibold dark:text-red-400 flex items-center gap-2">
                                            <svg fill="none" class="w-5 h-5" stroke="currentColor" stroke-width="1.5" 
                                                viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                                                <path stroke-linecap="round" stroke-linejoin="round" 
                                                    d="M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                            </svg>
                                            ${response['message']}</p>`
                        messageContainer.append(message)
                        btnSubmit.prop('disabled', true)
                        btnSubmit.addClass('cursor-not-allowed')
                    }
                },
                error: function () {
                    console.log('Error en la solicitud AJAX');
                }
            });
        }, 1000)
    } else {
        let message = `<p class="text-blue-800 text-xs font-semibold dark:text-blue-400 flex items-center gap-2">
                                <svg fill="none" class="w-5 h-5" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                                    <path stroke-linecap="round" stroke-linejoin="round" d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z"></path>
                                </svg>
                                El valor ingresado es inválido</p>`
        if (fieldValue.length === 0) {
            messageContainer.empty()
            btnSubmit.prop('disabled', false)
            btnSubmit.removeClass('cursor-not-allowed')
        } else {
            messageContainer.empty()
            messageContainer.append(message)
            btnSubmit.prop('disabled', true)
            btnSubmit.addClass('cursor-not-allowed')
        }
    }
}

function validateField(fieldValue, fieldIndicator) {
    if (fieldIndicator === 'email') {
        // Expresión regular para validar el formato del correo electrónico
        const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return regex.test(fieldValue);
    } else if (fieldIndicator === 'username') {
        return fieldValue.length >= 5
    } else if (fieldIndicator === 'identification') {
        return fieldValue.length >= 5
    }
}
