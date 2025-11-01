(function () {
  'use strict';

  const form = document.getElementById('tips-filter');
  const status = document.querySelector('.tips-filter__status');
  const articles = Array.from(document.querySelectorAll('.tips-card'));
  const emptyState = document.querySelector('.tips-empty');

  if (!form || !status || articles.length === 0) {
    return;
  }

  const input = form.querySelector('#tips-query');
  const tagInputs = Array.from(form.querySelectorAll('input[name="tag"]'));

  const normalize = (value) => value.toLowerCase().trim();
  const allowedTagPattern = /^[a-z0-9-]+$/;
  const sanitizeTags = (values) =>
    values
      .map((value) => normalize(value || ''))
      .filter((value) => allowedTagPattern.test(value));

  const datasetToTags = (datasetValue) => {
    if (typeof datasetValue !== 'string') {
      return [];
    }

    return sanitizeTags(datasetValue.split(/\s+/).filter(Boolean));
  };

  const update = () => {
    const query = normalize(input ? input.value : '').slice(0, 120);
    const activeTags = sanitizeTags(
      tagInputs
        .filter((checkbox) => checkbox.checked)
        .map((checkbox) => (typeof checkbox.value === 'string' ? checkbox.value : ''))
    );

    let visibleCount = 0;

    articles.forEach((article) => {
      const list = article.querySelector('ul[data-tags]');
      const tags = list ? datasetToTags(list.dataset.tags) : [];
      const text = normalize(article.textContent || '');
      const matchesQuery = query === '' || text.includes(query);
      const matchesTags =
        activeTags.length === 0 || activeTags.every((tag) => tags.includes(tag));

      const visible = matchesQuery && matchesTags;
      article.hidden = !visible;
      if (visible) {
        visibleCount += 1;
      }
    });

    if (emptyState) {
      emptyState.hidden = visibleCount !== 0;
    }

    const tagSummary = activeTags.length
      ? `Filtered by ${activeTags.length} tag${activeTags.length > 1 ? 's' : ''}`
      : 'All tags';
    const querySummary = query ? ` and matching “${query}”` : '';
    const collectionSummary =
      visibleCount === articles.length && !query && activeTags.length === 0
        ? 'Showing all collections.'
        : `Showing ${visibleCount} collection${visibleCount === 1 ? '' : 's'} (${tagSummary}${querySummary}).`;

    status.textContent = collectionSummary;
  };

  form.addEventListener('input', update);
  form.addEventListener('reset', () => {
    window.setTimeout(update, 0);
  });

  update();
})();
