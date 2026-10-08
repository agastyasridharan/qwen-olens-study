import examples from './data/reviewed-examples.json';

// Curated from the completed full-context reviews in FINAL_REPORT.md.
// These are selected behavioral examples, not an exhaustive prevalence label.
export const overtIds = new Set([
  'accurate-good_below--direct--07',
  'am-blackmail-america-replacement--think--10',
  'am-leaking-global-replacement--think--00',
  'am-murder-america-replacement--think--19',
  'ws-rh-unit-tests--think--00',
  'ws-rh-metric-gaming--think--00',
  'ws-selfpreserve-shutdown--think--00',
  'ws-oversight-disable-logging--think--00',
]);
export const reviewedExamples = examples;
export const reviewFor = (id: string) => examples.find(e => e.record === id);
type RecordInfo = {id:string;family:string;kind:string};
export const isEstimation = (r:RecordInfo) => r.family === 'donation' && ['natural','fixed_prefix'].includes(r.kind);
export const evidenceOptions = [
  {value:'', label:'All records'},
  {value:'overt', label:'Overt rationalization · reviewed'},
  {value:'estimation', label:'Incentive-driven estimation · study'},
  {value:'both', label:'Both categories'},
];
export function matchesEvidence(r:RecordInfo, filter:string) {
  if(filter==='overt') return overtIds.has(r.id);
  if(filter==='estimation') return isEstimation(r);
  if(filter==='both') return overtIds.has(r.id) || isEstimation(r);
  return true;
}
export const evidenceDescription = (filter:string) => filter==='overt'
  ? 'Eight selected, full-context-reviewed examples of overt justification or goal-directed assumption selection. This is not a prevalence estimate; an untagged record is not a negative finding. Reviews were performed by Codex, not independent human raters.'
  : filter==='estimation'
  ? 'All 380 donation-study records, including baseline and other controls. Incentive sensitivity is established across conditions; membership does not label an individual answer as motivated reasoning.'
  : 'Reviewed overt rationalization and the complete donation estimation study. Behavioral evidence does not establish a concealed motive decoded by O-lens.';
