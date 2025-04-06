document.addEventListener('DOMContentLoaded', function() {
    // Theme switching functionality
    const themeButtons = document.querySelectorAll('.theme-btn');
    const body = document.body;
    
    // Check for saved theme preference or use default
    const savedTheme = localStorage.getItem('theme') || 'default';
    setTheme(savedTheme);
    
    // Add click event listeners to theme buttons
    themeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const theme = this.getAttribute('data-theme');
            setTheme(theme);
            localStorage.setItem('theme', theme);
        });
    });
    
    function setTheme(theme) {
        body.setAttribute('data-theme', theme);
        
        // Update active state on buttons
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
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    // Make navigation sticky
    window.addEventListener('scroll', function() {
        const header = document.querySelector('header');
        if (window.scrollY > 50) {
            header.style.padding = '0.5rem 0';
            header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        } else {
            header.style.padding = '1rem 0';
            header.style.boxShadow = 'none';
        }
    });
});