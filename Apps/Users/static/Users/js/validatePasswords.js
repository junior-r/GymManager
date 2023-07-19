$(document).ready(function () {
    $('#id_password2').on('input', function () {
        let btnSubmit = $('#submitButton')
        const password1 = $('#id_password1')
        const password2 = $(this)
        let messageContainer = $('#passwordsMatchMessage')
        if (password1.val() === password2.val()) {
            messageContainer.empty()
            let message = `<p class="text-green-600 justify-center text-xs font-semibold dark:text-green-400 flex items-center gap-2">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                                      <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12c0 1.268-.63 2.39-1.593 3.068a3.745 3.745 0 01-1.043 3.296 3.745 3.745 0 01-3.296 1.043A3.745 3.745 0 0112 21c-1.268 0-2.39-.63-3.068-1.593a3.746 3.746 0 01-3.296-1.043 3.745 3.745 0 01-1.043-3.296A3.745 3.745 0 013 12c0-1.268.63-2.39 1.593-3.068a3.745 3.745 0 011.043-3.296 3.746 3.746 0 013.296-1.043A3.746 3.746 0 0112 3c1.268 0 2.39.63 3.068 1.593a3.746 3.746 0 013.296 1.043 3.746 3.746 0 011.043 3.296A3.745 3.745 0 0121 12z"></path>
                                    </svg>
                                    Contraseñas iguales
                                   </p>`
            messageContainer.append(message)
            btnSubmit.prop('disabled', false)
            btnSubmit.removeClass('cursor-not-allowed')
        } else {
            messageContainer.empty()
            let message = `<p class="text-red-600 justify-center text-xs font-semibold dark:text-red-400 flex items-center gap-2">
                                    <svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
                                        <path stroke-linecap="round" stroke-linejoin="round" d="M9.75 9.75l4.5 4.5m0-4.5l-4.5 4.5M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                                    </svg>
                                    Las contraseñas no coinciden
                                   </p>`
            messageContainer.append(message)
            btnSubmit.prop('disabled', true)
            btnSubmit.addClass('cursor-not-allowed')
        }
    })
})