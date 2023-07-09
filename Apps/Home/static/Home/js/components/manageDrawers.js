function openDrawer(url, modalId) {
    $(`#${modalId}`).load(url, function () {
        let modal = $(this).children()
        modal.show()
        modal.attr('aria-modal', true)
        modal.attr('role', 'dialog')
        modal.removeClass('-translate-x-full')
        modal.removeAttr('style')
        modal.addClass('transform-none')

        const backdrop = document.createElement('div')
        backdrop.setAttribute('id', 'backdrop-drawer')
        backdrop.setAttribute('drawer-backdrop', '')
        backdrop.setAttribute('class', 'bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-30')
        document.body.appendChild(backdrop)
        document.body.style.overflow = "hidden";
    });
}

function closeDrawer(modalId) {
    let modal = $(`#${modalId}`).children()
    modal.attr('aria-modal', false)
    modal.removeAttr('role')
    modal.removeAttr('style')
    modal.addClass('-translate-x-full')
    modal.removeClass('transform-none')
    document.body.style.overflow = "auto";

    const backdrop = document.getElementById('backdrop-drawer')
    // Verificar si el elemento existe y es un hijo del cuerpo
    if (backdrop && backdrop.parentNode === document.body) {
        // Remover el elemento del cuerpo
        document.body.removeChild(backdrop);
    }
    $(`#${modalId}`).empty();
}

function closeOpenDrawer(url, closeModalId, openModalId) {
    closeDrawer(closeModalId);
    setTimeout(function() {
        openDrawer(url, openModalId);
    }, 100)
}