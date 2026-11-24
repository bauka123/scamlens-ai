"""ScamLens package."""

from .coordinator import analyze
from .llm import analyze_with_llm

__all__ = ["analyze", "analyze_with_llm"]
