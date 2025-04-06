# LiteLLM 自定義 API 服務器

這是一個使用 LiteLLM 框架的自定義 LLM API 服務器實現。該項目展示了如何創建和集成自定義 LLM 處理程序。

## 功能特點

- 自定義 LLM 實現，支持同步和異步操作
- 支持文本完成（completion）功能
- ⚠️ 注意：目前不支持自定義 embedding 功能（參見 [GitHub Issue #8660](https://github.com/BerriAI/litellm/issues/8660)）
- 可配置的模型設置
- 調試模式支持

## 安裝

1. 克隆此倉庫：
```bash
git clone [repository-url]
cd wrenai-litellm-custom-api-server
```

2. 安裝依賴：
```bash
pip install -r requirements.txt
```

## 配置

項目使用 `litellm_config.yaml` 進行配置：

```yaml
model_list:
  - model_name: "my-custom-model"
    litellm_params:
      model: "my-custom-llm/my-custom-model"

litellm_settings:
  custom_provider_map:
    - {"provider": "my-custom-llm", "custom_handler": "custom_handler.my_custom_llm"}
  debug: true
```

## 使用方法

1. 啟動服務器：
```bash
python -m litellm --config litellm_config.yaml
```

2. API 端點：
- 完成（Completion）: `/v1/completions`
- ⚠️ 嵌入（Embedding）: `/v1/embeddings` - 目前不可用，等待 LiteLLM 官方支持

## 自定義處理程序

自定義處理程序位於 `custom_handler.py`，實現了以下功能：
- 文本完成（completion）
- ⚠️ 文本嵌入（embedding）- 目前不可用，等待 LiteLLM 官方支持
- 同步和異步操作支持

## 開發

要擴展或修改自定義處理程序，請編輯 `custom_handler.py` 文件。主要類別為 `MyCustomLLM`，您可以在其中實現自己的邏輯。

### 已知限制

- 自定義 embedding 功能目前不可用，這是因為 LiteLLM 尚未正式支持自定義 embedding 提供者。相關討論請參見 [GitHub Issue #8660](https://github.com/BerriAI/litellm/issues/8660)。
- 當前的 embedding 實現僅返回虛擬向量，不應在生產環境中使用。

## 許可證

[添加許可證信息]
