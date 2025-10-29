"""
Utility to load per-source coverage configuration and apply year masks.

Recommended repo locations:
- Place this file at: utils/config_loader.py
- Place the YAML at: config/data_sources_coverage.yaml

Requires: pyyaml (add to environment/requirements_minimal.txt)
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any, Tuple
import os

try:
    import yaml  # type: ignore
except Exception as e:
    raise RuntimeError(
        "PyYAML is required. Please add 'pyyaml>=6.0' to environment/requirements_minimal.txt"
    ) from e

try:
    import pandas as pd  # type: ignore
except Exception:
    pd = None  # Only needed for masking helper that accepts DataFrame


@dataclass
class AnalysisWindow:
    start_year: int
    end_year: int


@dataclass
class SourceCoverage:
    key: str
    name: str
    coverage_start: int
    coverage_end: int
    notes: str | None = None


def load_coverage_config(path: str) -> Dict[str, Any]:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Coverage config not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    if not isinstance(cfg, dict):
        raise ValueError("Coverage config must be a YAML mapping at the top level")
    return cfg


def get_analysis_window(cfg: Dict[str, Any]) -> AnalysisWindow:
    aw = cfg.get("analysis_window", {})
    return AnalysisWindow(
        start_year=int(aw.get("start_year", 1990)),
        end_year=int(aw.get("end_year", 2023)),
    )


def get_source_coverage(cfg: Dict[str, Any], source_key: str) -> SourceCoverage:
    sources = cfg.get("sources", {})
    if source_key not in sources:
        raise KeyError(f"Source not found in config: {source_key}")
    s = sources[source_key]
    return SourceCoverage(
        key=source_key,
        name=str(s.get("name", source_key)),
        coverage_start=int(s.get("coverage_start", get_analysis_window(cfg).start_year)),
        coverage_end=int(s.get("coverage_end", get_analysis_window(cfg).end_year)),
        notes=s.get("notes"),
    )


def mask_years(values, start_year: int, end_year: int):
    """Mask a 1D iterable of years into [start_year, end_year]. Returns list of bools."""
    return [(start_year <= int(y) <= end_year) for y in values]


def mask_df_by_year(df, year_col: str, start_year: int, end_year: int):
    """Return a filtered DataFrame within [start_year, end_year]. Pandas optional."""
    if pd is None:
        raise RuntimeError("pandas is required for mask_df_by_year")
    if year_col not in df.columns:
        raise KeyError(f"Column not found: {year_col}")
    m = (df[year_col].astype(int) >= start_year) & (df[year_col].astype(int) <= end_year)
    return df.loc[m].copy()


def mask_df_by_source(df, year_col: str, cfg: Dict[str, Any], source_key: str):
    """Filter DataFrame to the valid coverage window of a specific source."""
    sc = get_source_coverage(cfg, source_key)
    return mask_df_by_year(df, year_col, sc.coverage_start, sc.coverage_end)


def effective_window_for_sources(cfg: Dict[str, Any], source_keys: list[str]) -> Tuple[int, int]:
    """Intersection window across given sources."""
    starts, ends = [], []
    for k in source_keys:
        sc = get_source_coverage(cfg, k)
        starts.append(sc.coverage_start)
        ends.append(sc.coverage_end)
    return max(starts), min(ends)


if __name__ == "__main__":
    # Minimal smoke test for manual runs
    cfg_path = os.environ.get("COVERAGE_YAML", "config/data_sources_coverage.yaml")
    cfg = load_coverage_config(cfg_path)
    aw = get_analysis_window(cfg)
    print(f"Analysis window: {aw.start_year}-{aw.end_year}")
    gbd = get_source_coverage(cfg, "gbd")
    print(f"GBD coverage: {gbd.coverage_start}-{gbd.coverage_end}")
