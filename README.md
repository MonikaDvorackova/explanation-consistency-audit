# Explanation Consistency Audit

Provides metrics for comparing feature attributions across paired inputs and recording deletion-test effects. Connect an explainer adapter (e.g. SHAP or Integrated Gradients) and define semantics-preserving transformations for the target modality.

Run `python3 main.py`. Similarity alone is not proof that an explanation is faithful; report prediction stability and intervention-based checks alongside it.
