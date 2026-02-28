// ====================================
// Heart Disease Analysis - Main JavaScript
// ====================================

document.addEventListener('DOMContentLoaded', function () {
    initMobileMenu();
    initDashboardNavigation();
    initContactForm();
    initSmoothScroll();
});

// ====================================
// Mobile Menu Toggle
// ====================================
function initMobileMenu() {
    const toggle = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (toggle && navLinks) {
        toggle.addEventListener('click', function () {
            navLinks.classList.toggle('active');
            toggle.classList.toggle('active');
        });
    }
}

// ====================================
// Dashboard Navigation
// ====================================
let currentDashboard = 0;
const totalDashboards = document.querySelectorAll('.dashboard-slide').length;

function initDashboardNavigation() {
    updateDashboardButtons();

    // Add click handlers to indicators
    const indicators = document.querySelectorAll('.indicator');
    indicators.forEach((indicator, index) => {
        indicator.addEventListener('click', () => {
            goToDashboard(index);
        });
    });
}

function changeDashboard(direction) {
    const newIndex = currentDashboard + direction;
    if (newIndex >= 0 && newIndex < totalDashboards) {
        goToDashboard(newIndex);
    }
}

function goToDashboard(index) {
    const slides = document.querySelectorAll('.dashboard-slide');
    const indicators = document.querySelectorAll('.indicator');

    if (slides.length === 0) return;

    // Update slides
    slides[currentDashboard].classList.remove('active');
    slides[index].classList.add('active');

    // Update indicators
    if (indicators.length > 0) {
        indicators[currentDashboard].classList.remove('active');
        indicators[index].classList.add('active');
    }

    currentDashboard = index;
    updateDashboardButtons();
}

function updateDashboardButtons() {
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');

    if (prevBtn) {
        prevBtn.disabled = currentDashboard === 0;
    }

    if (nextBtn) {
        nextBtn.disabled = currentDashboard === totalDashboards - 1;
        if (currentDashboard === totalDashboards - 1) {
            nextBtn.classList.remove('btn-primary');
        } else {
            nextBtn.classList.add('btn-primary');
        }
    }
}

// ====================================
// Fullscreen Modal for Visualizations
// ====================================
function toggleFullscreen(button) {
    const card = button.closest('.viz-card');
    const iframe = card.querySelector('iframe');
    const modal = document.getElementById('fullscreen-modal');
    const modalIframe = document.getElementById('modal-iframe');

    if (modal && modalIframe && iframe) {
        modalIframe.src = iframe.src;
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
}

function closeModal() {
    const modal = document.getElementById('fullscreen-modal');
    const modalIframe = document.getElementById('modal-iframe');

    if (modal) {
        modal.classList.remove('active');
        document.body.style.overflow = '';
    }

    if (modalIframe) {
        modalIframe.src = '';
    }
}

// Close modal on escape key
document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
        closeModal();
    }
});

// Close modal on backdrop click
document.addEventListener('click', function (e) {
    const modal = document.getElementById('fullscreen-modal');
    if (e.target === modal) {
        closeModal();
    }
});

// ====================================
// Contact Form
// ====================================
function initContactForm() {
    const form = document.getElementById('contact-form');

    if (form) {
        form.addEventListener('submit', async function (e) {
            e.preventDefault();

            const formData = new FormData(form);
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalText = submitBtn.textContent;

            submitBtn.textContent = 'Sending...';
            submitBtn.disabled = true;

            try {
                const response = await fetch(form.action, {
                    method: 'POST',
                    body: formData
                });

                const data = await response.json();

                if (data.success) {
                    showNotification('Thank you! Your message has been sent.', 'success');
                    form.reset();
                } else {
                    showNotification('Something went wrong. Please try again.', 'error');
                }
            } catch (error) {
                showNotification('Something went wrong. Please try again.', 'error');
            } finally {
                submitBtn.textContent = originalText;
                submitBtn.disabled = false;
            }
        });
    }
}

function showNotification(message, type) {
    // Remove existing notification
    const existing = document.querySelector('.notification');
    if (existing) {
        existing.remove();
    }

    // Create notification
    const notification = document.createElement('div');
    notification.className = `notification notification-${type}`;
    notification.textContent = message;
    notification.style.cssText = `
        position: fixed;
        top: 100px;
        right: 24px;
        padding: 16px 24px;
        background: ${type === 'success' ? '#10B981' : '#EF4444'};
        color: white;
        border-radius: 8px;
        font-size: 14px;
        font-weight: 500;
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
        z-index: 3000;
        animation: slideIn 0.3s ease;
    `;

    document.body.appendChild(notification);

    // Auto remove after 5 seconds
    setTimeout(() => {
        notification.style.animation = 'slideOut 0.3s ease';
        setTimeout(() => notification.remove(), 300);
    }, 5000);
}

// ====================================
// Smooth Scroll
// ====================================
function initSmoothScroll() {
    const links = document.querySelectorAll('a[href^="#"]');

    links.forEach(link => {
        link.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#') {
                e.preventDefault();
                const target = document.querySelector(href);
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            }
        });
    });
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(100%);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    
    @keyframes slideOut {
        from {
            transform: translateX(0);
            opacity: 1;
        }
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
    
    /* Mobile menu styles */
    @media (max-width: 768px) {
        .nav-links.active {
            display: flex !important;
            flex-direction: column;
            position: absolute;
            top: 72px;
            left: 0;
            right: 0;
            background: white;
            padding: 24px;
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            gap: 16px;
        }
        
        .mobile-menu-toggle.active span:nth-child(1) {
            transform: rotate(45deg) translate(5px, 5px);
        }
        
        .mobile-menu-toggle.active span:nth-child(2) {
            opacity: 0;
        }
        
        .mobile-menu-toggle.active span:nth-child(3) {
            transform: rotate(-45deg) translate(5px, -5px);
        }
    }
`;
document.head.appendChild(style);
