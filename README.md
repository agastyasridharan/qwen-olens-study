# Qwen O-lens study

[Open the dashboard](https://agastyasridharan.github.io/qwen-olens-study/)

Static publication of the completed Qwen3.6-27B / O-lens motivated-reasoning study: 740 subject outputs, 47 diagnostic records, and 3,258 unique readouts. Includes full contexts, token/layer navigation, reviewed rationalization filters, matched references, numerical results, and dispositions of all 116 supplied claims.

The rationalization filter selects eight reviewed behavioral examples; it is not a prevalence estimate. The donation filter includes all 380 estimation-study records and their controls. Lens outputs are interpretations, not verified private thoughts. All subject actions are simulated text.

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
