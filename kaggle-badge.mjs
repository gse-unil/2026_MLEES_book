// kaggle-badge.mjs
// MyST (Jupyter Book 2) plugin: add an "Open in Kaggle" badge to the top of
// every notebook (.ipynb) page, with the link computed from the page's own
// path at build time. Nothing is hand-written per page, so links cannot rot
// when files are renamed or moved.
//
// Shares one badge row with colab-badge.mjs (and any future cloud-launch
// badge plugin): each plugin looks for an existing row (marked via
// node.data.badgeRow) at the top of the page and appends into it instead of
// adding a new paragraph, so badges render inline on one line regardless of
// plugin order.
//
// Register in myst.yml:
//   project:
//     plugins:
//       - colab-badge.mjs
//       - kaggle-badge.mjs
//
// If you rename the repo or change the default branch, edit REPO / BRANCH.

import path from 'node:path';

const REPO = 'gse-unil/2026_MLEES_book';
const BRANCH = 'main';
const BADGE = 'https://img.shields.io/badge/Open%20in-Kaggle-20BEFF?logo=kaggle&logoColor=white';

function getBadgeRow(tree) {
  const first = tree.children[0];
  if (first && first.data && first.data.badgeRow) return first;
  const row = {
    type: 'paragraph',
    data: { badgeRow: true, hProperties: { className: 'notebook-badges' } },
    children: [],
  };
  tree.children.unshift(row);
  return row;
}

const addKaggleBadge = {
  name: 'add-kaggle-badge',
  doc: 'Inject an Open-in-Kaggle badge at the top of every notebook page.',
  stage: 'document',
  plugin: (_opts, _utils) => (tree, vfile) => {
    const src = vfile?.path;
    if (!src || !src.endsWith('.ipynb')) return; // notebooks only

    // path of the notebook relative to the project root (== its GitHub path)
    const rel = path
      .relative(process.cwd(), path.resolve(src))
      .split(path.sep)
      .join('/');

    const githubUrl = `https://github.com/${REPO}/blob/${BRANCH}/${rel}`;
    const url = `https://www.kaggle.com/kernels/welcome?src=${githubUrl}`;

    const row = getBadgeRow(tree);
    if (row.children.length > 0) row.children.push({ type: 'text', value: ' ' });
    row.children.push({
      type: 'link',
      url,
      children: [{ type: 'image', url: BADGE, alt: 'Open In Kaggle', align: 'left' }],
    });
  },
};

const plugin = { name: 'Kaggle badge', transforms: [addKaggleBadge] };
export default plugin;
