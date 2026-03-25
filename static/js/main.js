// ─── Inline toast notification (replaces all alert() calls) ─────────────────
function showToast(message, type) {
    var existing = document.getElementById('mx-toast');
    if (existing) existing.remove();

    var toast = document.createElement('div');
    toast.id = 'mx-toast';
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.style.cssText = [
        'position:fixed', 'bottom:24px', 'right:24px', 'z-index:9999',
        'padding:14px 20px', 'border-radius:10px', 'max-width:360px',
        'font-size:0.9rem', 'font-weight:500', 'box-shadow:0 8px 24px rgba(0,0,0,.4)',
        'display:flex', 'align-items:center', 'gap:10px',
        'background:' + (type === 'success' ? 'rgba(16,185,129,.15)' : 'rgba(239,68,68,.15)'),
        'border:1px solid ' + (type === 'success' ? 'rgba(16,185,129,.5)' : 'rgba(239,68,68,.5)'),
        'color:' + (type === 'success' ? '#6ee7b7' : '#fca5a5'),
        'transition:opacity .4s ease',
    ].join(';');

    var icon = document.createElement('i');
    icon.className = type === 'success' ? 'bi bi-check-circle-fill' : 'bi bi-exclamation-triangle-fill';
    icon.style.fontSize = '1.1rem';

    var text = document.createElement('span');
    text.textContent = message;

    toast.appendChild(icon);
    toast.appendChild(text);
    document.body.appendChild(toast);

    setTimeout(function () {
        toast.style.opacity = '0';
        setTimeout(function () { toast.remove(); }, 450);
    }, 4000);
}


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

// Hero carousel behavior (product showcase)
const heroCarousel = document.querySelector('.hero-carousel');
const heroImages = heroCarousel ? heroCarousel.querySelectorAll('img') : [];
const carouselIndicators = document.getElementById('carouselIndicators');
let currentHeroIndex = 0;

function showHeroImage(index) {
    heroImages.forEach((img, i) => {
        img.classList.toggle('active', i === index);
    });
    
    // Update indicators
    if (carouselIndicators) {
        const indicators = carouselIndicators.querySelectorAll('.indicator');
        indicators.forEach((indicator, i) => {
            indicator.classList.toggle('active', i === index);
        });
    }
}

if (heroImages.length > 0) {
    // Create indicators
    if (carouselIndicators) {
        heroImages.forEach((_, i) => {
            const indicator = document.createElement('div');
            indicator.className = 'indicator' + (i === 0 ? ' active' : '');
            indicator.addEventListener('click', () => {
                currentHeroIndex = i;
                showHeroImage(currentHeroIndex);
            });
            carouselIndicators.appendChild(indicator);
        });
    }
    
    showHeroImage(0);
    const prevBtn = document.querySelector('.carousel-control.prev');
    const nextBtn = document.querySelector('.carousel-control.next');

    if (prevBtn) {
        prevBtn.addEventListener('click', () => {
            currentHeroIndex = (currentHeroIndex - 1 + heroImages.length) % heroImages.length;
            showHeroImage(currentHeroIndex);
        });
    }
    if (nextBtn) {
        nextBtn.addEventListener('click', () => {
            currentHeroIndex = (currentHeroIndex + 1) % heroImages.length;
            showHeroImage(currentHeroIndex);
        });
    }
}


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
        const submitBtn = document.getElementById('contactSubmitBtn');
        const origHtml = submitBtn ? submitBtn.innerHTML : null;
        if (submitBtn) { submitBtn.disabled = true; submitBtn.innerHTML = '<span>Sending…</span>'; }

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
                showToast(data.message || 'Message sent! We\'ll be in touch within 24 hours.', 'success');
                contactForm.reset();
                contactForm.classList.remove('was-validated');
            } else {
                showToast(data.message || 'An error occurred. Please try again.', 'error');
            }
        })
        .catch(function(error) {
            console.error('Error:', error);
            showToast('An error occurred. Please try again.', 'error');
        })
        .finally(function() {
            if (submitBtn && origHtml) { submitBtn.disabled = false; submitBtn.innerHTML = origHtml; }
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


// Quote form logic (site‑wide) – the modal is defined in base.html and
// individual pages (product_details) already have a copy as a fallback.
(function() {
    function initQuoteForm() {
        const quoteForm = document.getElementById('quoteForm');
        if (!quoteForm || quoteForm.hasAttribute('data-handler-set')) return;

        quoteForm.addEventListener('submit', function (e) {
            e.preventDefault();
            const formData  = new FormData(this);
            const submitBtn = document.getElementById('quoteSubmitBtn');
            const origHtml  = submitBtn.innerHTML;

            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span>Submitting...</span>';

            // Read the URL from the data-attribute set in base.html (template tags
            // are NOT processed in static files, so we cannot use {% url %} here).
            const quoteUrl = document.getElementById('quoteModal')?.dataset?.quoteUrl || '/products/quote-request/';
            fetch(quoteUrl, {
                method: 'POST',
                body: formData,
            })
            .then(r => r.json())
            .then(data => {
                const msgDiv = document.getElementById('quoteResponseMsg');
                msgDiv.style.display = 'block';
                if (data.success) {
                    msgDiv.className = 'alert alert-success';
                    msgDiv.textContent = data.message;
                    quoteForm.reset();
                    setTimeout(() => {
                        bootstrap.Modal.getInstance(document.getElementById('quoteModal')).hide();
                        msgDiv.style.display = 'none';
                    }, 2000);
                } else {
                    msgDiv.className = 'alert alert-danger';
                    msgDiv.textContent = data.message;
                }
            })
            .catch(function () {
                const msgDiv = document.getElementById('quoteResponseMsg');
                msgDiv.style.display = 'block';
                msgDiv.className = 'alert alert-danger';
                msgDiv.textContent = 'An error occurred. Please try again.';
            })
            .finally(function () {
                submitBtn.disabled = false;
                submitBtn.innerHTML = origHtml;
            });
        });

        quoteForm.setAttribute('data-handler-set', 'true');
    }

    document.addEventListener('click', function(e) {
        const btn = e.target.closest('.btn-quote');
        if (!btn) return;
        e.preventDefault();
        const prodName = btn.dataset.product || '';
        const modalEl = document.getElementById('quoteModal');
        if (modalEl) {
            const input = modalEl.querySelector('#quoteProduct');
            if (input) input.value = prodName;
            new bootstrap.Modal(modalEl).show();
            initQuoteForm();
        }
    });

    document.addEventListener('DOMContentLoaded', function() {
        const productName = document.getElementById('product-title')?.textContent.trim() || '';
        const quoteProductInput = document.getElementById('quoteProduct');
        if (quoteProductInput && productName) quoteProductInput.value = productName;
        initQuoteForm();
    });
})();


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
                showToast(data.message || 'Request submitted! Our team will contact you shortly.', 'success');
                const modal = bootstrap.Modal.getInstance(serviceModal);
                modal.hide();
                serviceForm.reset();
                serviceForm.classList.remove('was-validated');
            } else {
                showToast(data.message || 'An error occurred. Please try again.', 'error');
            }
        })
        .catch(function(error) {
            console.error('Error:', error);
            showToast('An error occurred. Please try again.', 'error');
        });
    });
}