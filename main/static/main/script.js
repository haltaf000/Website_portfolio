document.addEventListener('DOMContentLoaded', function() {
    const themeButtons = document.querySelectorAll('.theme-btn');
    const body = document.body;
    
    const savedTheme = localStorage.getItem('theme') || 'default';
    setTheme(savedTheme);
    
    themeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const theme = this.getAttribute('data-theme');
            setTheme(theme);
            localStorage.setItem('theme', theme);
        });
    });
    
    function setTheme(theme) {
        body.setAttribute('data-theme', theme);
        
        themeButtons.forEach(button => {
            if (button.getAttribute('data-theme') === theme) {
                button.style.transform = 'scale(1.2)';
                button.style.borderColor = 'var(--accent-color)';
            } else {
                button.style.transform = 'scale(1)';
                button.style.borderColor = 'var(--text-color)';
            }
        });
    }
    
    const navbarToggler = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    if (navbarToggler && navbarCollapse) {
        navbarToggler.addEventListener('click', function() {
            navbarCollapse.classList.toggle('show');
            
            const icon = this.querySelector('i');
            if (navbarCollapse.classList.contains('show')) {
                icon.classList.replace('fa-bars', 'fa-times');
            } else {
                icon.classList.replace('fa-times', 'fa-bars');
            }
        });
    }
    
    const navLinks = document.querySelectorAll('.navbar-nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            if (window.innerWidth <= 768 && navbarCollapse.classList.contains('show')) {
                navbarCollapse.classList.remove('show');
                const icon = navbarToggler.querySelector('i');
                icon.classList.replace('fa-times', 'fa-bars');
            }
        });
    });
    
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    window.addEventListener('scroll', function() {
        const header = document.querySelector('header');
        if (window.scrollY > 50) {
            header.style.padding = '0.5rem 0';
            header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        } else {
            header.style.padding = '0';
            header.style.boxShadow = 'none';
        }
    });
    
    window.dispatchEvent(new Event('scroll'));
});