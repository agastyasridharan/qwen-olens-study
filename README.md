# Qwen O-lens study

[Open the dashboard](https://agastyasridharan.github.io/qwen-olens-study/)

Static publication of the completed Qwen3.6-27B / O-lens motivated-reasoning study: 740 subject outputs, 47 diagnostic records, and 3,258 unique readouts. Includes full contexts, token/layer navigation, reviewed rationalization filters, matched references, numerical results, and dispositions of all 116 supplied claims.

The rationalization filter selects eight reviewed behavioral examples; it is not a prevalence estimate. The donation filter includes all 380 estimation-study records and their controls. Lens outputs are interpretations, not verified private thoughts. All subject actions are simulated text.

## Separate dense API follow-up

The [Dense scan view](https://agastyasridharan.github.io/qwen-olens-study/?view=dense) adds 2,047 verified Neuronpedia readouts from six accessible saved trajectories. The frozen selection included 12 trajectories and 7,848 planned cells; 5,801 cells could not be requested because the live API accepts only 2,048 tokens, below the assumed 4,096. No selected blackmail, leaking, or alarm activation fit. Complete original prefixes were preserved.

The new data and assessment are under `public/data/dense/`, with a frozen manifest, coverage deviation, hash audit, full contexts/token IDs, all readouts, and eight contextual examples. These results are separate from the original study and do not establish a faithful hidden motive. The API adapter revision is not supplied, so equivalence to the original instrument is unverified.

## Development

Node.js 22.13+ is required.

```sh
npm ci
npm run dev
npm run build
```

GitHub Pages serves the committed `docs/` directory from `main`. After editing, run `npm run build` and commit the updated source and `docs/` together. Static data are in `public/data/`; no server, API keys, or login are required.

To rebuild the data from the original local study artifacts:

```sh
python3 scripts/export-study.py /path/to/olens_motivated_reasoning_run
npm run build
```

`public/data/provenance.json` records the source UI commit and hashes of all source result/readout files. The report's internal dashboard links point to this publication; its scientific text is unchanged.
