'use strict';
const research = JSON.parse(document.querySelector('#research-data').textContent);
const sources = new Map(research.sources.map(source => [source.id, source]));
const $ = selector => document.querySelector(selector);
function element(tag, text, className) {
  const node = document.createElement(tag);
  if (text !== undefined) node.textContent = text;
  if (className) node.className = className;
  return node;
}
function link(label, url) {
  const node = element('a', label);
  node.href = url;
  return node;
}
function references(ids) {
  const row = element('div', undefined, 'references');
  for (const id of ids) {
    const source = sources.get(id);
    row.append(link(`${id} · ${source.publisher}`, source.url));
  }
  return row;
}
const statusSelect = $('#status');
for (const status of [...new Set(research.claims.map(c => c.status))].sort()) {
  const option = element('option', status.replaceAll('-', ' '));
  option.value = status;
  statusSelect.append(option);
}
function renderResearch() {
  const query = $('#search').value.trim().toLocaleLowerCase();
  const matches = object => JSON.stringify(object).toLocaleLowerCase().includes(query);
  const claims = research.claims.filter(claim =>
    ($('#era').value === 'all' || claim.era === $('#era').value) &&
    (statusSelect.value === 'all' || claim.status === statusSelect.value) &&
    matches({...claim, evidence: claim.sources.map(id => sources.get(id))}));
  $('#claim-count').textContent = `${claims.length} of ${research.claims.length} claims`;
  const list = $('#claim-list');
  list.replaceChildren();
  for (const claim of claims) {
    const article = element('article', undefined, 'claim');
    article.id = claim.id;
    const heading = element('div', undefined, 'claim-label');
    heading.append(element('span', `${claim.id} / ${claim.era} / ${claim.topic}`),
      element('span', claim.status.replaceAll('-', ' '), `badge ${claim.status}`));
    article.append(heading, element('h3', claim.statement), element('p', claim.scope, 'scope'));
    const details = element('details');
    details.append(element('summary', 'Evidence and unresolved questions'), references(claim.sources));
    if (claim.locator) details.append(element('p', claim.locator, 'caption'));
    details.append(element('p', `Unresolved: ${claim.unresolved}`));
    article.append(details);
    list.append(article);
  }
  if (!claims.length) list.append(element('p', 'No claims match. Clear search or choose another era or status.', 'empty'));
  const sourceRows = research.sources.filter(matches);
  $('#source-count').textContent = `${sourceRows.length} of ${research.sources.length} source records`;
  const library = $('#source-list');
  library.replaceChildren();
  for (const source of sourceRows) {
    const item = element('details', undefined, 'source');
    const summary = element('summary');
    summary.append(element('span', `${source.id} · ${source.title}`), element('span', source.access, 'badge'));
    item.append(summary, link(`${source.publisher} · Open original source`, source.url),
      element('p', `Published: ${source.published ?? 'not established'} · Checked: ${source.checked} · ${source.kind}`, 'caption'),
      element('p', `Supports: ${source.support}`), element('p', `Limits: ${source.limitations}`, 'limits'));
    library.append(item);
  }
  if (!sourceRows.length) library.append(element('p', 'No sources match. Try a broader phrase or a source ID.', 'empty'));
}
for (const selector of ['#search', '#era', '#status']) $(selector).addEventListener('input', renderResearch);
renderResearch();
for (const event of [...research.timeline].sort((a, b) => b.date.localeCompare(a.date))) {
  const entry = element('article', undefined, 'event');
  entry.append(element('p', `${event.date} · ${event.kind}`, 'event-date'), element('h3', event.title),
    element('p', event.summary), references(event.sources));
  $('#timeline-list').append(entry);
}
function calculate(event) {
  if (event) event.preventDefault();
  const t = Number($('#time').value), m = Number($('#mass').value), mph = Number($('#speed').value);
  if (![t, m, mph].every(Number.isFinite) || t <= 0 || m <= 0 || mph < 0 ||
      !$('#lab-form').checkValidity()) {
    $('#lab-error').textContent = 'Enter a positive time and mass, and a non-negative speed within the displayed limits.';
    $('#lab-result').replaceChildren();
    return;
  }
  $('#lab-error').textContent = '';
  const v = mph * 0.44704;
  const a = v / t;
  const values = [
    ['Average acceleration', `${(a / 9.80665).toFixed(2)} g`],
    ['Average net force', `${(m * a / 1000).toFixed(1)} kN`],
    ['Translational kinetic energy', `${(0.5 * m * v * v / 3600000).toFixed(3)} kWh`],
    ['Distance at constant acceleration', `${(0.5 * v * t).toFixed(2)} m`]
  ];
  const output = element('dl', undefined, 'lab-output');
  for (const [label, value] of values) output.append(element('dt', label), element('dd', value));
  $('#lab-result').replaceChildren(output);
}
$('#lab-form').addEventListener('submit', calculate);
calculate();
