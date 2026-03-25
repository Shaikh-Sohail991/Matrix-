/* ============================================
   MATRIX TECHNOLOGY – SHARED JS
   ============================================ */

// ─── Scroll Reveal ───────────────────────────
const revealObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
      revealObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });
document.querySelectorAll('.reveal').forEach(el => revealObserver.observe(el));

// ─── Hamburger / Mobile Nav ───────────────────
const hamburger = document.getElementById('hamburger');
const mobileNav = document.getElementById('mobileNav');
if (hamburger && mobileNav) {
  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    mobileNav.classList.toggle('open');
    document.body.style.overflow = mobileNav.classList.contains('open') ? 'hidden' : '';
  });
}

// ─── Navbar scroll shrink ───────────────────
const navbar = document.querySelector('.navbar');
window.addEventListener('scroll', () => {
  if (window.scrollY > 20) {
    navbar?.classList.add('scrolled');
  } else {
    navbar?.classList.remove('scrolled');
  }
}, { passive: true });

// ─── Stagger children on viewport enter ──────
const staggerObserver = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const children = entry.target.querySelectorAll('.product-card, .category-card, .stagger-item');
      children.forEach((child, i) => {
        setTimeout(() => {
          child.style.opacity = '1';
          child.style.transform = 'translateY(0)';
        }, i * 80);
      });
      staggerObserver.unobserve(entry.target);
    }
  });
}, { threshold: 0.05 });
document.querySelectorAll('.products-grid, .stagger-container').forEach(el => {
  const cards = el.querySelectorAll('.product-card, .stagger-item');
  cards.forEach(c => {
    c.style.opacity = '0';
    c.style.transform = 'translateY(20px)';
    c.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
  });
  staggerObserver.observe(el);
});

// ─── Filter buttons ───────────────────────────
document.querySelectorAll('.filter-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    const group = btn.closest('.filter-bar');
    group?.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const filter = btn.dataset.filter;
    document.querySelectorAll('.product-card').forEach(card => {
      if (filter === 'all' || card.dataset.type === filter) {
        card.style.display = '';
      } else {
        card.style.display = 'none';
      }
    });
  });
});

// ─── Product search ──────────────────────────
const searchInput = document.getElementById('productSearch');
if (searchInput) {
  searchInput.addEventListener('input', () => {
    const q = searchInput.value.toLowerCase();
    document.querySelectorAll('.product-card').forEach(card => {
      const text = card.textContent.toLowerCase();
      card.style.display = text.includes(q) ? '' : 'none';
    });
  });
}

// ─── Mobile sidebar toggle ────────────────────
const sidebarTrigger = document.getElementById('sidebarTrigger');
const sidebarEl = document.getElementById('sidebar');
if (sidebarTrigger && sidebarEl) {
  sidebarTrigger.addEventListener('click', () => {
    sidebarEl.style.display = sidebarEl.style.display === 'block' ? '' : 'block';
  });
}

// ─── Smooth navbar scrolled style ────────────
document.querySelector('.navbar')?.style && (
  document.querySelector('.navbar').style.transition = 'all 0.3s ease'
);
