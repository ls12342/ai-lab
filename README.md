# AI-Lab

Welcome to AI-Lab, an advanced research repository dedicated to the development and experimentation of artificial intelligence models tailored for content generation across image and audio domains.

## Project Overview

AI-Lab is at the forefront of multimedia content generation, exploring a wide range of AI models to produce innovative and diverse outputs. Our goal is to leverage cutting-edge AI techniques to push the boundaries of what's possible in digital content creation.

## Repository Structure

Our repository is meticulously organized with each AI model housed in its own dedicated directory. Inside each directory, you will find:

- **Scripts**: Executable Python scripts configured to utilize our AI models for generating content.
- **Demos**: A collection of output samples demonstrating the capabilities of our models. Each file is named after the prompt used for generation. These samples illustrate the potential of our models and are intended for demonstration purposes.

## Installation Guide

To ensure a smooth setup, please follow these steps:

### Prerequisites

Ensure that CUDA is installed on your system to leverage GPU acceleration for the models.

### Dependencies Installation

- **PyTorch Installation**: Check the compatible version for your CUDA from [PyTorch Official Site](https://pytorch.org/). Install PyTorch, torchvision, and torchaudio using:

```bash
   pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu<version>
```

Replace <version> with your CUDA version number.

- **Additional Python Libraries**:

```bash
pip install diffusers huggingface_hub safetensors accelerate
```

Install any additional dependencies as required.

## Executing Models

**Set Prompt**: Modify the prompt variable in the script with your desired text.

- **Run the Model**:

```bash
cd path_to_model_folder
python main.py
```

This script handles model downloading (if not locally available) and executes the generation process.

- **Environment Configuration** (Optional):
  Set an environment variable to specify a custom directory for model data:

```bash
export HF_HOME="PATH/TO/FOLDER"
```

## Note

The outputs in the demos folder are initial results intended to showcase model functionalities. These are not fully optimized and can be further refined by experimenting with various settings or prompts to enhance performance and quality.
