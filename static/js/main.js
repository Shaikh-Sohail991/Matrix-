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

        // Demo success message
        const formData = new FormData(contactForm);
        console.log('Form submitted:', Object.fromEntries(formData));

        alert('Thank you for your message! We will get back to you within 24 hours.');

        // Reset form
        contactForm.reset();
        contactForm.classList.remove('was-validated');
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


// Inquiry form submission (demo) (from product_details.html)
const inquiryForm = document.getElementById('inquiryForm');
if (inquiryForm) {
    inquiryForm.addEventListener('submit', function (e) {
        e.preventDefault();
        alert('Thank you for your question! We will respond within 24 hours.');
        bootstrap.Modal.getInstance(document.getElementById('inquiryModal')).hide();
        this.reset();
    });
}


// Quote form submission (demo) (from product_details.html)
const quoteForm = document.getElementById('quoteForm');
if (quoteForm) {
    quoteForm.addEventListener('submit', function (e) {
        e.preventDefault();
        alert('Your quote request has been sent! We will contact you shortly.');
        bootstrap.Modal.getInstance(document.getElementById('quoteModal')).hide();
        this.reset();
    });
}


// Populate product name for forms if needed (from product_details.html)
const productName = document.getElementById('product-title')?.textContent || '';
const inquiryProductInput = document.getElementById('inquiryProduct');
const quoteProductInput = document.getElementById('quoteProduct');
if (inquiryProductInput) inquiryProductInput.value = productName;
if (quoteProductInput) quoteProductInput.value = productName;


// Service Modal functionality (from services.html)
const serviceModal = document.getElementById('serviceModal');
const serviceTypeInput = document.getElementById('serviceType');

if (serviceModal) {
    serviceModal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget;
        const service = button.getAttribute('data-service');
        serviceTypeInput.value = service;
    });
}


// Form submission (demo only) (from services.html)
const serviceForm = document.getElementById('serviceForm');

if (serviceForm) {
    serviceForm.addEventListener('submit', function (e) {
        e.preventDefault();

        // Simple validation
        if (!serviceForm.checkValidity()) {
            e.stopPropagation();
            return;
        }

        // Demo success message
        alert('Thank you for your inquiry! We will contact you shortly.');

        // Close modal and reset form
        const modal = bootstrap.Modal.getInstance(serviceModal);
        modal.hide();
        serviceForm.reset();
    });
}