# Code Completion

This repository provides tools for training, quantizing, and benchmarking code completion models. It supports end-to-end workflows including dataset preparation, model fine-tuning, quantization (LoRA), and latency evaluation.

---

## 📌 Requirements

* Python 3.12.8
* Ollama (required for latency benchmarking)

---

## ⚙️ Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/Anh39/Code-Completion
cd Code-Completion
```

---

### Step 2: Setup Environment

Create a Python 3.12.8 environment and install dependencies:

```bash
pip install -r requirements.txt
```

---

### Optional: Setup Quantization Environment

If you want to run model quantization:

1. Navigate to the `quantize` directory
2. Follow instructions in `install.ipynb`

Additionally:

* Clone llama.cpp into the `quantize` folder:

  ```bash
  git clone https://github.com/ggml-org/llama.cpp
  ```

* Download the latest prebuilt binaries from:
  https://github.com/ggml-org/llama.cpp/releases

---

## 🚀 Usage

---

### 🧠 Training

#### a. Prepare Training Data

Step 1: Download and filter dataset

```bash
python data/download_data.py
```

Step 2: Build training dataset

```bash
python data/prepare_data.py
```

---

#### b. Run Training

* Edit dataset paths and configurations in:

```
train/trainer.py
```

* Then run training (depending on your setup, e.g.):

```bash
python train/trainer.py
```

---

### ⚡ Quantize LoRA Model

* Open and configure:

```
quantize/quantize.ipynb
```

* Adjust paths and parameters, then run all cells.

---

### ⏱️ Latency Benchmark (Ollama)

Step 1: Start Ollama

Step 2: Modify model name in:

```
benchmark/benchmark-system.ipynb
```

Then run the notebook to measure latency.

---

## 📖 Notes

* Ensure correct Python version (3.12.8) to avoid compatibility issues.
* Quantization requires additional setup (llama.cpp).
* Latency benchmarking depends on Ollama being properly configured and machine hardware.

---


