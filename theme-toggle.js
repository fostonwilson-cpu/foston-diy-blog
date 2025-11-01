(function () {
  'use strict';

  const toggle = document.getElementById('toggle-theme');
  if (!toggle) {
    return;
  }

  const applyTheme = (theme) => {
    const isDark = theme === 'dark';
    document.body.classList.toggle('dark-mode', isDark);
    toggle.textContent = isDark ? '☀️' : '🌙';
    toggle.setAttribute('aria-pressed', isDark ? 'true' : 'false');
  };

  let storedTheme = null;
  try {
    storedTheme = window.localStorage.getItem('foston-theme');
  } catch (error) {
    storedTheme = null;
  }

  const sanitizedStoredTheme = storedTheme === 'dark' || storedTheme === 'light' ? storedTheme : null;

  const prefersDark =
    sanitizedStoredTheme === null &&
    typeof window.matchMedia === 'function' &&
    window.matchMedia('(prefers-color-scheme: dark)').matches;

  const initialTheme = sanitizedStoredTheme || (prefersDark ? 'dark' : 'light');
  applyTheme(initialTheme);

  toggle.addEventListener('click', () => {
    const nextTheme = document.body.classList.contains('dark-mode') ? 'light' : 'dark';
    applyTheme(nextTheme);

    try {
      window.localStorage.setItem('foston-theme', nextTheme);
    } catch (error) {
      /* ignore storage errors */
    }
  });
})();
