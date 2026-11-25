# 稀疏 Scatter/Gather 的别名与反向归属

这是一个 Python 算子工程的资料基线，包含与 共享视图、重复/越界索引和聚合约定。 运行约定和合成输入。资料文件只描述输入对象、版本和边界，不包含算子实现。

## 环境

项目运行和资料检查仅依赖 Python 标准库。运行测试与打包验证前安装锁定的测试工具：

```bash
python -m pip install -e .
python -m pip install -r requirements-test.txt
python -m unittest discover -s tests -v
python -m build --wheel --no-isolation
```

## 资料

`data/input.json` 是可重复使用的本地合成输入，`data/schema.json` 记录字段含义和允许的状态。包目录保留公开入口的命名空间；调用方可以在此基础上接入自己的批处理或推理流程。
