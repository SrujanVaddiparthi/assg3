# ACE: Automatic Concept Extraction for Bias Evaluation

## Overview
This repository implements the Automatic Concept Extraction (ACE) method to evaluate bias in facial recognition models. The main goal is to explore how ACE can automatically extract relevant concepts and assess whether certain concepts disproportionately influence model predictions, particularly concerning skin tone and facial features.

## Repository Structure
- **ACE/**: Contains the core implementation of the ACE method.
  - `ace_helpers.py`: Helper functions for running ACE.
  - `ace_run.py`: Main script for executing the ACE method.
  - `ace.py`: Contains the concept discovery implementation.
  - `imagenet_labels.txt`: Labels for the ImageNet dataset.
  - `results/`: Directory for storing results and discovered concepts.
- **tensorflow_inception_graph.pb**: Pre-trained Inception model graph file.
- **run_command.txt**: Contains the command to run the ACE method.
- **preprocessed_images/**: Directory containing preprocessed images for analysis.
- **UTKFace_resized/**: Directory containing the UTKFace dataset images resized for processing.
- **LICENSE**: The license under which the project is distributed.

## Getting Started
To run the ACE analysis, use the command provided in `run_command.txt`. Ensure you have all the necessary dependencies installed, and update the paths according to your local setup.

## Bias Evaluation
This project focuses on the evaluation of bias in facial recognition models using ACE. The analysis includes examining how different concepts extracted from images impact model predictions, with a particular focus on potential biases related to skin tone.

## Acknowledgments
- The original ACE paper by Ghorbani et al. (2019) for foundational concepts.
- The developers of the UTKFace dataset for providing access to the data.

## Authors
- Srujan Vaddiparthi - [GitHub Profile](<https://github.com/SrujanVaddiparthi>)
