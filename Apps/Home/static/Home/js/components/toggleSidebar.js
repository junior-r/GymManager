$(document).ready(function () {
    const toggleButton = $('#toggleSidebar');
    const sidebar = $('#logo-sidebar');

    // Comprueba si hay un estado almacenado en el localStorage
    const sidebarState = localStorage.getItem('sidebarState');
    if (sidebarState === 'collapsed') {
        sidebar.addClass('sidebar-collapsed');
        $('.sidebar-text').addClass('sidebar-hidden');
    } else {
        sidebar.removeClass('sidebar-collapsed');
        $('.sidebar-text').removeClass('sidebar-hidden');
    }

    // Agrega el evento de clic al botón
    toggleButton.on('click', function () {
        sidebar.toggleClass('sidebar-collapsed');
        // Animar y ocultar los elementos de texto del sidebar
        const sidebarText = $('.sidebar-text');
        if (sidebar.hasClass('sidebar-collapsed')) {
            sidebarText.animate({opacity: 0}, 500, function () {
                sidebarText.addClass('sidebar-hidden');
            });
        } else {
            sidebarText.removeClass('sidebar-hidden');
            sidebarText.animate({opacity: 1}, 300);
        }

        // Guardar el estado en el localStorage
        if (sidebar.hasClass('sidebar-collapsed')) {
            localStorage.setItem('sidebarState', 'collapsed');
        } else {
            localStorage.removeItem('sidebarState');
        }
    });

    // Agrega el evento resize a la ventana
    $(window).resize(function () {
        if ($(window).width() <= 640) {
            localStorage.removeItem('sidebarState');
            sidebar.removeClass('sidebar-collapsed');

            // Animar y ocultar los elementos de texto del sidebar
            const sidebarText = $('.sidebar-text');
            sidebarText.removeClass('sidebar-hidden');
            sidebarText.animate({opacity: 1}, 300);
        }
    });
});