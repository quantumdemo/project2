document.addEventListener('DOMContentLoaded', () => {
  // Mobile Nav Toggle & Body Scroll Locking
  const navToggle = document.getElementById('mobileNavToggle');
  const navDrawer = document.getElementById('mobileNavDrawer');
  const body = document.body;

  function closeMobileNav() {
    if (navDrawer && navToggle) {
      navDrawer.classList.remove('is-open');
      navToggle.setAttribute('aria-expanded', 'false');
      navToggle.innerHTML = '&#9776;';
      body.classList.remove('menu-open');
    }
  }

  function openMobileNav() {
    if (navDrawer && navToggle) {
      navDrawer.classList.add('is-open');
      navToggle.setAttribute('aria-expanded', 'true');
      navToggle.innerHTML = '&#10005;';
      body.classList.add('menu-open');
    }
  }

  if (navToggle && navDrawer) {
    navToggle.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = navDrawer.classList.contains('is-open');
      if (isOpen) {
        closeMobileNav();
      } else {
        openMobileNav();
      }
    });

    // Close when clicking any nav link inside drawer
    const drawerLinks = navDrawer.querySelectorAll('a');
    drawerLinks.forEach(link => {
      link.addEventListener('click', () => {
        closeMobileNav();
      });
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && navDrawer.classList.contains('is-open')) {
        closeMobileNav();
      }
    });
  }

  // Scroll Reveal Animations
  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -50px 0px',
    threshold: 0.1
  };

  const revealElements = document.querySelectorAll('.reveal-on-scroll');

  if ('IntersectionObserver' in window) {
    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    revealElements.forEach(el => revealObserver.observe(el));
  } else {
    revealElements.forEach(el => el.classList.add('is-visible'));
  }
});
