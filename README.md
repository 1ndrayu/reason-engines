# Reason-Engines: A Critical Reasoning Framework
Reason-Engines is a Python-based framework for systematic problem-solving, driven by reason, skepticism, and first-principles thinking. It evaluates data reliability, adjusts analysis depth to problem complexity, checks consensus, and blends deductive and inductive reasoning. Perfect for automated research, fact-checking, or decision support in domains like economics or science.

## Features
Confidence Scoring: Rates source reliability (e.g., academic vs. blog) using weighted metrics.
Decision-Rule Engine: Selects analysis depth (light, moderate, deep) based on query complexity.
Consensus Evaluation: Verifies claims against high-confidence sources for support or disputes.
Hybrid Reasoning: Merges first-principles deduction with data-driven induction for robust conclusions.

## Requirements
Python 3.6+
Standard json module (no external dependencies)

## Installation
Clone the repository:git clone https://github.com/your-username/reason-engines.git
cd reason-engines

## Usage
Create an input.json file with component data (see input.json.example for structure).
Run the framework:python framework.py
Review outputs for confidence scores, analysis mode, consensus status, and reasoning conclusions.

### Input File Structure
The input.json file included must be adhered to get error-free outputs.

### Example Output
Confidence Score: 0.88
Analysis Mode: deep
Consensus Status: no_consensus
Conclusion: Supply and demand govern prices. Data suggests do tariffs increase prices? likely increases.

---
