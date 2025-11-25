# 🤖 Robot Framework Test Generator

## Overview

The Robot Framework Test Generator is a **local, open-source solution** for generating automated test scripts in the Robot Framework format. Leveraging **local LLM models** via Ollama, the platform allows users to quickly create `.robot` test files using natural language descriptions.

The system includes built-in templates for:

* Web Testing
* API Testing
* Mobile Testing
* Car HLK (Hardware-in-the-Loop / ECU) Testing

The solution is designed to run fully **offline**, ensuring security and privacy for enterprise and automotive environments.

---

## Key Features

* Local generation using open-source LLMs (Qwen2.5, Llama3, Mistral, etc.)
* Streamlined web interface via **Streamlit**
* Predefined templates for common test categories, including automotive HLK
* Fully offline, requiring no API keys or cloud services
* Downloadable `.robot` scripts for immediate use
* Supports CAN, ECU, HIL, and diagnostic test automation

---

## Installation

1. Install Ollama and pull a compatible model (e.g., Qwen2.5).
2. Install Python dependencies and the Streamlit interface.
3. Launch the Streamlit app to access the web interface.

The system is designed for quick deployment in corporate environments with minimal configuration.

---

## User Interaction

Users interact with the system via a **web-based interface**.

* Users select a test category (Web, API, Mobile, or Car HLK).
* Users provide a **natural-language description** of the test scenario.
* The generator produces a valid Robot Framework script ready for download.

This approach allows **non-developers and engineers** to quickly define test cases without deep knowledge of Robot Framework syntax.

---

## Templates

The platform includes pre-built templates to accelerate test creation:

* **Web Testing** – Common web automation scenarios.
* **API Testing** – RESTful API validation tests.
* **Mobile Testing** – Basic mobile app test scaffolds.
* **Car HLK Testing** – ECU/HIL testing including CAN bus monitoring, sensor validation, and software version verification.

---

## Project Structure

* **app.py** – Main application interface.
* **templates/** – Folder containing all test templates for each category.
* **README.md** – Documentation and usage instructions.

This structure ensures maintainability and ease of extending the platform with new test templates.

---

## Roadmap

Future enhancements include:

* Diagnostic test templates based on UDS (ISO-14229)
* Automated test generation from CAN log analysis
* ECU firmware flashing and post-flash verification
* Advanced automotive test suites (ADAS, LIN, FlexRay)
* REST API backend for integration into CI/CD pipelines

---

## License

This project is released under the **MIT License**, making it suitable for corporate use and internal deployment.

---

## Contributions

Contributions, feature requests, and issues are welcome. Please adhere to the corporate code of conduct when collaborating.
