# 🩺 AI Skin Specialist — Agentic Multimodal Dermatology Assistant

> *Your skin has a story. Tell us what you're experiencing in your own voice, share a photo or video, and let our secure AI guide your path to clear skin.*

![Python](https://img.shields.io/badge/Python-3.14%2B-blue?style=flat-square&logo=python)
![Gradio](https://img.shields.io/badge/UI-Gradio_v6-orange?style=flat-square&logo=gradio)
![Google GenAI](https://img.shields.io/badge/AI-Gemini_2.5_Flash-green?style=flat-square&logo=google)

---

## 🚨 The Problem

Accessing dermatological care is often slow, expensive, and intimidating. Most initial digital triage systems suffer from two major flaws:
1. **Text-Only Limitations:** Patients find it difficult to write accurate clinical descriptions of rashes, lesions, or irritations.
2. **Static Image Constraints:** A single image lacks motion context, texture depth, and patient history spoken in real-time.

## 💡 The Solution

**AI Skin Specialist** bridges the gap between patient experience and preliminary guidance. It acts as an agentic clinical workflow pipeline that:
* **Listens:** Converts patient voice recordings into accurate text transcripts using Gemini 2.5 Flash.
* **Analyzes:** Evaluates patient voice descriptions alongside high-resolution images and videos of the skin area.
* **Responds:** Generates observational reports, severity estimations, home-care recommendations, and clear guidance on when to seek urgent care.
* **Speaks:** Converts the AI medical guidance back to audio for an accessible, human-centric patient experience.

---

## 🏗️ System Architecture & Workflow
Patient Input
(Voice + Image + Video)
          │
          ▼
Voice Processing
(Gemini 2.5 Speech-to-Text)
          │
          ▼
AI Skin Analysis
(Multimodal Reasoning Engine)
          │
          ▼
Doctor Response
(Text-to-Speech)
          │
          ▼
Gradio Interface
(Text & Audio Output)

## ✨ Features

* 🎙️ **Voice-First Input:** Speak your symptoms naturally using built-in microphone recording or audio uploads.
* 📷 **Multimodal Vision & Video:** Supports high-resolution skin photos and video clips to capture surface texture and dynamic lighting.
* 🤖 **Gemini 2.5 Flash Powered:** Fast, high-accuracy multimodal reasoning for visual and audio data.
* 🔊 **Spoken Medical Responses:** Generates spoken audio feedback for accessible triage results.
* 🛡️ **Safety & Disclaimers:** Built-in system prompts enforce medical boundary guardrails and automatic clinical disclaimers.

