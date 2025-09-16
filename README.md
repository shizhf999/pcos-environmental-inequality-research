# Open Science Release (PCOS Inequality & Modeling Study)

本目录提供论文复现所需的核心方法脚本、环境说明与结构示例。

## 目录结构
- code/: 方法与分析核心脚本 (method110, 变量选择, Shapley, Theil & Concentration 分析等)
- environment/: 最小运行依赖 (requirements_minimal.txt)
- data_sample/: 数据结构示例与占位说明，不含敏感全量数据
- docs/: （待添加）方法流程图与再现指南
- results_samples/: （可选）放置部分生成结果 JSON/CSV 示例

## 快速开始
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r environment/requirements_minimal.txt
```

## 再现性与哈希
完整哈希追踪请参考主仓库中的 HASHES_SUMMARY_FINAL_PACKAGE_v2f.txt 与 FINAL freeze 标记。

## 数据获取
研究使用的聚合/派生数据结构可通过 data_sample/ 中的示例了解格式。敏感或授权受限数据需按照文档指引自行获取。

## 许可证
建议：代码采用 MIT；文档和图像采用 CC-BY 4.0（或根据期刊政策调整）。

## 引用
请引用主论文与 CITATION.cff 中列出的引用信息。

## 联系
Issues / Pull Requests 欢迎用于改进方法或扩展再现脚本。

## results_scripts 来源说明
'code/results_scripts' 目录包含从原始 'results' 路径中抽取的分析脚本副本（已移除调试/一次性脚本）。
参见 docs/RESULTS_SCRIPTS_INDEX.md 与 docs/RESULTS_SCRIPTS_STATIC_AUDIT.md 获取列表与静态审计。
