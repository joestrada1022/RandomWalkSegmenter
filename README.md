# Random Walk Segmenter

Random-walk image segmentation experiment for a mathematical modeling class
independent research assignment. This project implements the core workflow of
the random walker segmentation method described in a research paper, using a
classic test image and simple user-provided seed markers to separate foreground
and background regions.

## What this project does

- Loads a sample grayscale image from scikit-image.
- Runs k-means clustering to make foreground/background separation easier.
- Adds two manual seed regions (foreground and background).
- Applies the random walker segmentation algorithm.
- Visualizes each step (original, clustered, seeds, final segmentation).

## Files

- segmentation.py: end-to-end experiment script.

## How to run

1. Install dependencies (see below).
2. Run the script:

```bash
python segmentation.py
```

## Dependencies

- Python 3
- numpy
- matplotlib
- scikit-learn
- scikit-image

## Next steps

- Add a more interactive interface (e.g., draw seeds on an image and re-run the
	segmentation live).

## Notes

This is a focused, self-contained implementation intended for learning and
analysis rather than a production-ready tool.