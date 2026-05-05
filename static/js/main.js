/* ============================================================
   LeafCare AI — Main JavaScript
   Drag & Drop upload, animations, interactive UI
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  /* ── Floating Leaves (Hero Background)  */
  const leavesContainer = document.getElementById('floating-leaves');
  if (leavesContainer) {
    const leafEmojis = ['🍃', '🌿', '🍂', '🌱'];
    for (let i = 0; i < 18; i++) {
      const leaf = document.createElement('span');
      leaf.textContent = leafEmojis[Math.floor(Math.random() * leafEmojis.length)];
      leaf.style.cssText = `
        position: absolute;
        font-size: ${Math.random() * 20 + 14}px;
        left: ${Math.random() * 100}%;
        top: ${Math.random() * 100}%;
        opacity: ${Math.random() * 0.12 + 0.04};
        animation: floatLeaf ${Math.random() * 10 + 12}s linear infinite;
        animation-delay: -${Math.random() * 15}s;
        pointer-events: none;
      `;
      leavesContainer.appendChild(leaf);
    }
    // Inject keyframes
    const style = document.createElement('style');
    style.textContent = `
      @keyframes floatLeaf {
        0%   { transform: translateY(0) rotate(0deg) scale(1); }
        33%  { transform: translateY(-30px) rotate(120deg) scale(1.1); }
        66%  { transform: translateY(-10px) rotate(240deg) scale(0.9); }
        100% { transform: translateY(0) rotate(360deg) scale(1); }
      }
    `;
    document.head.appendChild(style);
  }

  /* ── Hamburger menu ───────── */
  const hamburger = document.getElementById('hamburger');
  if (hamburger) {
    hamburger.addEventListener('click', () => {
      const navLinks = document.querySelector('.nav-links');
      const navCta = document.querySelector('.nav-cta');
      if (navLinks) {
        const open = navLinks.style.display === 'flex';
        navLinks.style.cssText = open
          ? 'display:none'
          : 'display:flex;flex-direction:column;position:absolute;top:64px;left:0;right:0;background:rgba(10,26,10,0.97);padding:16px;gap:8px;border-bottom:1px solid rgba(102,187,106,0.15)';
        if (navCta) navCta.style.display = open ? 'none' : 'inline-flex';
      }
    });
  }

  /* ── Navbar scroll effect ─── */
  const navbar = document.querySelector('.navbar');
  if (navbar) {
    window.addEventListener('scroll', () => {
      navbar.style.background = window.scrollY > 20
        ? 'rgba(10,26,10,0.97)'
        : 'rgba(10,26,10,0.85)';
    });
  }

  /* ── Drag & Drop Upload ───── */
  const dropZone = document.getElementById('drop-zone');
  const imageInput = document.getElementById('image-input');
  const browseBtn = document.getElementById('browse-btn');
  const analyzeBtn = document.getElementById('analyze-btn');
  const dzContent = document.getElementById('dz-content');
  const previewWrap = document.getElementById('preview-wrapper');
  const previewImg = document.getElementById('preview-img');
  const previewInfo = document.getElementById('preview-info');
  const removeBtn = document.getElementById('remove-btn');
  const uploadForm = document.getElementById('upload-form');

  if (dropZone && imageInput) {

    // Click to browse
    browseBtn?.addEventListener('click', () => imageInput.click());
    dropZone.addEventListener('click', (e) => {
      if (e.target === dropZone || e.target === dzContent || dzContent?.contains(e.target)) {
        if (!previewWrap || previewWrap.style.display === 'none') imageInput.click();
      }
    });

    // Drag events
    ['dragenter', 'dragover'].forEach(ev => {
      dropZone.addEventListener(ev, (e) => {
        e.preventDefault(); dropZone.classList.add('dragover');
      });
    });
    ['dragleave', 'dragend', 'drop'].forEach(ev => {
      dropZone.addEventListener(ev, () => dropZone.classList.remove('dragover'));
    });
    dropZone.addEventListener('drop', (e) => {
      e.preventDefault();
      const file = e.dataTransfer.files[0];
      if (file) handleFile(file);
    });

    // File input change
    imageInput.addEventListener('change', () => {
      if (imageInput.files[0]) handleFile(imageInput.files[0]);
    });

    // Remove image
    removeBtn?.addEventListener('click', (e) => {
      e.stopPropagation();
      resetUpload();
    });

    function handleFile(file) {
      const allowed = ['image/jpeg', 'image/png', 'image/webp'];
      if (!allowed.includes(file.type)) {
        showToast('❌ Invalid file type. Use JPG, PNG, or WEBP.', 'error');
        return;
      }
      if (file.size > 16 * 1024 * 1024) {
        showToast('❌ File too large. Maximum 16MB.', 'error');
        return;
      }
      const reader = new FileReader();
      reader.onload = (e) => {
        if (previewImg) previewImg.src = e.target.result;
        if (dzContent) dzContent.style.display = 'none';
        if (previewWrap) previewWrap.style.display = 'block';
        if (previewInfo) previewInfo.textContent = `${file.name} · ${(file.size / 1024).toFixed(0)} KB`;
        if (analyzeBtn) analyzeBtn.disabled = false;
      };
      reader.readAsDataURL(file);
      // Transfer to real input
      const dt = new DataTransfer();
      dt.items.add(file);
      imageInput.files = dt.files;
    }

    function resetUpload() {
      imageInput.value = '';
      if (previewImg) previewImg.src = '';
      if (previewWrap) previewWrap.style.display = 'none';
      if (dzContent) dzContent.style.display = 'block';
      if (analyzeBtn) analyzeBtn.disabled = true;

      const btnText = document.querySelector('.btn-text');
      const btnLoading = document.querySelector('.btn-loading');
      if (btnText) btnText.style.display = 'inline-flex';
      if (btnLoading) btnLoading.style.display = 'none';
    }
  }

  /* ── Form Submit — Loading State & AJAX ──── */
  if (uploadForm) {
    uploadForm.addEventListener('submit', async (e) => {
      e.preventDefault();

      const btnText = document.querySelector('.btn-text');
      const btnLoading = document.querySelector('.btn-loading');
      if (btnText) btnText.style.display = 'none';
      if (btnLoading) btnLoading.style.display = 'inline-flex';
      if (analyzeBtn) analyzeBtn.disabled = true;

      try {
        const formData = new FormData(uploadForm);
        const response = await fetch(uploadForm.action, {
          method: 'POST',
          body: formData,
          headers: { 'Accept': 'application/json' }
        });

        if (!response.ok) throw new Error('Network response was not ok');
        const data = await response.json();

        if (data.success) {
          // Hide upload panel, show result
          document.getElementById('upload-layout').style.display = 'none';
          const simpleResult = document.getElementById('simple-result');
          simpleResult.style.display = 'block';

          // Simple animation
          simpleResult.style.opacity = '0';
          simpleResult.style.transform = 'translateY(20px)';
          setTimeout(() => {
            simpleResult.style.transition = 'all 0.5s ease';
            simpleResult.style.opacity = '1';
            simpleResult.style.transform = 'translateY(0)';
          }, 50);

          // Populate data
          const res = data.result;
          document.getElementById('sr-image').src = '/static/uploads/' + data.filename;
          document.getElementById('sr-id').textContent = 'ID #' + data.prediction_id;
          document.getElementById('sr-plant').textContent = res.plant_type;
          document.getElementById('sr-remedy').textContent = res.remedy;

          const srBadge = document.getElementById('sr-badge');
          const srCard = document.getElementById('sr-card');
          const srDisease = document.getElementById('sr-disease');
          const srSeverityBox = document.getElementById('sr-severity-box');
          const srSeverityTitle = document.getElementById('sr-severity-title');
          const srSeverityDesc = document.getElementById('sr-severity-desc');

          const srConfValue = document.getElementById('sr-conf-value');
          const srConfBar = document.getElementById('sr-conf-bar');
          const srConfHint = document.getElementById('sr-conf-hint');

          // Animate Confidence Bar
          const targetConf = res.confidence_pct;
          srConfBar.setAttribute('data-healthy', res.is_healthy);
          srConfBar.style.width = '0%';
          setTimeout(() => { srConfBar.style.width = targetConf + '%'; }, 100);

          let current = 0;
          const step = 16, duration = 1000;
          const increment = targetConf / (duration / step);
          const timer = setInterval(() => {
            current = Math.min(current + increment, targetConf);
            srConfValue.textContent = current.toFixed(1) + '%';
            if (current >= targetConf) clearInterval(timer);
          }, step);

          if (targetConf >= 90) srConfHint.textContent = '🎯 Very high confidence';
          else if (targetConf >= 75) srConfHint.textContent = '✅ High confidence';
          else if (targetConf >= 60) srConfHint.textContent = '⚠️ Moderate confidence — consider retaking photo';
          else srConfHint.textContent = '❓ Low confidence — please retake with better lighting';

          if (res.is_healthy) {
            srBadge.className = 'result-image-badge badge-healthy';
            srBadge.textContent = '✓ Healthy';
            srCard.className = 'result-main-card card-healthy';
            srDisease.innerHTML = '<span class="healthy-icon">✅</span> ' + res.disease_name;
            srSeverityBox.style.display = 'none';
          } else {
            srBadge.className = 'result-image-badge badge-' + res.severity.toLowerCase();
            srBadge.textContent = '⚠ ' + res.severity + ' Risk';
            srCard.className = 'result-main-card card-disease';
            srDisease.innerHTML = '<span class="disease-icon">🔴</span> ' + res.disease_name;

            srSeverityBox.style.display = 'block';
            srSeverityBox.className = 'severity-card severity-' + res.severity.toLowerCase();

            let icon = res.severity === 'High' ? '🔴' : (res.severity === 'Medium' ? '🟡' : '🟢');
            srSeverityTitle.innerHTML = '<span class="severity-icon">' + icon + '</span> Severity: ' + res.severity;

            if (res.severity === 'High') {
              srSeverityDesc.innerHTML = 'This disease poses a <strong>high risk</strong>. Immediate treatment is strongly recommended to prevent crop loss.';
            } else if (res.severity === 'Medium') {
              srSeverityDesc.innerHTML = 'This disease poses a <strong>moderate risk</strong>. Treat within the next few days to prevent spreading.';
            } else {
              srSeverityDesc.innerHTML = 'This is a <strong>low risk</strong> issue. Monitor the plant and apply treatment as a precaution.';
            }
          }
        } else {
          showToast('❌ Failed to analyze image.', 'error');
          resetUpload();
        }
      } catch (err) {
        console.error(err);
        showToast('❌ An error occurred during analysis.', 'error');
        resetUpload();
      }
    });
  }

  /* ── Animated Confidence Bar (Result Page) ── */
  const confBar = document.getElementById('conf-bar');
  const confValue = document.getElementById('conf-value');
  if (confBar && confValue) {
    const target = parseFloat(confBar.dataset.target) || 0;
    // Trigger animation on load
    setTimeout(() => {
      confBar.style.width = target + '%';
    }, 300);
    // Count-up animation
    let current = 0;
    const duration = 1200;
    const step = 16;
    const increment = target / (duration / step);
    const timer = setInterval(() => {
      current = Math.min(current + increment, target);
      confValue.textContent = current.toFixed(1) + '%';
      if (current >= target) clearInterval(timer);
    }, step);
  }

  /* ── Animate elements on scroll (Intersection Observer) ────── */
  const animElements = document.querySelectorAll(
    '.step-card, .plant-card, .feature-card, .arch-card, .tech-card, .history-card'
  );
  if (animElements.length && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    animElements.forEach((el, i) => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(30px)';
      el.style.transition = `opacity 0.5s ease ${i * 60}ms, transform 0.5s ease ${i * 60}ms`;
      observer.observe(el);
    });
  }

  /* ── Performance Bars (Upload page) ─── */
  const perfBars = document.querySelectorAll('.perf-bar');
  if (perfBars.length && 'IntersectionObserver' in window) {
    const obs = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const width = entry.target.style.width;
          entry.target.style.width = '0';
          setTimeout(() => { entry.target.style.width = width; }, 100);
          obs.unobserve(entry.target);
        }
      });
    });
    perfBars.forEach(bar => obs.observe(bar));
  }

  /* ── Toast Notification ─── */
  function showToast(message, type = 'info') {
    const container = document.querySelector('.flash-container') || (() => {
      const c = document.createElement('div');
      c.className = 'flash-container';
      document.body.appendChild(c);
      return c;
    })();
    const toast = document.createElement('div');
    toast.className = `flash flash-${type === 'error' ? 'error' : 'success'}`;
    toast.innerHTML = `${message} <button onclick="this.parentElement.remove()">✕</button>`;
    container.appendChild(toast);
    setTimeout(() => toast.remove(), 5000);
  }

  /* ── Auto-dismiss flash messages ────── */
  document.querySelectorAll('.flash').forEach(flash => {
    setTimeout(() => {
      flash.style.opacity = '0';
      flash.style.transform = 'translateX(120%)';
      flash.style.transition = 'all 0.4s ease';
      setTimeout(() => flash.remove(), 400);
    }, 5000);
  });

  /* ── Smooth hero CTA ripple effect ──── */
  const heroCta = document.getElementById('hero-cta');
  if (heroCta) {
    heroCta.addEventListener('click', function (e) {
      const ripple = document.createElement('span');
      const rect = this.getBoundingClientRect();
      ripple.style.cssText = `
        position:absolute; border-radius:50%; background:rgba(255,255,255,0.2);
        width:10px; height:10px; transform:scale(0);
        left:${e.clientX - rect.left - 5}px; top:${e.clientY - rect.top - 5}px;
        animation: ripple 0.6s ease-out; pointer-events:none;
      `;
      this.style.position = 'relative'; this.style.overflow = 'hidden';
      this.appendChild(ripple);
      const s = document.createElement('style');
      s.textContent = `@keyframes ripple { to { transform:scale(30); opacity:0; } }`;
      document.head.appendChild(s);
      setTimeout(() => ripple.remove(), 700);
    });
  }

});
