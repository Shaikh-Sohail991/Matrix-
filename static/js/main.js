// Helper function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Navbar scroll effect
const navbar = document.querySelector('.navbar');

function handleNavbarScroll() {
    if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
}

window.addEventListener('scroll', handleNavbarScroll);
handleNavbarScroll();

// Scroll reveal animation
const revealElements = document.querySelectorAll('.reveal, .reveal-left, .reveal-right, .stagger-children');

const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        }
    });
}, {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
});

revealElements.forEach(el => revealObserver.observe(el));

// Ensure reveal elements already in viewport are visible on load (from contact.html, privacy_policy.html, product_details.html, terms_of_service.html)
function setRevealActiveInViewport() {
    revealElements.forEach(el => {
        const rect = el.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0) {
            el.classList.add('active');
        }
    });
}
setRevealActiveInViewport();
window.addEventListener('load', setRevealActiveInViewport);

// Form validation and submission (from contact.html)
const contactForm = document.getElementById('contactForm');

if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
        e.preventDefault();

        // Bootstrap validation
        if (!contactForm.checkValidity()) {
            e.stopPropagation();

            // Add was-validated class to show validation states
            contactForm.classList.add('was-validated');
            return;
        }

        // Submit form via AJAX
        const formData = new FormData(contactForm);
        const actionUrl = contactForm.getAttribute('action');
        const csrftoken = getCookie('csrftoken');

        fetch(actionUrl, {
            method: 'POST',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrftoken,
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Show success message
                alert(data.message);

                // Reset form and remove validation state
                contactForm.reset();
                contactForm.classList.remove('was-validated');
            } else {
                alert(data.message || 'An error occurred. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
    });
}


// Counter animation (from index.html)
const counters = document.querySelectorAll('.counter');
let countersAnimated = false;

function animateCounters() {
    if (countersAnimated) return;

    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-target'));
        const duration = 2000;
        const step = target / (duration / 16);
        let current = 0;

        const updateCounter = () => {
            current += step;
            if (current < target) {
                counter.textContent = Math.floor(current).toLocaleString();
                requestAnimationFrame(updateCounter);
            } else {
                counter.textContent = target.toLocaleString();
            }
        };

        updateCounter();
    });

    countersAnimated = true;
}

const statsSection = document.querySelector('.stats-section');
if (statsSection) {
    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateCounters();
            }
        });
    }, { threshold: 0.3 });
    statsObserver.observe(statsSection);
}


// Gallery thumb selection (from product_details.html)
const thumbs = document.querySelectorAll('.product-gallery-thumb');
if (thumbs) {
    thumbs.forEach(thumb => {
        thumb.addEventListener('click', function () {
            thumbs.forEach(t => t.classList.remove('active'));
            this.classList.add('active');
        });
    });
}


// Quote form submission (demo) (from product_details.html)
// Note: This is overridden by inline script in product_details.html
const quoteForm = document.getElementById('quoteForm');
if (quoteForm && !quoteForm.hasAttribute('data-handler-set')) {
    quoteForm.addEventListener('submit', function (e) {
        e.preventDefault();
        alert('Your quote request has been sent! We will contact you shortly.');
        if (document.getElementById('quoteModal')) {
            bootstrap.Modal.getInstance(document.getElementById('quoteModal')).hide();
        }
        this.reset();
    });
    quoteForm.setAttribute('data-handler-set', 'true');
}


// Populate product name for forms if needed (from product_details.html)
const productName = document.getElementById('product-title')?.textContent || '';
const quoteProductInput = document.getElementById('quoteProduct');
if (quoteProductInput) quoteProductInput.value = productName;


// Service Modal functionality (from services.html)
const serviceModal = document.getElementById('serviceModal');

if (serviceModal) {
    serviceModal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget; // Button that triggered the modal
        const service = button.getAttribute('data-service');
        
        const serviceInput = document.getElementById('service');
        const serviceLabel = document.getElementById('serviceLabel');
        
        if (service) {
            if (serviceInput) serviceInput.value = service;
            if (serviceLabel) serviceLabel.textContent = service;
        }
    });
}


// Form submission (from services.html)
const serviceForm = document.getElementById('serviceForm');

if (serviceForm) {
    serviceForm.addEventListener('submit', function (e) {
        e.preventDefault();

        // Simple validation
        if (!serviceForm.checkValidity()) {
            e.stopPropagation();
            serviceForm.classList.add('was-validated');
            return;
        }

        // Submit form via AJAX
        const formData = new FormData(serviceForm);
        const actionUrl = serviceForm.getAttribute('action');
        const csrftoken = getCookie('csrftoken');

        fetch(actionUrl, {
            method: 'POST',
            headers: {
                'X-Requested-With': 'XMLHttpRequest',
                'X-CSRFToken': csrftoken,
            },
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Show success message
                alert(data.message);

                // Close modal and reset form
                const modal = bootstrap.Modal.getInstance(serviceModal);
                modal.hide();
                serviceForm.reset();
                serviceForm.classList.remove('was-validated');
            } else {
                alert(data.message || 'An error occurred. Please try again.');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
    });
}