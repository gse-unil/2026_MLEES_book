// colab-badge.mjs
// MyST (Jupyter Book 2) plugin: add an "Open in Colab" badge to the top of
// every notebook (.ipynb) page, with the link computed from the page's own
// path at build time. Nothing is hand-written per page, so links cannot rot
// when files are renamed or moved.
//
// Register in myst.yml:
//   project:
//     plugins:
//       - colab-badge.mjs
//
// If you rename the repo or change the default branch, edit REPO / BRANCH.

import path from 'node:path';

const REPO = 'gse-unil/2026_MLEES_book';
const BRANCH = 'main';
const BADGE = 'https://colab.research.google.com/assets/colab-badge.svg';

const addColabBadge = {
  name: 'add-colab-badge',
  doc: 'Inject an Open-in-Colab badge at the top of every notebook page.',
  stage: 'document',
  plugin: (_opts, _utils) => (tree, vfile) => {
    const src = vfile?.path;
    if (!src || !src.endsWith('.ipynb')) return; // notebooks only

    // path of the notebook relative to the project root (== its GitHub path)
    const rel = path
      .relative(process.cwd(), path.resolve(src))
      .split(path.sep)
      .join('/');

    const url = `https://colab.research.google.com/github/${REPO}/blob/${BRANCH}/${rel}`;

    const badge = {
      type: 'paragraph',
      children: [
        {
          type: 'link',
          url,
          children: [
            { type: 'image', url: BADGE, alt: 'Open In Colab', align: 'left' },
          ],
        },
      ],
    };

    tree.children.unshift(badge); // place it first on the page
  },
};

const plugin = { name: 'Colab badge', transforms: [addColabBadge] };
export default plugin;
