# ASR with LLMs

* 2024-7-10, [Seed-ASR](https://arxiv.org/pdf/2407.04675): Understanding Diverse Speech and Contexts with LLM-based Speech Recognition

  * has used accent/dialect data
* 2025-1-24, [FireRedASR](https://arxiv.org/pdf/2501.14350): pen-Source Industrial-Grade Mandarin Speech Recognition Models
  from Encoder-Decoder to LLM Integration

  * has used accent/dialect data
* 2025-10-5, [Fun-ASR](https://arxiv.org/pdf/2509.12508), Fun-ASR Technical Report.

  * Nothing innovative but massive data, a lot of unjustified fine-tuning steps, and the use of massive GPUs.

### The connector between speech encoder and LLMs

* two layers of transformer encoder, the output of Audio Encoder is fed into the connector.

  * [Fun-ASR](https://arxiv.org/pdf/2509.12508)
* downsampling module with a linear projection layer.

  * [Seed-ASR](https://arxiv.org/pdf/2407.04675)
* Linear-ReLU-Linear network with frame splicing operation to reduce the temporal resolution from 40ms to 80ms per frame

  * [FireRedASR](https://arxiv.org/pdf/2501.14350)

### The input type of LLM

* **continuous** speech representations with text instructions.
  * [Seed-ASR](https://arxiv.org/pdf/2407.04675), [FireRedASR](https://arxiv.org/pdf/2501.14350), [Fun-ASR](https://arxiv.org/pdf/2509.12508)
