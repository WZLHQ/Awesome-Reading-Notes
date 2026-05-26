# Audio LLM

当前，语音交互大模型当前分为两个技术路线：

* Audio multitask model (AMM) --> LLM --> TTS

  * 其中AMM进行多任务音频理解同时得到文本形式输出，将其输入到LLM中，后续再进行TTS
  * AudioGPT
* Audio encoder --> LLM --> TTS

  * 其中Audio encoder仍然进行音频理解，其输出不再是文本形式而是特征形式。

## 相关文献

* Qwen-Audio series model:
  * [Qwen-audio](https://arxiv.org/pdf/2311.07919)
  * [Qwen2-audio](https://arxiv.org/pdf/2407.10759?)
  * [Qwen2.5-omini](https://arxiv.org/pdf/2503.20215)
  * [Qwen3-omini](https://arxiv.org/pdf/2509.17765)

* EMNLP2023, **SpeechGPT**, Fudan University, citation 688, [PDF](https://aclanthology.org/2023.findings-emnlp.1055.pdf), [code and models](https://github.com/0nutation/SpeechGPT)

  * SSL model-->LLM-->TTS，其中利用SSL的离散特征作为LLM的输入
* 2024, **FunAudioLLM**, Tongyi SpeechTeam, citation 105, [PDF](https://arxiv.org/pdf/2407.04051?), [Code(Inference and FT)](https://github.com/FunAudioLLM/SenseVoice), [Model](https://huggingface.co/FunAudioLLM/SenseVoiceSmall)

  * Audio multitask model (AMM)-->LLM-->TTS，其中利用AMM的文本作为LLM的输入
  * 待细读
