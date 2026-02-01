## Naive Dockerfile observations

- Image size: 1.62MB
- Build time (first build): 12.070 s
- Build time (after code change): 32.281 s

### Problem observed
Even a small code change triggers a full dependency reinstall.

### Why this matters
In real environments, this slows down CI pipelines and increases costs.
