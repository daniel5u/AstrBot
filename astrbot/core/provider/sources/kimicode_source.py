import copy

from ..register import register_provider_adapter
from .anthropic_source import ProviderAnthropic

KIMICODE_DEFAULT_BASE_URL = "https://api.kimi.com/coding/"
KIMICODE_DEFAULT_USER_AGENT = "claude-code/0.1.0"


@register_provider_adapter(
    "kimicode_chat_completion",
    "KimiCode Chat Completion Provider Adapter",
)
class ProviderKimiCode(ProviderAnthropic):
    def __init__(
        self,
        provider_config: dict,
        provider_settings: dict,
    ) -> None:
        cfg = copy.deepcopy(provider_config)

        api_base = str(cfg.get("api_base", "") or "").strip()
        if not api_base:
            cfg["api_base"] = KIMICODE_DEFAULT_BASE_URL

        custom_headers = cfg.get("custom_headers", {})
        if not isinstance(custom_headers, dict):
            custom_headers = {}

        if not any(str(key).lower() == "user-agent" for key in custom_headers):
            custom_headers["User-Agent"] = KIMICODE_DEFAULT_USER_AGENT
        cfg["custom_headers"] = custom_headers

        super().__init__(cfg, provider_settings)
