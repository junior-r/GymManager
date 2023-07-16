function previewImage(action, inputImageId, imagePrevId) {
    // Obtiene los elementos del DOM
    const inputImage = document.getElementById(`${inputImageId}`);
    const inputImageOriginalValue = inputImage ? inputImage.value : null;
    const imagePrev = document.getElementById(`${imagePrevId}`);
    const urlOriginalImage = imagePrev ? imagePrev.getAttribute('src') : null;
    const deleteFileButton = document.getElementById('delete-file-btn');

    // Agrega un event listener al input de tipo file
    inputImage.addEventListener('change', function () {
        // Verifica si se seleccionó una imagen
        if (this.files && this.files[0]) {
            const reader = new FileReader();

            // Define la función que se ejecuta cuando la imagen se carga
            reader.onload = function (e) {
                // Actualiza el src de la etiqueta img para mostrar la imagen cargada
                imagePrev.setAttribute('src', e.target.result);
            };
            deleteFileButton.classList.remove('hidden');

            // Lee el contenido de la imagen como una URL
            reader.readAsDataURL(this.files[0]);
        }
    });

    // Agrega un event listener al botón de eliminar
    deleteFileButton.addEventListener('click', function () {
        // Restablece el valor del input y el src de la etiqueta img
        if (action === 'create') {
            inputImage.value = '';
        } else {
            inputImage.value = inputImageOriginalValue;
        }
        imagePrev.setAttribute('src', urlOriginalImage);
        // Oculta el botón de eliminar
        deleteFileButton.classList.add('hidden');
    });
}